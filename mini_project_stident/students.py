def input_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("Du lieu khong duoc de trong. Vui long nhap lai.")
        else:
            return value


def input_positive_int(prompt):
    while True:
        value = input(prompt).strip()
        if not value.isdigit():
            print("Vui long nhap mot so nguyen duong.")
            continue

        value = int(value)
        if value <= 0:
            print("Gia tri phai lon hon 0.")
        else:
            return value


def input_gpa(prompt):
    while True:
        value = input(prompt).strip()
        try:
            value = float(value)
            if 0.0 <= value <= 4.0:
                return value
            else:
                print("GPA phai nam trong khoang tu 0.0 den 4.0.")
        except ValueError:
            print("Vui long nhap GPA hop le (vi du: 3.2).")


def find_student_by_id(students, student_id):
    for student in students:
        if student["id"].lower() == student_id.lower():
            return student
    return None


def add_student(students):
    print("\n=== THEM SINH VIEN ===")
    student_id = input_non_empty("Nhap ma sinh vien: ")

    if find_student_by_id(students, student_id) is not None:
        print("Ma sinh vien da ton tai. Khong duoc trung ma.")
        return

    name = input_non_empty("Nhap ho ten: ")
    age = input_positive_int("Nhap tuoi: ")
    major = input_non_empty("Nhap nganh hoc: ")
    gpa = input_gpa("Nhap GPA (0.0 - 4.0): ")
    gender = input_non_empty("Nhap gioi tinh: ")
    class_name = input_non_empty("Nhap lop: ")
    year = input_positive_int("Nhap nam hoc: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "major": major,
        "gpa": gpa,
        "gender": gender,
        "class": class_name,
        "year": year
    }

    students.append(student)
    print("Them sinh vien thanh cong.")


def display_students(students):
    print("\n=== DANH SACH SINH VIEN ===")
    if len(students) == 0:
        print("Danh sach sinh vien dang rong.")
        return

    print(f"{'ID':<10} {'Ho ten':<25} {'Tuoi':<6} {'Nganh':<15} {'GPA':<6} {'Gioi tinh':<10} {'Lop':<10} {'Nam hoc':<8}")
    print("-" * 100)

    for student in students:
        print(f"{student['id']:<10} "
              f"{student['name']:<25} "
              f"{student['age']:<6} "
              f"{student['major']:<15} "
              f"{student['gpa']:<6.2f} "
              f"{student['gender']:<10} "
              f"{student['class']:<10} "
              f"{student['year']:<8}")


def search_student_by_id(students):
    print("\n=== TIM SINH VIEN THEO MA ===")
    if len(students) == 0:
        print("Danh sach sinh vien dang rong.")
        return

    student_id = input_non_empty("Nhap ma sinh vien can tim: ")
    student = find_student_by_id(students, student_id)

    if student is None:
        print("Khong tim thay sinh vien voi ma nay.")
    else:
        print("Thong tin sinh vien tim thay:")
        print(student)


def search_student_by_name(students):
    print("\n=== TIM SINH VIEN THEO TEN ===")
    if len(students) == 0:
        print("Danh sach sinh vien dang rong.")
        return

    keyword = input_non_empty("Nhap ten can tim: ").lower()
    results = []

    for student in students:
        if keyword in student["name"].lower():
            results.append(student)

    if len(results) == 0:
        print("Khong tim thay sinh vien nao phu hop.")
    else:
        print(f"Tim thay {len(results)} sinh vien:")
        print(f"{'ID':<10} {'Ho ten':<25} {'Tuoi':<6} {'Nganh':<15} {'GPA':<6} {'Gioi tinh':<10} {'Lop':<10} {'Nam hoc':<8}")
        print("-" * 100)
        for student in results:
            print(f"{student['id']:<10} "
                  f"{student['name']:<25} "
                  f"{student['age']:<6} "
                  f"{student['major']:<15} "
                  f"{student['gpa']:<6.2f} "
                  f"{student['gender']:<10} "
                  f"{student['class']:<10} "
                  f"{student['year']:<8}")


def update_student(students):
    print("\n=== CAP NHAT SINH VIEN ===")
    if len(students) == 0:
        print("Danh sach sinh vien dang rong.")
        return

    student_id = input_non_empty("Nhap ma sinh vien can cap nhat: ")
    student = find_student_by_id(students, student_id)

    if student is None:
        print("Khong tim thay sinh vien voi ma nay.")
        return

    print("De trong neu muon giu nguyen thong tin cu.")

    new_name = input("Nhap ho ten moi: ").strip()
    if new_name != "":
        student["name"] = new_name

    new_age = input("Nhap tuoi moi: ").strip()
    if new_age != "":
        if new_age.isdigit() and int(new_age) > 0:
            student["age"] = int(new_age)
        else:
            print("Tuoi khong hop le. Giu nguyen gia tri cu.")

    new_major = input("Nhap nganh hoc moi: ").strip()
    if new_major != "":
        student["major"] = new_major

    new_gpa = input("Nhap GPA moi (0.0 - 4.0): ").strip()
    if new_gpa != "":
        try:
            new_gpa = float(new_gpa)
            if 0.0 <= new_gpa <= 4.0:
                student["gpa"] = new_gpa
            else:
                print("GPA khong hop le. Giu nguyen gia tri cu.")
        except ValueError:
            print("GPA khong hop le. Giu nguyen gia tri cu.")

    new_gender = input("Nhap gioi tinh moi: ").strip()
    if new_gender != "":
        student["gender"] = new_gender

    new_class = input("Nhap lop moi: ").strip()
    if new_class != "":
        student["class"] = new_class

    new_year = input("Nhap nam hoc moi: ").strip()
    if new_year != "":
        if new_year.isdigit() and int(new_year) > 0:
            student["year"] = int(new_year)
        else:
            print("Nam hoc khong hop le. Giu nguyen gia tri cu.")

    print("Cap nhat sinh vien thanh cong.")


def delete_student(students):
    print("\n=== XOA SINH VIEN ===")
    if len(students) == 0:
        print("Danh sach sinh vien dang rong.")
        return

    student_id = input_non_empty("Nhap ma sinh vien can xoa: ")
    student = find_student_by_id(students, student_id)

    if student is None:
        print("Khong tim thay sinh vien voi ma nay.")
        return

    students.remove(student)
    print("Xoa sinh vien thanh cong.")


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


def show_menu():
    print("\n" + "=" * 40)
    print("   CHUONG TRINH QUAN LY SINH VIEN")
    print("=" * 40)
    print("1. Them sinh vien")
    print("2. Hien thi toan bo sinh vien")
    print("3. Tim sinh vien theo ma")
    print("4. Tim sinh vien theo ten")
    print("5. Cap nhat sinh vien")
    print("6. Xoa sinh vien")
    print("7. Sap xep GPA tang dan")
    print("8. Sap xep GPA giam dan")
    print("9. Sap xep ten A-Z")
    print("0. Thoat")
    print("=" * 40)


def main():
    students = []

    while True:
        show_menu()
        choice = input("Nhap lua chon cua ban: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            search_student_by_id(students)
        elif choice == "4":
            search_student_by_name(students)
        elif choice == "5":
            update_student(students)
        elif choice == "6":
            delete_student(students)
        elif choice == "7":
            sort_by_gpa_ascending(students)
        elif choice == "8":
            sort_by_gpa_descending(students)
        elif choice == "9":
            sort_by_name_a_to_z(students)
        elif choice == "0":
            print("Da thoat chuong trinh.")
            break
        else:
            print("Lua chon khong hop le. Vui long nhap lai.")


main()