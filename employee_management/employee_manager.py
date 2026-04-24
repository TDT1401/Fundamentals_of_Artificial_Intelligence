from employee import Employee
from validation import input_not_empty, input_birth_year, input_salary
import json
import os
import csv
from openpyxl import Workbook

# Tính toán đường dẫn file từ folder hiện tại
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
FILE_NAME = os.path.join(PROJECT_ROOT, "data", "employees", "employees.json")

class EmployeeManager:
    def __init__(self):
        self.file_name = FILE_NAME
        self.employees = []
        self.load_data()

    def is_empty(self):
        return len(self.employees) == 0

    def find_employee_by_id(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                return employee

        return None

    def add_employee(self):
        print("\n=== THÊM NHÂN VIÊN ===")

        while True:
            emp_id = input_not_empty("Nhập mã nhân viên: ")

            if self.find_employee_by_id(emp_id) is None:
                break

            print("Mã nhân viên đã tồn tại. Vui lòng nhập mã khác.")

        name = input_not_empty("Nhập họ tên: ")
        birth_year = input_birth_year("Nhập năm sinh: ")
        phone = input_not_empty("Nhập số điện thoại: ")
        email = input_not_empty("Nhập email: ")
        address = input_not_empty("Nhập địa chỉ: ")
        department = input_not_empty("Nhập phòng ban: ")
        position = input_not_empty("Nhập chức vụ: ")
        gender = input_not_empty("Nhập giới tính: ")
        start_date = input_not_empty("Nhập ngày vào làm: ")
        base_salary = input_salary("Nhập lương cơ bản: ")

        employee = Employee(
            emp_id,
            name,
            birth_year,
            phone,
            email,
            address,
            department,
            position,
            gender,
            start_date,
            base_salary
        )

        self.employees.append(employee)
        self.save_data()
        print("Thêm nhân viên thành công.")

    def display_all_employees(self):
        print("\n=== DANH SÁCH NHÂN VIÊN ===")

        if self.is_empty():
            print("Danh sách nhân viên đang rỗng.")
            return

        page_size = 5
        total_employees = len(self.employees)
        total_pages = (total_employees + page_size - 1) // page_size

        while True:
            try:
                page = int(input(f"Nhập trang muốn xem từ 1 đến {total_pages}: "))

                if page < 1 or page > total_pages:
                    print("Số trang không hợp lệ.")
                    continue

                start_index = (page - 1) * page_size
                end_index = start_index + page_size

                print(f"\n=== TRANG {page}/{total_pages} ===")
                print(f"Hiển thị nhân viên {start_index + 1} đến {min(end_index, total_employees)} trong tổng {total_employees} nhân viên")

                for employee in self.employees[start_index:end_index]:
                    employee.display_info()

                break

            except ValueError:
                print("Vui lòng nhập số nguyên.")

    def search_by_id(self):
        print("\n=== TÌM NHÂN VIÊN THEO MÃ ===")

        if self.is_empty():
            print("Danh sách nhân viên đang rỗng.")
            return

        emp_id = input_not_empty("Nhập mã nhân viên cần tìm: ")
        employee = self.find_employee_by_id(emp_id)

        if employee is None:
            print("Không tìm thấy nhân viên có mã này.")
        else:
            employee.display_info()

    def search_by_name(self):
        print("\n=== TÌM NHÂN VIÊN THEO TÊN ===")

        if self.is_empty():
            print("Danh sách nhân viên đang rỗng.")
            return

        keyword = input_not_empty("Nhập tên cần tìm: ").lower()

        results = []

        for employee in self.employees:
            if keyword in employee.name.lower():
                results.append(employee)

        if len(results) == 0:
            print("Không tìm thấy nhân viên phù hợp.")
        else:
            for employee in results:
                employee.display_info()

    def update_employee(self):
        print("\n=== CẬP NHẬT NHÂN VIÊN ===")

        if self.is_empty():
            print("Danh sách nhân viên đang rỗng.")
            return

        emp_id = input_not_empty("Nhập mã nhân viên cần cập nhật: ")
        employee = self.find_employee_by_id(emp_id)

        if employee is None:
            print("Không tìm thấy nhân viên có mã này.")
            return

        print("Nhập thông tin mới:")

        employee.name = input_not_empty("Nhập họ tên: ")
        employee.birth_year = input_birth_year("Nhập năm sinh: ")
        employee.phone = input_not_empty("Nhập số điện thoại: ")
        employee.email = input_not_empty("Nhập email: ")
        employee.address = input_not_empty("Nhập địa chỉ: ")
        employee.department = input_not_empty("Nhập phòng ban: ")
        employee.position = input_not_empty("Nhập chức vụ: ")
        employee.gender = input_not_empty("Nhập giới tính: ")
        employee.start_date = input_not_empty("Nhập ngày vào làm: ")
        employee.base_salary = input_salary("Nhập lương cơ bản: ")
        
        self.save_data()

        print("Cập nhật nhân viên thành công.")

    def delete_employee(self):
        print("\n=== XÓA NHÂN VIÊN ===")

        if self.is_empty():
            print("Danh sách nhân viên đang rỗng.")
            return

        emp_id = input_not_empty("Nhập mã nhân viên cần xóa: ")
        employee = self.find_employee_by_id(emp_id)

        if employee is None:
            print("Không tìm thấy nhân viên có mã này.")
            return

        self.employees.remove(employee)
        self.save_data()
        print("Xóa nhân viên thành công.")

    def sort_by_position(self):
        print("\n=== SẮP XẾP THEO CHỨC VỤ ===")

        if self.is_empty():
            print("Danh sách nhân viên đang rỗng.")
            return

        self.employees.sort(key=lambda employee: employee.position.lower())
        print("Sắp xếp theo chức vụ thành công.")
        self.display_all_employees()

    def sort_by_name(self):
        print("\n=== SẮP XẾP THEO TÊN A-Z ===")

        if self.is_empty():
            print("Danh sách nhân viên đang rỗng.")
            return

        self.employees.sort(key=lambda employee: employee.name.lower())
        print("Sắp xếp theo tên A-Z thành công.")
        self.display_all_employees()
        
    def load_data(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                data = json.load(file)

                self.employees = []

                for item in data:
                    employee = Employee.from_dict(item)
                    self.employees.append(employee)

        except FileNotFoundError:
            self.employees = []

        except json.JSONDecodeError:
            self.employees = []
            
    def save_data(self):
        data = []

        for employee in self.employees:
            data.append(employee.to_dict())

        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            
    def statistics_by_department(self):
        print("\n=== THỐNG KÊ NHÂN VIÊN THEO PHÒNG BAN ===")

        if self.is_empty():
            print("Danh sách nhân viên đang rỗng.")
            return

        statistics = {}

        for employee in self.employees:
            department = employee.department

            if department in statistics:
                statistics[department] += 1
            else:
                statistics[department] = 1

        for department, quantity in statistics.items():
            print(f"Phòng ban: {department} | Số lượng: {quantity}")


    def statistics_by_position(self):
        print("\n=== THỐNG KÊ NHÂN VIÊN THEO CHỨC VỤ ===")

        if self.is_empty():
            print("Danh sách nhân viên đang rỗng.")
            return

        statistics = {}

        for employee in self.employees:
            position = employee.position

            if position in statistics:
                statistics[position] += 1
            else:
                statistics[position] = 1

        for position, quantity in statistics.items():
            print(f"Chức vụ: {position} | Số lượng: {quantity}")

    def find_highest_salary(self):
        print("\n=== NHÂN VIÊN LƯƠNG CAO NHẤT ===")

        if self.is_empty():
            print("Danh sách nhân viên đang rỗng.")
            return

        max_salary = max(emp.base_salary for emp in self.employees)

        result = []

        for emp in self.employees:
            if emp.base_salary == max_salary:
                result.append(emp)

        print(f"Lương cao nhất: {max_salary}")

        for emp in result:
            emp.display_info()
            
    def find_lowest_salary(self):
        print("\n=== NHÂN VIÊN LƯƠNG THẤP NHẤT ===")

        if self.is_empty():
            print("Danh sách nhân viên đang rỗng.")
            return

        min_salary = min(emp.base_salary for emp in self.employees)

        result = []

        for emp in self.employees:
            if emp.base_salary == min_salary:
                result.append(emp)

        print(f"Lương thấp nhất: {min_salary}")

        for emp in result:
            emp.display_info()
            
    def filter_employees(self):
        print("\n=== LỌC NHÂN VIÊN NÂNG CAO ===")

        if self.is_empty():
            print("Danh sách nhân viên đang rỗng.")
            return

        department = input("Nhập phòng ban cần lọc, bỏ trống nếu không lọc: ").strip().lower()
        position = input("Nhập chức vụ cần lọc, bỏ trống nếu không lọc: ").strip().lower()

        try:
            min_salary_input = input("Nhập lương tối thiểu, bỏ trống nếu không lọc: ").strip()
            max_salary_input = input("Nhập lương tối đa, bỏ trống nếu không lọc: ").strip()

            min_salary = float(min_salary_input) if min_salary_input != "" else None
            max_salary = float(max_salary_input) if max_salary_input != "" else None

        except ValueError:
            print("Lương phải là số.")
            return

        results = []

        for employee in self.employees:
            match_department = True
            match_position = True
            match_min_salary = True
            match_max_salary = True

            if department != "":
                match_department = department in employee.department.lower()

            if position != "":
                match_position = position in employee.position.lower()

            if min_salary is not None:
                match_min_salary = employee.base_salary >= min_salary

            if max_salary is not None:
                match_max_salary = employee.base_salary <= max_salary

            if match_department and match_position and match_min_salary and match_max_salary:
                results.append(employee)

        if len(results) == 0:
            print("Không tìm thấy nhân viên phù hợp.")
            return

        print(f"Tìm thấy {len(results)} nhân viên phù hợp:")

        for employee in results:
            employee.display_info()
            
        self.ask_export_filtered_result(results)
            
    def export_to_csv(self, employees, file_name="filtered_employees.csv"):
        # Tạo folder exports nếu chưa tồn tại
        exports_dir = os.path.join(PROJECT_ROOT, "exports")
        os.makedirs(exports_dir, exist_ok=True)
        
        # Đường dẫn file đầy đủ
        file_path = os.path.join(exports_dir, file_name)
        
        with open(file_path, "w", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Mã nhân viên",
                "Họ tên",
                "Năm sinh",
                "Số điện thoại",
                "Email",
                "Địa chỉ",
                "Phòng ban",
                "Chức vụ",
                "Giới tính",
                "Ngày vào làm",
                "Lương cơ bản"
            ])

            for emp in employees:
                writer.writerow([
                    emp.emp_id,
                    emp.name,
                    emp.birth_year,
                    emp.phone,
                    emp.email,
                    emp.address,
                    emp.department,
                    emp.position,
                    emp.gender,
                    emp.start_date,
                    emp.base_salary
                ])

        print(f"Đã xuất dữ liệu ra file CSV: {file_path}")


    def export_to_excel(self, employees, file_name="filtered_employees.xlsx"):
        # Tạo folder exports nếu chưa tồn tại
        exports_dir = os.path.join(PROJECT_ROOT, "exports")
        os.makedirs(exports_dir, exist_ok=True)
        
        # Đường dẫn file đầy đủ
        file_path = os.path.join(exports_dir, file_name)
        
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Filtered Employees"

        sheet.append([
            "Mã nhân viên",
            "Họ tên",
            "Năm sinh",
            "Số điện thoại",
            "Email",
            "Địa chỉ",
            "Phòng ban",
            "Chức vụ",
            "Giới tính",
            "Ngày vào làm",
            "Lương cơ bản"
        ])

        for emp in employees:
            sheet.append([
                emp.emp_id,
                emp.name,
                emp.birth_year,
                emp.phone,
                emp.email,
                emp.address,
                emp.department,
                emp.position,
                emp.gender,
                emp.start_date,
                emp.base_salary
            ])

        workbook.save(file_path)

        print(f"Đã xuất dữ liệu ra file Excel: {file_path}")


    def ask_export_filtered_result(self, employees):
        while True:
            print("""
Bạn có muốn xuất kết quả lọc ra file không?
1. Xuất CSV
2. Xuất Excel
3. Không xuất
""")

            choice = input("Nhập lựa chọn: ").strip()

            if choice == "1":
                self.export_to_csv(employees)
                break

            elif choice == "2":
                self.export_to_excel(employees)
                break

            elif choice == "3":
                print("Không xuất file.")
                break

            else:
                print("Lựa chọn không hợp lệ.")