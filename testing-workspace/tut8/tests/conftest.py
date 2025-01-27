import pytest
from app.student import Student
from datetime import datetime

# Fixtures
@pytest.fixture
def student_factory():
    """Factory fixture for creating students with custom parameters."""
    def make_dummy_student(name, credits):
        return Student(name, datetime(2000, 1, 1), "COE", credits)
    return make_dummy_student


@pytest.fixture()
def dummy_student(request):
    """Fixture for creating a student with dynamic credits."""
    return Student("nikhil", datetime(2000, 1, 1), "COE", request.param)
