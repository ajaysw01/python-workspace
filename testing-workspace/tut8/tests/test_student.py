from datetime import datetime
import pytest
from app.student import Student

# Tests
def test_student_get_age(dummy_student):
    """Test if get_age calculates the correct age."""
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age


@pytest.mark.parametrize("credits,expected", [(19, False), (21, True)])
def test_student_is_eligible_for_degree(make_dummy_student, credits, expected):
    """Test is_eligible_for_degree with a factory-created student."""
    student = make_dummy_student("Sam", credits)
    assert Student.is_eligible_for_degree(student) == expected


@pytest.mark.parametrize("dummy_student,expected", [(19, False), (21, True)], indirect=["dummy_student"])
def test_student_is_eligible_for_degree_with_fixture(dummy_student, expected):
    """Test is_eligible_for_degree using the dummy_student fixture."""
    assert Student.is_eligible_for_degree(dummy_student) == expected
