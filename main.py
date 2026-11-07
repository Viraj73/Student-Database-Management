import mysql.connector as sqltor
from datetime import datetime
import sys

# Connecting Python and MySQL
try:
    mycon = sqltor.connect(
        host="localhost",
        user="root",
        password="viraj12345",  # Update with your local password
        database="student_manage",
        auth_plugin="mysql_native_password"
    )
except sqltor.Error as err:
    print(f"\nConnection not established: {err}")
    sys.exit(1)


def student_table():
    cursor = mycon.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Student_details (
        Roll_No INT PRIMARY KEY,
        Admission_Number INT,
        First_Name VARCHAR(50),
        Second_Name VARCHAR(50),
        Father_Name VARCHAR(50),
        Mother_Name VARCHAR(50),
        Gender VARCHAR(10),
        State VARCHAR(30),
        Enrollment_Date DATE
    )""")
    mycon.commit()
    cursor.close()


def initial_query():
    cursor = mycon.cursor()
    insert_query = """INSERT IGNORE INTO Student_details (
        Roll_No, Admission_Number, First_Name, Second_Name, Father_Name, 
        Mother_Name, Gender, State, Enrollment_Date
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    student_details = [
        (1, 1001, 'Rohan', 'Verma', 'Ajay Verma', 'Sunita Verma', 'Male', 'Delhi', '2015-01-10'),
        (2, 1002, 'Meera', 'Sharma', 'Vijay Sharma', 'Pooja Sharma', 'Female', 'Delhi', '2014-02-15'),
        (3, 1003, 'Amit', 'Gupta', 'Suresh Gupta', 'Anita Gupta', 'Male', 'Delhi', '2016-03-20'),
        (4, 1004, 'Sakshi', 'Mishra', 'Ravi Mishra', 'Seema Mishra', 'Female', 'Delhi', '2013-04-25'),
        (5, 1005, 'Vikas', 'Singh', 'Raj Singh', 'Kiran Singh', 'Male', 'Delhi', '2017-05-30'),
        (6, 1006, 'Priya', 'Kumar', 'Dinesh Kumar', 'Rita Kumar', 'Female', 'Delhi', '2015-06-05'),
        (7, 1007, 'Anjali', 'Joshi', 'Manoj Joshi', 'Neha Joshi', 'Female', 'Delhi', '2018-07-10'),
        (8, 1008, 'Arjun', 'Reddy', 'Surya Reddy', 'Lakshmi Reddy', 'Male', 'Delhi', '2014-08-15'),
        (9, 1009, 'Nisha', 'Patel', 'Kiran Patel', 'Suman Patel', 'Female', 'Delhi', '2016-09-20'),
        (10, 1010, 'Rahul', 'Chopra', 'Ashok Chopra', 'Mina Chopra', 'Male', 'Delhi', '2013-10-25'),
        (11, 1011, 'Pooja', 'Nair', 'Ramesh Nair', 'Latha Nair', 'Female', 'Delhi', '2015-11-30'),
        (12, 1012, 'Karan', 'Menon', 'Vikas Menon', 'Anitha Menon', 'Male', 'Delhi', '2017-12-05'),
        (13, 1013, 'Sneha', 'Das', 'Amit Das', 'Mona Das', 'Female', 'Delhi', '2018-01-10'),
        (14, 1014, 'Vikram', 'Singh', 'Anil Singh', 'Geeta Singh', 'Male', 'Delhi', '2014-02-15'),
        (15, 1015, 'Richa', 'Roy', 'Ajit Roy', 'Shila Roy', 'Female', 'Delhi', '2016-03-20')
    ]
    cursor.executemany(insert_query, student_details)
    mycon.commit()
    cursor.close()


def delete_student(input_value):
    print("\n-- Deleting Student Details --")
    cursor = mycon.cursor()
    cursor.execute(
        "DELETE FROM Student_details WHERE Roll_No = %s OR Admission_Number = %s",
        (input_value, input_value)
    )
    mycon.commit()
    if cursor.rowcount > 0:
        print(f'Student with Roll No. or Admission No. "{input_value}" deleted.')
    else:
        print('Student not found.')
    cursor.close()


def search_student(input_value):
    print("\n-- Searching Student Details --")
    cursor = mycon.cursor()
    query = "SELECT * FROM Student_details WHERE Roll_No = %s OR Admission_Number = %s"
    cursor.execute(query, (input_value, input_value))
    result = cursor.fetchone()
    if result:
        print(f"Student found:\n"
              f"  Roll No: {result[0]} | Admission No: {result[1]}\n"
              f"  Name: {result[2]} {result[3]}\n"
              f"  Parents: {result[4]} (Father), {result[5]} (Mother)\n"
              f"  Gender: {result[6]} | State: {result[7]} | Enrolled: {result[8]}")
    else:
        print("Student not found.")
    cursor.close()


def add_student_by_user():
    print("\n-- Adding Student Details --")
    try:
        roll_no = int(input("Enter Roll No.: "))
        admission_no = int(input("Enter Admission No.: "))
        first_name = input("Enter First Name: ").strip()
        second_name = input("Enter Second Name: ").strip()
        father_name = input("Enter Father Name: ").strip()
        mother_name = input("Enter Mother Name: ").strip()
        gender = input("Enter Gender: ").strip()
        state = input("Enter State: ").strip()
        enrollment_date = input("Enter Enrollment Date (YYYY-MM-DD): ").strip()
        enrollment_date_obj = datetime.strptime(enrollment_date, '%Y-%m-%d').date()

        cursor = mycon.cursor()
        insert_query = """INSERT INTO Student_details (
            Roll_No, Admission_Number, First_Name, Second_Name, Father_Name, 
            Mother_Name, Gender, State, Enrollment_Date
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        cursor.execute(insert_query, (
            roll_no, admission_no, first_name, second_name, father_name, 
            mother_name, gender, state, enrollment_date_obj
        ))
        mycon.commit()
        cursor.close()
        print("Student record added successfully.")
    except ValueError as ve:
        print(f"Invalid input: {ve}")


def student_details_menu():
    while True:
        print("\n-- Student Details Menu --")
        print("1. Delete Student")
        print("2. Search Student")
        print("3. Add Student by User Input")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            val = input("Enter Roll No. or Admission No. to delete: ").strip()
            delete_student(val)
        elif choice == '2':
            val = input("Enter Roll No. or Admission No. to search: ").strip()
            search_student(val)
        elif choice == '3':
            add_student_by_user()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")


def marks_table():
    cursor = mycon.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Marks (
        Roll_number INT,
        admission_number INT,
        Name VARCHAR(50),
        exam_name VARCHAR(30),
        Subject VARCHAR(30),
        marks_obtained INT
    )""")
    mycon.commit()
    cursor.close()


def insert_marks():
    print("\n-- Insert Student Marks --")
    name = input("Name of Student: ").strip()
    roll_num = input("Roll Number: ").strip()
    ad_num = input("Admission Number: ").strip()

    if not roll_num.isdigit() or not ad_num.isdigit():
        print("Roll Number and Admission Number must be numeric.")
        return

    print("Exams: PT-1, HALF-YEARLY, PT-2, PREBOARDS, BOARDS")
    ex_nm = input("Enter Exam Name: ").strip()

    subjects = ["Maths", "English", "Chemistry", "Physics", "Physical Education"]
    print("Choose additional subject:\n1. Computer Science\n2. Hindi")
    sub_choice = input("Choice (1 or 2): ").strip()
    if sub_choice == '1':
        subjects.append("Computer Science")
    elif sub_choice == '2':
        subjects.append("Hindi")

    cursor = mycon.cursor()
    for sub in subjects:
        mr = input(f"Enter Marks for {sub} (0-100): ").strip()
        if mr.isdigit() and 0 <= int(mr) <= 100:
            cursor.execute("""INSERT INTO Marks (
                Roll_number, admission_number, Name, exam_name, Subject, marks_obtained
            ) VALUES (%s, %s, %s, %s, %s, %s)""",
            (int(roll_num), int(ad_num), name.upper(), ex_nm.upper(), sub, int(mr)))
    mycon.commit()
    cursor.close()
    print("Marks inserted successfully.")


def update_marks():
    print("\n-- Update Marks --")
    roll_number = input("Enter Roll Number: ").strip()
    exam_name = input("Enter Exam Name: ").strip()

    if not roll_number.isdigit():
        return

    cursor = mycon.cursor()
    cursor.execute(
        "SELECT DISTINCT Subject FROM Marks WHERE Roll_number = %s AND exam_name = %s",
        (int(roll_number), exam_name.upper())
    )
    subjects = cursor.fetchall()
    if not subjects:
        print("No subjects found.")
        cursor.close()
        return

    for subject in subjects:
        sub_name = subject[0]
        cursor.execute(
            "SELECT marks_obtained FROM Marks WHERE Roll_number = %s AND exam_name = %s AND Subject = %s",
            (int(roll_number), exam_name.upper(), sub_name)
        )
        current = cursor.fetchone()
        print(f"\nCurrent marks for {sub_name}: {current[0] if current else 'N/A'}")
        new_marks = input(f"New marks for {sub_name} (leave blank to skip): ").strip()
        if new_marks and new_marks.isdigit():
            cursor.execute("""UPDATE Marks SET marks_obtained = %s 
                              WHERE Roll_number = %s AND exam_name = %s AND Subject = %s""",
                           (int(new_marks), int(roll_number), exam_name.upper(), sub_name))
            mycon.commit()
    cursor.close()


def search_marks():
    print("\n-- Search Marks --")
    print("1. Admission Number\n2. Roll Number")
    choice = input("Choice: ").strip()
    identifier = input("ID: ").strip()
    exam_name = input("Exam Name: ").strip()

    if not identifier.isdigit():
        return

    cursor = mycon.cursor()
    field = "admission_number" if choice == '1' else "Roll_number"
    cursor.execute(f"SELECT * FROM Marks WHERE {field} = %s AND exam_name = %s",
                   (int(identifier), exam_name.upper()))
    marks = cursor.fetchall()
    if marks:
        print(f"\nStudent: {marks[0][2]} | Roll: {marks[0][0]} | Exam: {marks[0][3]}")
        for m in marks:
            print(f"  {m[4]:<20}: {m[5]}")
    else:
        print("No records found.")
    cursor.close()


def delete_marks():
    print("\n-- Delete Marks --")
    ex_nm = input("Exam Name: ").strip()
    choice = input("1. Admission Number\n2. Roll Number\nChoice: ").strip()
    identifier = input("ID: ").strip()

    if not identifier.isdigit():
        return

    cursor = mycon.cursor()
    field = "admission_number" if choice == '1' else "Roll_number"
    cursor.execute(f"DELETE FROM Marks WHERE {field} = %s AND exam_name = %s", 
                   (int(identifier), ex_nm.upper()))
    mycon.commit()
    print("Records deleted.")
    cursor.close()


def marksheet_menu():
    while True:
        print("\n-- Student Marksheet Menu --")
        print("1. Insert Marks\n2. Update Marks\n3. Search Marks\n4. Delete Marks\n5. Back")
        c = input("Choice: ").strip()
        if c == '1': insert_marks()
        elif c == '2': update_marks()
        elif c == '3': search_marks()
        elif c == '4': delete_marks()
        elif c == '5': break


if __name__ == "__main__":
    student_table()
    initial_query()
    marks_table()

    while True:
        print("\n" + "=" * 35)
        print("     STUDENT MANAGEMENT SYSTEM     ")
        print("       ~ Created by Viraj Mittal   ")
        print("=" * 35)
        print("1. STUDENT DETAILS\n2. STUDENT MARKSHEET\n3. Exit")
        opt = input("\nChoose an option (1-3): ").strip()
        if opt == '1':
            student_details_menu()
        elif opt == '2':
            marksheet_menu()
        elif opt == '3':
            mycon.close()
            break
