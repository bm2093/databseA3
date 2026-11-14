import psycopg2
from psycopg2 import Error

# Database config (passwordless so i dont think it matters)
DB_CONFIG = {
    "dbname": "a3",
    "user": "postgres",
    "password": "1234",
    "host": "localhost",
    "port": "5432"
}

def get_connection():
    """Establish and return a database connection."""
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        return connection
    except (Exception, Error) as error:
        print("Error connecting", error)
        return None

def getAllStudents():
    """1. Retrieves and displays all records from the students table."""
    conn = get_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT student_id, first_name, last_name, email, enrollment_date FROM students;")
        records = cursor.fetchall()
        print("\n-- All Students --")
        for row in records:
            print(f"ID: {row[0]} | Name: {row[1]} {row[2]} | Email: {row[3]} | Enrolled: {row[4]}")
        cursor.close()
    except (Exception, Error) as error:
        print("Error getting the data", error)
    finally:
        conn.close()

def addStudent(first_name, last_name, email, enrollment_date):
    """2. Inserts a new student record into the students table."""
    conn = get_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO students (first_name, last_name, email, enrollment_date) 
            VALUES (%s, %s, %s, %s);
        """
        cursor.execute(query, (first_name, last_name, email, enrollment_date))
        conn.commit()
        print(f"\nAdded student of: {first_name} {last_name}")
        cursor.close()
    except (Exception, Error) as error:
        conn.rollback()
        print("Error inserting student", error)
    finally:
        conn.close()

def updateStudentEmail(student_id, new_email):
    """3. Updates the email address for a student with the specified student_id."""
    conn = get_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        query = "UPDATE students SET email = %s WHERE student_id = %s;"
        cursor.execute(query, (new_email, student_id))
        conn.commit()
        print(f"\nUpdated email for student ID of {student_id} to {new_email}")
        cursor.close()
    except (Exception, Error) as error:
        conn.rollback()
        print("Error updating email", error)
    finally:
        conn.close()

def deleteStudent(student_id):
    """4. Deletes the record of the student with the specified student_id."""
    conn = get_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        query = "DELETE FROM students WHERE student_id = %s;"
        cursor.execute(query, (student_id,))
        conn.commit()
        print(f"\nDeleted student with the ID of {student_id}")
        cursor.close()
    except (Exception, Error) as error:
        conn.rollback()
        print("Error deleting", error)
    finally:
        conn.close()


if __name__ == "__main__":
    # view initial 
    getAllStudents()

    # new student
    addStudent("Shai", "Gillgeous", "SG.Alexander@example.com", "2023-09-03")

    # update student email 
    updateStudentEmail(1, "john.doe.new@example.com")

    # delete a student 
    deleteStudent(3)

    # view final 
    getAllStudents()
