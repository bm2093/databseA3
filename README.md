## Database Management Systems F26 Assignment 3

## Video Demonstration
https://youtu.be/hO1uqx5rDm0?si=vOdBiLwmesEfWuVu

## Setup

1. Install dependency:
cmd 
pip install psycopg2-binary

2. Create a database in PostgreSQL and run the schema SQL in pgAdmin:

3. Update the DB_CONFIG in a3_CRUD_ops.py with your postgre credentials if needed (mine was passwordless)

## Run
cmd
python src/a3_CRUD_ops.py

Note: If re-running the script, reset the table (`TRUNCATE TABLE students RESTART IDENTITY;` followed by the initial `INSERT` statements) to avoid duplicate `email` errors and missing-ID deletes

## Functions

- getAllStudents() - Retrieves and prints all student records, done initially and for final
- addStudent(first_name, last_name, email, enrollment_date) - Inserts a new student record
- updateStudentEmail(student_id, new_email) - Updates a student's email by ID
- deleteStudent(student_id) - Deletes a student record by ID
