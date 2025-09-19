import os
import json

def _get_data_file_path():
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "database"))
    os.makedirs(base, exist_ok=True)
    return os.path.join(base, "studentdata.json")

def _read_students():
    path = _get_data_file_path()
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def _write_students(students):
    path = _get_data_file_path()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=2)

def _generate_next_id(students):
    if not students:
        return 1
    try:
        max_id = max(int(s.get("id", 0)) for s in students)
        return max_id + 1
    except Exception:
        return len(students) + 1

def register_student():
    """Interactively create a student record and save to studentdata.json"""
    print("\n--- Student Registration ---")
    name = input("Enter student's name: ").strip()
    address = input("Enter student's address: ").strip()
    email = input("Enter student's email: ").strip()

    
    qualifications = []
    while True:
        resp = input("Do you want to add a qualification? (yes / no): ").strip().lower()
        if resp in ("no", "n"):
            
            break
        elif resp in ("yes", "y"):
            qual = input("  Qualification (e.g. B.Sc, M.Tech): ").strip()
            year = input("  Year (e.g. 2022): ").strip()
            qualifications.append({"qualification": qual, "year": year})
            
        else:
            print("Please answer 'yes' or 'no'.")

    students = _read_students()
    new_id = _generate_next_id(students)
    student = {
        "id": new_id,
        "name": name,
        "address": address,
        "email": email,
        "qualifications": qualifications
    }
    students.append(student)
    _write_students(students)
    print(f"\nStudent registered successfully with ID: {new_id}\n")
