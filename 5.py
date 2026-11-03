
import os
import sys

def show_directory():
    print("\nCurrent Directory:", os.getcwd())
    print("\nFiles and Folders:")

    items = os.listdir()

    for item in items:
        print(item)


def create_workspace():
    folder = input("Enter workspace folder name: ")

    if not os.path.exists(folder):
        os.mkdir(folder)
        print("Workspace created successfully!")
    else:
        print("Folder already exists!")


def navigate_directory():
    path = input("Enter directory path: ")

    if os.path.isdir(path):
        os.chdir(path)
        print("Directory changed to:", os.getcwd())
    else:
        print("Invalid directory path!")


def list_files():
    extension = input("Enter file extension (e.g. .py, .txt): ")

    print("\nMatching Files:")

    for file in os.listdir():
        if file.endswith(extension):
            print(file)


def manage_log():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "activity.txt"

    try:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                print("\nExisting Log Content:")
                print(file.read())
        else:
            with open(filename, "w") as file:
                file.write("File Management Utility Log\n")
                file.write("Log file created successfully.\n")

            print("New log file created:", filename)

    except (OSError, UnicodeError) as e:
        print("File error:", e)


while True:
    print("\n===== FILE MANAGEMENT UTILITY =====")
    print("1. Show Current Directory")
    print("2. Create Workspace")
    print("3. Navigate Directory")
    print("4. List Files by Extension")
    print("5. Read or Create Log File")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_directory()

    elif choice == "2":
        create_workspace()

    elif choice == "3":
        navigate_directory()

    elif choice == "4":
        list_files()

    elif choice == "5":
        manage_log()

    elif choice == "6":
        print("Exiting File Management Utility...")
        break

    else:
        print("Invalid choice! Try again.")
