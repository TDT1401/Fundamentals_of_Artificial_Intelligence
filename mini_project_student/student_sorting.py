from student_operations import display_students


def sort_by_gpa_ascending(students):
    print("\n=== SAP XEP GPA TANG DAN ===")
    if len(students) == 0:
        print("Danh sach sinh vien dang rong.")
        return

    students.sort(key=lambda student: student["gpa"])
    print("Da sap xep theo GPA tang dan.")
    display_students(students)


def sort_by_gpa_descending(students):
    print("\n=== SAP XEP GPA GIAM DAN ===")
    if len(students) == 0:
        print("Danh sach sinh vien dang rong.")
        return

    students.sort(key=lambda student: student["gpa"], reverse=True)
    print("Da sap xep theo GPA giam dan.")
    display_students(students)


def sort_by_name_a_to_z(students):
    print("\n=== SAP XEP TEN A-Z ===")
    if len(students) == 0:
        print("Danh sach sinh vien dang rong.")
        return

    students.sort(key=lambda student: student["name"].lower())
    print("Da sap xep theo ten A-Z.")
    display_students(students)
