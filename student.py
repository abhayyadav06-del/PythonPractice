import os

# Student Class
class Student:
    def __init__(self, roll, name, age, course):
        self.roll = roll
        self.name = name
        self.age = age
        self.course = course

    def __str__(self):
        return f"{self.roll},{self.name},{self.age},{self.course}"


# File Name
FILE_NAME = "students.txt"


# Add Student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = Student(roll, name, age, course)

    with open(FILE_NAME, "a") as file:
        file.write(str(student) + "\n")

    print("Student Added Successfully!\n")


# View Students
def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

            if not data:
                print("No Student Records Found.\n")
                return

            print("\n------ Student Records ------")
            for line in data:
                roll, name, age, course = line.strip().split(",")
                print(f"Roll: {roll}")
                print(f"Name: {name}")
                print(f"Age: {age}")
                print(f"Course: {course}")
                print("--------------------------")

    except FileNotFoundError:
        print("No Records File Found!\n")


# Search Student
def search_student():
    roll_no = input("Enter Roll Number to Search: ")

    try:
        with open(FILE_NAME, "r") as file:
            found = False

            for line in file:
                roll, name, age, course = line.strip().split(",")

                if roll == roll_no:
                    print("\nStudent Found")
                    print("Roll:", roll)
                    print("Name:", name)
                    print("Age:", age)
                    print("Course:", course)
                    found = True
                    break

            if not found:
                print("Student Not Found.\n")

    except FileNotFoundError:
        print("No Records File Found.\n")


# Update Student
def update_student():
    roll_no = input("Enter Roll Number to Update: ")

    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        found = False

        with open(FILE_NAME, "w") as file:
            for line in students:
                roll, name, age, course = line.strip().split(",")

                if roll == roll_no:
                    print("Enter New Details")
                    name = input("Name: ")
                    age = input("Age: ")
                    course = input("Course: ")

                    student = Student(roll, name, age, course)
                    file.write(str(student) + "\n")
                    found = True
                else:
                    file.write(line)

        if found:
            print("Student Updated Successfully!\n")
        else:
            print("Student Not Found.\n")

    except FileNotFoundError:
        print("No Records File Found.\n")


# Delete Student
def delete_student():
    roll_no = input("Enter Roll Number to Delete: ")

    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        found = False

        with open(FILE_NAME, "w") as file:
            for line in students:
                roll, name, age, course = line.strip().split(",")

                if roll == roll_no:
                    found = True
                else:
                    file.write(line)

        if found:
            print("Student Deleted Successfully!\n")
        else:
            print("Student Not Found.\n")

    except FileNotFoundError:
        print("No Records File Found.\n")


# Main Menu
def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank You!")
            break

        else:
            print("Invalid Choice! Try Again.")


# Start Program
menu()