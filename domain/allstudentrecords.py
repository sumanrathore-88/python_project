import os
import json

def _get_data_file_path():
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "database"))
    return os.path.join(base, "studentdata.json")

def _read_students():
    path = _get_data_file_path()
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def show_all_students():
    """Display all student records."""
    print("\n--- All Student Records ---")
    students = _read_students()
    if not students:
        print("No student records found.\n")
        return

    for s in students:
        print(f"ID: {s.get('id')}")
        print(f"Name: {s.get('name')}")
        print(f"Address: {s.get('address')}")
        print(f"Email: {s.get('email')}")
        print("Qualifications:")
        for q in s.get("qualifications", []):
            print(f"  - {q.get('qualification')} ({q.get('year')})")
        print("-" * 40)
    print()