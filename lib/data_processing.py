# lib/data_processing.py

# This module contains functions to process student data.
# Format student data for display.
def format_student_data(student):
    """Return: 'ID: 10 | Name: Louis Medina | Major: Computer Science'."""
    sid, name, major = student
    return f"ID: {sid} | Name: {name} | Major: {major}"
    
# Display a list of students.
def display_students(students):
    """Print one formatted line per student."""
    for s in students:
        print(format_student_data(s))