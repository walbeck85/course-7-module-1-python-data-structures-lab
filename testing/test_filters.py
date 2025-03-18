import pytest
from lib.filters import filter_students_by_major
from lib.student_data import students

def test_filter_students_by_major():
    cs_students = filter_students_by_major(students, "Computer Science")
    assert len(cs_students) == 2
    assert cs_students[0][1] == "Alice Johnson"

def test_filter_no_results():
    result = filter_students_by_major(students, "Biology")
    assert result == []
