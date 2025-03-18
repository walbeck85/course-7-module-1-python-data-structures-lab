import pytest
from lib.set_operations import unique_majors
from lib.student_data import students

def test_unique_majors():
    majors = unique_majors(students)
    assert "Computer Science" in majors
    assert "Mathematics" in majors
    assert len(majors) == 3  # Expected 3 unique majors

def test_empty_students():
    assert unique_majors([]) == set()
