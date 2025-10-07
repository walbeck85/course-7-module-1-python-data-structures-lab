# This module contains functions to lazily generate student data.

def student_generator(student_list, major):
    """Return a generator yielding students filtered by major."""
    return (student for student in student_list if student[2].lower() == major.lower())