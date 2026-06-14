from mini_projects.mini_project_student.input_validators import input_non_empty

from mini_projects.mini_project_student.student_operations import (
    add_student,
    display_students,
    search_student_by_id,
    search_student_by_name,
    update_student,
    delete_student
)
from mini_projects.mini_project_student.student_sorting import (
    sort_by_gpa_ascending,
    sort_by_gpa_descending,
    sort_by_name_a_to_z
)
from mini_projects.mini_project_student.student_storage import load_students_from_file
from mini_projects.mini_project_student.ui import show_menu


def main():
    students = load_students_from_file()  # Load dữ liệu khi khởi động

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


if __name__ == "__main__":
    main()
