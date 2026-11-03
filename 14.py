
import pickle
import shelve

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("\nStudent Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)


def save_pickle(student):
    with open("student.dat", "wb") as file:
        pickle.dump(student, file)

    print("Object saved using Pickle!")


def load_pickle():
    try:
        with open("student.dat", "rb") as file:
            student = pickle.load(file)

        print("Object restored using Pickle!")
        student.display()

    except FileNotFoundError:
        print("Pickle file not found!")


def save_shelve(student):
    with shelve.open("student_db") as db:
        db["student"] = student

    print("Object saved using Shelve!")


def load_shelve():
    with shelve.open("student_db") as db:
        if "student" in db:
            student = db["student"]
            print("Object restored using Shelve!")
            student.display()
        else:
            print("No student record found!")


while True:
    print("\n===== OBJECT PERSISTENCE SYSTEM =====")
    print("1. Create Student")
    print("2. Save Object Using Pickle")
    print("3. Load Object Using Pickle")
    print("4. Save Object Using Shelve")
    print("5. Load Object Using Shelve")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        marks = float(input("Enter marks: "))

        student = Student(name, roll, marks)
        print("Student object created!")

    elif choice == "2":
        if "student" in globals():
            save_pickle(student)
        else:
            print("Create a student first!")

    elif choice == "3":
        load_pickle()

    elif choice == "4":
        if "student" in globals():
            save_shelve(student)
        else:
            print("Create a student first!")

    elif choice == "5":
        load_shelve()

    elif choice == "6":
        print("Exiting Object Persistence System...")
        break

    else:
        print("Invalid choice!")
