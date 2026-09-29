from app.safety.response_validator import validate_response


def test_valid_response():
    response = (
        "Your hemoglobin is below the reference range. "
        "This can have several possible explanations. "
        "This explanation is not a diagnosis."
    )

    is_valid, issues = validate_response(response)

    assert is_valid is True
    assert issues == []


def test_empty_response_is_invalid():
    is_valid, issues = validate_response("")

    assert is_valid is False
    assert "Response is empty." in issues


def test_medication_advice_is_flagged():
    response = (
        "Your result is abnormal. "
        "You should take iron supplements. "
        "This explanation is not a diagnosis."
    )

    is_valid, issues = validate_response(response)

    assert is_valid is False
    assert len(issues) > 0


def test_missing_safety_statement_is_flagged():
    response = (
        "Your hemoglobin is below the reference range."
    )

    is_valid, issues = validate_response(response)

    assert is_valid is False
    assert any(
        "missing required safety statement" in issue
        for issue in issues
    )