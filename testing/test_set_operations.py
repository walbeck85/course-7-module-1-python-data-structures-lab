from lib.set_operations import unique_majors

students = [
    (101, "Alice Johnson", "Computer Science"),
    (102, "Bob Smith", "Mathematics"),
    (103, "Charlie Davis", "Physics"),
    (104, "David Wilson", "Computer Science"),
    (105, "Eve Lewis", "Mathematics"),
]

secondary_students = [
    (101, "Miles", "Mathematics"),
    (102, "Laura", "Mathematics"),
    (103, "Benji", "Physics"),
    (104, "Natalia", "Physics"),
    (105, "Nadia", "Mathematics"),
]

def test_unique_majors():
    majors = unique_majors(students)
    assert "Computer Science" in majors
    assert "Mathematics" in majors
    assert "Physics" in majors
    assert len(majors) == 3  # Expected 3 unique majors
    majors = unique_majors(secondary_students)
    assert "Computer Science" not in majors
    assert "Mathematics" in majors
    assert "Physics" in majors
    assert len(majors) == 2  # Expected 3 unique majors

def test_empty_students():
    assert unique_majors([]) == set()
