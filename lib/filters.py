# This module contains functions for filtering student data.

# lib/filters.py
def filter_students_by_major(students, major):
    """Return a list of student tuples whose major matches (case-insensitive)."""
    m = major.lower()
    return [s for s in students if s[2].lower() == m]
