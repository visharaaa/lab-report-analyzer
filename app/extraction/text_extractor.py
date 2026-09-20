"""
Utilities for extracting laboratory results from report text.
"""

import re

from app.models.schemas import LabResult
from app.normalization.test_names import normalize_test_name


def classify_result(
    value: float,
    reference_low: float | None,
    reference_high: float | None,
) -> str | None:
    """Classify a result using the laboratory-provided reference range."""

    if reference_low is None or reference_high is None:
        return None

    if value < reference_low:
        return "low"

    if value > reference_high:
        return "high"

    return "normal"


def extract_reference_range(
    text: str,
) -> tuple[float | None, float | None]:
    """
    Extract a numeric reference range.

    Examples:
        12.0 - 15.0
        12 - 15
        4.0–11.0
    """

    match = re.search(
        r"(\d+(?:\.\d+)?)\s*[-–]\s*(\d+(?:\.\d+)?)",
        text,
    )

    if not match:
        return None, None

    return float(match.group(1)), float(match.group(2))


def extract_value(text: str) -> float | None:
    """Extract the first numeric value from a line."""

    match = re.search(r"\b\d+(?:\.\d+)?\b", text)

    if not match:
        return None

    return float(match.group())


def extract_unit(text: str, value: float) -> str | None:
    """
    Extract the unit appearing immediately after the result value.
    Supports units such as:
    - g/dL
    - mg/dL
    - %
    - fL
    - 10^9/L
    - 10^12/L
    """

    match = re.match(
        r"^\s*\d+(?:\.\d+)?\s*([A-Za-z0-9%]+(?:[/^][A-Za-z0-9]+)*)",
        text,
    )

    if not match:
        return None

    return match.group(1)


def extract_test_name(text: str) -> str | None:
    """
    Extract a recognized laboratory test name from the beginning of a line.
    """

    cleaned_text = text.strip()

    # Try longer names first so "RBC Count" is checked before "RBC".
    known_names = sorted(
        normalize_test_name.__globals__["TEST_NAME_MAP"].keys(),
        key=len,
        reverse=True,
    )

    for name in known_names:
        pattern = rf"^{re.escape(name)}\s+"
        match = re.match(pattern, cleaned_text, re.IGNORECASE)

        if match:
            return cleaned_text[:match.end()].strip()

    return None


def extract_results(text: str) -> list[LabResult]:
    """
    Extract recognizable laboratory results from report text.
    """

    results = []

    for line in text.splitlines():
        line = line.strip()

        if not line:
            continue

        test_name = extract_test_name(line)

        if not test_name:
            continue

        canonical_name = normalize_test_name(test_name)

        if canonical_name is None:
            continue

        remaining_text = line[len(test_name):].strip()

        value = extract_value(remaining_text)

        if value is None:
            continue

        reference_low, reference_high = extract_reference_range(remaining_text)

        unit = extract_unit(remaining_text, value)

        flag = classify_result(
            value,
            reference_low,
            reference_high,
        )

        results.append(
            LabResult(
                test_name=test_name,
                canonical_name=canonical_name,
                value=value,
                unit=unit,
                reference_low=reference_low,
                reference_high=reference_high,
                flag=flag,
            )
        )

    return results