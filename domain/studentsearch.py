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

def search_by_qualification():
    """Ask user for a qualification string and print matching student records."""
    print("\n--- Student Search by Qualification ---")
    qual_query = input("Enter qualification to search (e.g. B.Sc, M.Tech): ").strip().lower()
    if not qual_query:
        print("No qualification entered. Returning to menu.\n")
        return

    students = _read_students()
    matches = []
    for s in students:
        for q in s.get("qualifications", []):
            if qual_query in (q.get("qualification") or "").lower():
                matches.append(s)
                break

    if not matches:
        print(f"No students found with qualification containing '{qual_query}'.\n")
        return

    print(f"\nFound {len(matches)} student(s):\n")
    for s in matches:
        print(f"ID: {s.get('id')}")
        print(f"Name: {s.get('name')}")
        print(f"Address: {s.get('address')}")
        print(f"Email: {s.get('email')}")
        print("Qualifications:")
        for q in s.get("qualifications", []):
            print(f"  - {q.get('qualification')} ({q.get('year')})")
        print("-" * 30)
    print()