from tut2.app.sample import validate_age
import pytest

def test_validate_age_valid_age() : 
    validate_age(20)

def test_validate_age_invalid_age() :
    with pytest.raises(ValueError, match="Age cannot be less than zero"):
        validate_age(-1)
