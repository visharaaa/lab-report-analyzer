from app.safety.response_validator import validate_response


def test_valid_response():
    response = (
        "Your hemoglobin is below the reference range. "
        "This can have several possible explanations."
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
        "You should take iron supplements."
    )

    is_valid, issues = validate_response(response)

    assert is_valid is False
    assert len(issues) > 0