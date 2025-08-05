# Student Data Management System Lab

## Learning Goals

- Utilize **lists, tuples, dictionaries, and sets** to store and manage student records.
- Apply **list comprehensions** and **dictionary comprehensions** for efficient data filtering.
- Use **generator expressions** to process large datasets efficiently.
- Implement **set operations** for tracking unique student attributes.
- Structure a Python application with modular data management techniques.

## Introduction

In this lab, you will build a **Student Data Management System** that allows users to store, filter, and process student records efficiently. The system will enable users to:

- Store and retrieve student information using **lists, tuples, dictionaries, and sets**.
- Filter student data dynamically using **list comprehensions** and **dictionary comprehensions**.
- Process large student datasets efficiently using **generator expressions**.
- Track unique student attributes (e.g., **majors, completed courses**) using **sets**.

This lab will help you apply Python **data structures** to solve real-world problems efficiently and dynamically.

## Setup Instructions

### Fork and Clone the Repository

1. Go to the provided GitHub repository link.
2. Fork the repository to your GitHub account.
3. Clone the forked repository to your local machine using:
   ```sh
   git clone <repo-url>
   cd course-7-module-1-python-data-structures-lab
   ```

### Install Dependencies

Ensure **Python** is installed:
```sh
python --version
```

Run the following command to install dependencies:
```sh
pipenv install
```

Run the following to enter the virtual environment:
```sh
pipenv shell
```

To run the test suite, use:
```sh
pytest -x
```

## Tasks

### Task 1: Define the Problem

The goal of this lab is to build a **Student Data Management System** that allows users to store, retrieve, and process student records efficiently. The system must provide the following capabilities:

- Manage student records using **lists, dictionaries, and sets**.
- Filter student data dynamically using **list comprehensions** and **dictionary comprehensions**.
- Process large datasets efficiently using **generator expressions**.
- Track unique student attributes (e.g., completed courses) using **sets**.

The key challenge is to apply **efficient Python data structures** to dynamically handle, filter, and process student information.

---

### Task 2: Determine the Design

The **Student Data Management System** will be built using structured data handling techniques, including:

- **Lists & Tuples**: Store student data in structured collections.
- **List Comprehensions & Generator Expressions**: Process and filter student records efficiently.
- **Dictionaries**: Store student attributes using key-value pairs for fast lookups.
- **Sets**: Track unique student data attributes such as completed courses and enrolled majors.

#### Design Breakdown:
- **Student list storage** using **tuples** and **lists**.
- **Filtering capabilities** using **list comprehensions**.
- **Memory-efficient data handling** with **generator expressions**.
- **Fast lookups and updates** using **dictionaries**.
- **Tracking unique attributes** using **sets**.

This structured approach ensures an **efficient, maintainable, and scalable** student data system.

---

### Task 3: Develop the Code

#### Step 1: Define Student Records using Lists and Tuples

```python
# List of students stored as tuples (ID, Name, Major)
students = [
    (101, "Alice Johnson", "Computer Science"),
    (102, "Bob Smith", "Mathematics"),
    (103, "Charlie Davis", "Physics"),
    (104, "David Wilson", "Computer Science"),
    (105, "Eve Lewis", "Mathematics"),
]

def display_students(student_list):
    """Display student records"""
    print("\nStudent Records:")
    for sid, name, major in student_list:
        print(f"ID: {sid} | Name: {name} | Major: {major}")

display_students(students)
```

#### Step 2: Filtering Students Using List Comprehensions

```python
def filter_students_by_major(student_list, major):
    """Filter students by major using a list comprehension"""
    filtered = [student for student in student_list if student[2] == major]
    
    if filtered:
        print(f"\nStudents majoring in {major}:")
        display_students(filtered)
    else:
        print(f"\nNo students found in {major}.")

filter_students_by_major(students, "Computer Science")
```

#### Step 3: Processing Large Student Datasets Using a Generator Expression

```python
def student_generator(student_list, major):
    """Generate student records lazily for memory efficiency"""
    return (student for student in student_list if student[2] == major)

# Creating a generator for Mathematics students
math_students = student_generator(students, "Mathematics")

# Retrieving student records lazily
print(next(math_students))  # Output: (102, "Bob Smith", "Mathematics")
print(next(math_students))  # Output: (105, "Eve Lewis", "Mathematics")
```

#### Step 4: Managing Student Data Using Dictionaries

```python
# Dictionary storing student data with ID as key
student_dict = {
    101: {"name": "Alice Johnson", "major": "Computer Science", "courses": {"CS101", "CS102"}},
    102: {"name": "Bob Smith", "major": "Mathematics", "courses": {"MATH101", "MATH102"}},
    103: {"name": "Charlie Davis", "major": "Physics", "courses": {"PHYS101", "PHYS102"}},
}

def display_student_details(student_db):
    """Display student details from a dictionary"""
    print("\nStudent Details:")
    for sid, details in student_db.items():
        print(f"ID: {sid} | Name: {details['name']} | Major: {details['major']} | Courses: {details['courses']}")

display_student_details(student_dict)
```

#### Step 5: Updating Student Courses Using Set Operations

```python
def add_course(student_db, student_id, new_course):
    """Add a new course to a student's course set"""
    if student_id in student_db:
        student_db[student_id]["courses"].add(new_course)
        print(f"\nAdded {new_course} to {student_db[student_id]['name']}'s courses.")
    else:
        print("\nStudent not found.")

add_course(student_dict, 101, "CS201")

# Display updated student data
display_student_details(student_dict)
```

---

## Best Practices for Managing Student Data

- **Use comments** to clarify logic.
- **Optimize lookups** with dictionary `.get()` method.
- **Use set operations** for efficient course tracking.
- **Apply generator expressions** for memory efficiency.
- **Update README** to document functionality.

## Conclusion

By mastering **Sequences, List Comprehensions, Generator Expressions, Dictionaries, and Sets**, developers can:

- Optimize **student data storage and retrieval**.
- Enhance **performance using efficient data structures**.
- Improve **scalability using structured data management techniques**.

This lab ensures real-world applicability of Python **data structures** in managing dynamic, scalable, and efficient datasets.