"""
Utilities for normalizing extracted laboratory results.
"""

from app.models.schemas import LabResult
from app.normalization.test_names import normalize_test_name


def normalize_result(result: LabResult) -> LabResult:
    """
    Normalize the test name of a laboratory result.

    The original test name is preserved while the canonical
    name is assigned for internal processing.
    """

    canonical_name = normalize_test_name(result.test_name)

    return result.model_copy(
        update={
            "canonical_name": canonical_name,
        }
    )


def normalize_results(results: list[LabResult]) -> list[LabResult]:
    """
    Normalize a list of laboratory results.
    """

    return [
        normalize_result(result)
        for result in results
    ]