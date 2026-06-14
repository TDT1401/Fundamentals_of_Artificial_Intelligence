from mini_projects.employee_management.employee_manager import EmployeeManager


def show_menu():
    print("""
========== QUẢN LÝ NHÂN VIÊN ==========
1. Thêm nhân viên
2. Hiển thị toàn bộ nhân viên
3. Tìm nhân viên theo mã
4. Tìm nhân viên theo tên
5. Cập nhật nhân viên
6. Xóa nhân viên
7. Sắp xếp theo chức vụ
8. Sắp xếp theo tên A-Z
9. Thống kê nhân viên theo phòng ban
10. Thống kê nhân viên theo chức vụ
11. Tìm nhân viên lương cao nhất
12. Tìm nhân viên lương thấp nhất
13. Lọc nhân viên nâng cao
0. Thoát
=======================================
""")


def main():
    manager = EmployeeManager()

    while True:
        show_menu()
        choice = input("Nhập lựa chọn: ")

        if choice == "1":
            manager.add_employee()

        elif choice == "2":
            manager.display_all_employees()

        elif choice == "3":
            manager.search_by_id()

        elif choice == "4":
            manager.search_by_name()

        elif choice == "5":
            manager.update_employee()

        elif choice == "6":
            manager.delete_employee()

        elif choice == "7":
            manager.sort_by_position()

        elif choice == "8":
            manager.sort_by_name()
            
        elif choice == "9":
            manager.statistics_by_department()

        elif choice == "10":
            manager.statistics_by_position()
            
        elif choice == "11":
            manager.find_highest_salary()

        elif choice == "12":
            manager.find_lowest_salary()
            
        elif choice == "13":
            manager.filter_employees()

        elif choice == "0":
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")


if __name__ == "__main__":
    main()