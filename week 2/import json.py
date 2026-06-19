import json
import os

FILE_NAME = "students.json"

def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

def add_student():
    students = load_students()

    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number: ")
    department = input("Enter Department: ")

    student = {
        "name": name,
        "roll_no": roll_no,
        "department": department
    }

    students.append(student)
    save_students(students)

    print("Student Added Successfully!")

def view_students():
    students = load_students()

    if not students:
        print("No Records Found!")
        return

    print("\nStudent Records")
    print("-" * 40)

    for student in students:
        print(f"Name       : {student['name']}")
        print(f"Roll No    : {student['roll_no']}")
        print(f"Department : {student['department']}")
        print("-" * 40)

def search_student():
    students = load_students()

    roll_no = input("Enter Roll Number: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found")
            print(student)
            return

    print("Student Not Found!")

def delete_student():
    students = load_students()

    roll_no = input("Enter Roll Number to Delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            save_students(students)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")

def main():
    while True:
        print("\n===== STUDENT DATABASE SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Thank You!")
            break
        else:
            print("Invalid Choice!")

main()