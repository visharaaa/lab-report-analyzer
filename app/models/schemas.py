from typing import List, Optional, Literal
from pydantic import BaseModel, Field


class LabResult(BaseModel):
    """Represents a single laboratory test result."""

    test_name: str = Field(
        description="The test name exactly as it appears on the laboratory report."
    )

    canonical_name: Optional[str] = Field(
        default=None,
        description="Standardized name used internally by the system."
    )

    value: float = Field(
        description="Numerical value of the laboratory result."
    )

    unit: Optional[str] = Field(
        default=None,
        description="Unit used for the reported result."
    )

    reference_low: Optional[float] = Field(
        default=None,
        description="Lower limit of the laboratory-provided reference range."
    )

    reference_high: Optional[float] = Field(
        default=None,
        description="Upper limit of the laboratory-provided reference range."
    )

    flag: Optional[Literal["low", "normal", "high"]] = Field(
        default=None,
        description="Interpretation based on the laboratory-provided reference range."
    )

    extraction_confidence: Optional[float] = Field(
        default=None,
        ge=0.0,
        le=1.0,
        description="Confidence that the result was correctly extracted from the report."
    )


class LabReport(BaseModel):
    """Represents a complete laboratory report."""

    report_id: Optional[str] = Field(
        default=None,
        description="Unique identifier assigned to the laboratory report."
    )

    results: List[LabResult] = Field(
        default_factory=list,
        description="Laboratory test results extracted from the report."
    )