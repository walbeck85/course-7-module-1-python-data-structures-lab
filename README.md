# Student Data Management System — Lab

> A compact, hands‑on lab that demonstrates how to model student records with **lists & tuples**, filter data with **list comprehensions**, track uniqueness with **sets**, and process data lazily with **generator expressions**.

---

## Overview
This lab implements a small **Student Data Management System**. You will:
- Store student records using **lists** and **tuples**
- Filter by major using a **list comprehension**
- Format and display records for readable output
- Extract **unique majors** with a **set comprehension**
- Iterate lazily by major using a **generator expression**

---

## What Was Implemented
- **Step 1:** `student_data.py` — seed data as tuples `(id, name, major)`
- **Step 2:** `filters.py` — `filter_students_by_major(students, major)` (list comprehension)
- **Step 3:** `data_processing.py` — `format_student_data(student)` and `display_students(students)`
- **Step 4:** `set_operations.py` — `unique_majors(students)` (set comprehension)
- **Step 5/6:** `data_generator.py` — `student_generator(student_list, major)` (generator expression)

All functions are small, single‑purpose, and covered by tests.

---

## Project Structure
```
lib/
  __init__.py
  data_generator.py        # student_generator
  data_processing.py       # format_student_data, display_students
  filters.py               # filter_students_by_major
  set_operations.py        # unique_majors
  student_data.py          # students seed
pytest.ini
testing/
  test_data_generator.py
  test_data_processing.py
  test_filters.py
  test_set_operations.py
```

---

## Setup & Installation

1. Clone your fork of this repository:
   ```bash
   git clone git@github.com:walbeck85/course-7-module-1-python-data-structures-lab.git
   ```
2. Install dependencies and start a new virtual environment:
   ```bash
   pipenv install && pipenv shell
   ```

---

## Run Tests
Run the full suite:
```bash
pytest -x
```
Or run a specific step while developing:
```bash
pytest -x testing/test_filters.py
pytest -x testing/test_data_processing.py
pytest -x testing/test_set_operations.py
pytest -x testing/test_data_generator.py
```

---

## Usage Examples
```python
from lib.student_data import students
from lib.filters import filter_students_by_major
from lib.data_processing import display_students, format_student_data
from lib.set_operations import unique_majors
from lib.data_generator import student_generator

# Display all students
display_students(students)

# Filter by major (list comprehension)
cs_students = filter_students_by_major(students, "Computer Science")
print([format_student_data(s) for s in cs_students])

# Unique majors (set comprehension)
print(unique_majors(students))

# Lazy iteration by major (generator expression)
math_gen = student_generator(students, "Mathematics")
print(next(math_gen))  # First math student
for s in student_generator(students, "Mathematics"):
    print(s)
```

---

## Troubleshooting
- **Module not found / imports**: ensure you run commands from the repo root and that your Pipenv shell is active.
- **Pytest not found**: run `pipenv install --dev pytest` then `pipenv run pytest -x`.
- **Wrong environment**: `exit`, then `pipenv shell` again in this repo.

---


## Best Practices
- Keep comprehensions readable; move complex logic to helpers
- Prefer set membership (`in my_set`) over linear scans
- Use docstrings and concise comments for intent
- Commit in small, meaningful chunks with clear messages

---
