from .studentregister import register_student
from .studentsearch import search_by_qualification
from .allstudentrecords import show_all_students

def menu_loop():
    
    while True:
        print("=== Student Management Menu ===")
        print("1 - Student Registration")
        print("2 - Student Search (by qualification)")
        print("3 - All Student Records")
        print("4 - Exit")
        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            register_student()
        elif choice == "2":
            search_by_qualification()
        elif choice == "3":
            show_all_students()
        elif choice == "4":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.\n")