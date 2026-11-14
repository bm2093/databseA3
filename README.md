## Database Management Systems F26 Assignment 3

## Setup

1. Install dependency:
cmd 
pip install psycopg2-binary

2. Create a database in PostgreSQL and run the schema SQL in pgAdmin:
   `sql
   CREATE TABLE students (
       student_id SERIAL PRIMARY KEY,
       first_name TEXT NOT NULL,
       last_name TEXT NOT NULL,
       email TEXT NOT NULL UNIQUE,
       enrollment_date DATE
   );

   INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
   ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
   ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
   ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
   `
3. Update the DB_CONFIG in a3_CRUD_ops.py with your postgre credentials if needed (mine was passwordless)

## Run
cmd
python a3_CRUD_ops.py

## Functions

- getAllStudents() - Retrieves and prints all student records, done initially and for final
- addStudent(first_name, last_name, email, enrollment_date) - Inserts a new student record
- updateStudentEmail(student_id, new_email) - Updates a student's email by ID
- deleteStudent(student_id) - Deletes a student record by ID