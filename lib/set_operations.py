# lib/set_operations.py

# This module contains operations related to sets.
# Extract unique majors from student data.
def unique_majors(students):
    """Return a set of unique student majors using set comprehension."""
    return {major for _, _, major in students}