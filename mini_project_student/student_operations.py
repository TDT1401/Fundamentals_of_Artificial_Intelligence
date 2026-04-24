from input_validators import input_non_empty, input_positive_int, input_gpa
from student_storage import save_students_to_file


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
    save_students_to_file(students)
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

    save_students_to_file(students)
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
    save_students_to_file(students)
    print("Xoa sinh vien thanh cong.")
