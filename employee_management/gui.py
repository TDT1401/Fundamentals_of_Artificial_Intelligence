import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
import csv
from openpyxl import Workbook

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
FILE_NAME = os.path.join(PROJECT_ROOT, "data", "employees", "employees.json")


class EmployeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý nhân viên")
        self.root.geometry("900x500")
        
        self.data_file = FILE_NAME
        self.employees = []

        self.create_menu()
        self.create_form()
        self.create_table()
        self.create_buttons()
        
        self.load_from_json()
        self.refresh_table()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Menu Tìm kiếm
        search_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tìm kiếm", menu=search_menu)
        search_menu.add_command(label="Tìm theo mã", command=self.search_by_id)
        search_menu.add_command(label="Tìm theo tên", command=self.search_by_name)
        search_menu.add_separator()
        search_menu.add_command(label="Tìm kiếm nâng cao", command=self.advanced_search)

        # Menu Thống kê
        stats_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Thống kê", menu=stats_menu)
        stats_menu.add_command(label="Thống kê theo phòng ban", command=self.statistics_by_department)
        stats_menu.add_command(label="Thống kê theo chức vụ", command=self.statistics_by_position)
        stats_menu.add_separator()
        stats_menu.add_command(label="Lương cao nhất", command=self.find_highest_salary)
        stats_menu.add_command(label="Lương thấp nhất", command=self.find_lowest_salary)

        # Menu Xuất file
        export_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Xuất file", menu=export_menu)
        export_menu.add_command(label="Xuất CSV", command=self.export_all_to_csv)
        export_menu.add_command(label="Xuất Excel", command=self.export_all_to_excel)

    def create_form(self):
        frame = tk.LabelFrame(self.root, text="Thông tin nhân viên")
        frame.pack(fill="x", padx=10, pady=10)

        self.entries = {}

        fields = [
            ("Mã NV", "emp_id"),
            ("Tên", "name"),
            ("Năm sinh", "birth_year"),
            ("Giới tính", "gender"),
            ("SĐT", "phone"),
            ("Email", "email"),
            ("Địa chỉ", "address"),
            ("Phòng ban", "department"),
            ("Chức vụ", "position"),
            ("Lương cơ bản", "base_salary"),
            ("Ngày vào làm", "start_date"),
        ]

        for index, (label_text, field_name) in enumerate(fields):
            row = index // 2
            col = (index % 2) * 2

            tk.Label(frame, text=label_text).grid(row=row, column=col, padx=5, pady=5, sticky="w")

            entry = tk.Entry(frame, width=25)
            entry.grid(row=row, column=col + 1, padx=5, pady=5)

            self.entries[field_name] = entry

    def create_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack(fill="x", padx=10, pady=5)

        tk.Button(frame, text="Thêm", width=12, command=self.add_employee).pack(side="left", padx=5)
        tk.Button(frame, text="Sửa", width=12, command=self.update_employee).pack(side="left", padx=5)
        tk.Button(frame, text="Xóa", width=12, command=self.delete_employee).pack(side="left", padx=5)
        tk.Button(frame, text="Làm mới", width=12, command=self.clear_form).pack(side="left", padx=5)

    def create_table(self):
        columns = (
            "emp_id",
            "name",
            "birth_year",
            "gender",
            "phone",
            "email",
            "address",
            "department",
            "position",
            "base_salary",
            "start_date",
        )

        self.table = ttk.Treeview(self.root, columns=columns, show="headings")

        headings = {
            "emp_id": "Mã NV",
            "name": "Tên",
            "birth_year": "Năm sinh",
            "gender": "Giới tính",
            "phone": "SĐT",
            "email": "Email",
            "address": "Địa chỉ",
            "department": "Phòng ban",
            "position": "Chức vụ",
            "base_salary": "Lương cơ bản",
            "start_date": "Ngày vào làm",
        }

        for col in columns:
            self.table.heading(col, text=headings[col])
            self.table.column(col, width=120)

        self.table.pack(fill="both", expand=True, padx=10, pady=10)
        self.table.bind("<<TreeviewSelect>>", self.on_select_employee)

    def add_employee(self):
        employee = {}

        for field_name, entry in self.entries.items():
            employee[field_name] = entry.get().strip()

        if not employee["emp_id"] or not employee["name"] or not employee["base_salary"]:
            messagebox.showwarning("Lỗi", "Vui lòng nhập Mã NV, Tên và Lương")
            return

        for emp in self.employees:
            if emp["emp_id"] == employee["emp_id"]:
                messagebox.showwarning("Lỗi", "Mã nhân viên đã tồn tại")
                return

        self.employees.append(employee)
        self.save_to_json()
        self.refresh_table()
        self.clear_form()

        messagebox.showinfo("Thành công", "Đã thêm nhân viên")
        
    def clear_form(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

        self.table.selection_remove(self.table.selection())


    def on_select_employee(self, event):
        selected_item = self.table.selection()

        if not selected_item:
            return

        values = self.table.item(selected_item[0], "values")

        field_names = [
            "emp_id",
            "name",
            "birth_year",
            "gender",
            "phone",
            "email",
            "address",
            "department",
            "position",
            "base_salary",
            "start_date",
        ]

        for field_name, value in zip(field_names, values):
            self.entries[field_name].delete(0, tk.END)
            self.entries[field_name].insert(0, value)


    def update_employee(self):
        selected_item = self.table.selection()

        if not selected_item:
            messagebox.showwarning("Lỗi", "Vui lòng chọn nhân viên cần sửa")
            return

        old_values = self.table.item(selected_item[0], "values")
        old_id = old_values[0]

        updated_employee = {}

        for field_name, entry in self.entries.items():
            updated_employee[field_name] = entry.get().strip()

        if not updated_employee["emp_id"] or not updated_employee["name"] or not updated_employee["base_salary"]:
            messagebox.showwarning("Lỗi", "Vui lòng nhập Mã NV, Tên và Lương")
            return

        for emp in self.employees:
            if emp["emp_id"] == updated_employee["emp_id"] and emp["emp_id"] != old_id:
                messagebox.showwarning("Lỗi", "Mã nhân viên đã tồn tại")
                return

        for index, emp in enumerate(self.employees):
            if emp["emp_id"] == old_id:
                self.employees[index] = updated_employee
                break

        self.save_to_json()
        self.refresh_table()
        self.clear_form()

        messagebox.showinfo("Thành công", "Đã cập nhật nhân viên")


    def delete_employee(self):
        selected_item = self.table.selection()

        if not selected_item:
            messagebox.showwarning("Lỗi", "Vui lòng chọn nhân viên cần xóa")
            return

        values = self.table.item(selected_item[0], "values")
        employee_id = values[0]

        confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa nhân viên này không?")

        if confirm:
            self.employees = [
                emp for emp in self.employees
                if emp["emp_id"] != employee_id
            ]

            self.save_to_json()
            self.refresh_table()
            self.clear_form()

            messagebox.showinfo("Thành công", "Đã xóa nhân viên")

    def search_by_id(self):
        emp_id = simpledialog.askstring("Tìm kiếm", "Nhập mã nhân viên cần tìm:")
        if emp_id is None:
            return
        
        for emp in self.employees:
            if emp["emp_id"] == emp_id:
                self.clear_form()
                for field_name, entry in self.entries.items():
                    entry.delete(0, tk.END)
                    entry.insert(0, emp.get(field_name, ""))
                messagebox.showinfo("Tìm kiếm", "Tìm thấy nhân viên!")
                return
        
        messagebox.showwarning("Tìm kiếm", "Không tìm thấy nhân viên có mã này.")

    def search_by_name(self):
        name = simpledialog.askstring("Tìm kiếm", "Nhập tên nhân viên cần tìm:")
        if name is None:
            return
        
        results = [emp for emp in self.employees if name.lower() in emp["name"].lower()]
        
        if not results:
            messagebox.showwarning("Tìm kiếm", "Không tìm thấy nhân viên phù hợp.")
            return
        
        # Hiển thị kết quả tìm kiếm
        self.show_search_results(results)

    def show_search_results(self, results, show_export=False):
        result_window = tk.Toplevel(self.root)
        result_window.title("Kết quả tìm kiếm")
        result_window.geometry("900x400")
        
        columns = ("emp_id", "name", "birth_year", "gender", "phone", "email", "address", "department", "position", "base_salary", "start_date")
        headings = {
            "emp_id": "Mã NV",
            "name": "Tên",
            "birth_year": "Năm sinh",
            "gender": "Giới tính",
            "phone": "SĐT",
            "email": "Email",
            "address": "Địa chỉ",
            "department": "Phòng ban",
            "position": "Chức vụ",
            "base_salary": "Lương cơ bản",
            "start_date": "Ngày vào làm",
        }
        
        # Nút xuất file nếu cần
        if show_export:
            btn_frame = tk.Frame(result_window)
            btn_frame.pack(fill="x", padx=10, pady=5)
            tk.Button(btn_frame, text="Xuất CSV", command=lambda: self.export_results_to_csv(results)).pack(side="left", padx=5)
            tk.Button(btn_frame, text="Xuất Excel", command=lambda: self.export_results_to_excel(results)).pack(side="left", padx=5)
        
        table = ttk.Treeview(result_window, columns=columns, show="headings")
        for col in columns:
            table.heading(col, text=headings[col])
            table.column(col, width=100)
        
        for emp in results:
            table.insert("", "end", values=(
                emp["emp_id"], emp["name"], emp["birth_year"], emp["gender"],
                emp["phone"], emp["email"], emp["address"], emp["department"],
                emp["position"], emp["base_salary"], emp["start_date"]
            ))
        
        table.pack(fill="both", expand=True, padx=10, pady=10)

    def statistics_by_department(self):
        stats = {}
        for emp in self.employees:
            dept = emp["department"]
            stats[dept] = stats.get(dept, 0) + 1
        
        self.show_statistics("Thống kê theo phòng ban", stats)

    def statistics_by_position(self):
        stats = {}
        for emp in self.employees:
            pos = emp["position"]
            stats[pos] = stats.get(pos, 0) + 1
        
        self.show_statistics("Thống kê theo chức vụ", stats)

    def show_statistics(self, title, stats):
        stat_window = tk.Toplevel(self.root)
        stat_window.title(title)
        stat_window.geometry("400x300")
        
        frame = tk.Frame(stat_window)
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        text = tk.Text(frame, height=15, width=40)
        text.pack(side="left", fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(frame, command=text.yview)
        scrollbar.pack(side="right", fill="y")
        text.config(yscrollcommand=scrollbar.set)
        
        for key, value in stats.items():
            text.insert(tk.END, f"{key}: {value}\n")
        
        text.config(state=tk.DISABLED)

    def find_highest_salary(self):
        if not self.employees:
            messagebox.showwarning("Lỗi", "Danh sách nhân viên đang rỗng.")
            return
        
        max_salary = max(emp["base_salary"] for emp in self.employees)
        results = [emp for emp in self.employees if emp["base_salary"] == max_salary]
        
        messagebox.showinfo("Lương cao nhất", f"Lương cao nhất: {max_salary}\nSố nhân viên: {len(results)}")
        self.show_search_results(results)

    def find_lowest_salary(self):
        if not self.employees:
            messagebox.showwarning("Lỗi", "Danh sách nhân viên đang rỗng.")
            return
        
        min_salary = min(emp["base_salary"] for emp in self.employees)
        results = [emp for emp in self.employees if emp["base_salary"] == min_salary]
        
        messagebox.showinfo("Lương thấp nhất", f"Lương thấp nhất: {min_salary}\nSố nhân viên: {len(results)}")
        self.show_search_results(results)

    def advanced_search(self):
        search_window = tk.Toplevel(self.root)
        search_window.title("Tìm kiếm nâng cao")
        search_window.geometry("400x300")
        
        # Phòng ban
        tk.Label(search_window, text="Phòng ban:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        departments = sorted(set([emp.get("department", "") for emp in self.employees if emp.get("department")]) or [""])
        dept_var = tk.StringVar()
        dept_combo = ttk.Combobox(search_window, textvariable=dept_var, values=departments, width=30)
        dept_combo.grid(row=0, column=1, padx=10, pady=5)
        
        # Chức vụ
        tk.Label(search_window, text="Chức vụ:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        positions = sorted(set([emp.get("position", "") for emp in self.employees if emp.get("position")]) or [""])
        pos_var = tk.StringVar()
        pos_combo = ttk.Combobox(search_window, textvariable=pos_var, values=positions, width=30)
        pos_combo.grid(row=1, column=1, padx=10, pady=5)
        
        # Lương tối thiểu
        tk.Label(search_window, text="Lương tối thiểu:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        min_salary_entry = tk.Entry(search_window, width=33)
        min_salary_entry.grid(row=2, column=1, padx=10, pady=5)
        
        # Lương tối đa
        tk.Label(search_window, text="Lương tối đa:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        max_salary_entry = tk.Entry(search_window, width=33)
        max_salary_entry.grid(row=3, column=1, padx=10, pady=5)
        
        def perform_search():
            dept = dept_var.get().strip()
            pos = pos_var.get().strip()
            min_sal = min_salary_entry.get().strip()
            max_sal = max_salary_entry.get().strip()
            
            results = self.employees[:]
            
            if dept:
                results = [e for e in results if e.get("department") == dept]
            if pos:
                results = [e for e in results if e.get("position") == pos]
            
            try:
                if min_sal:
                    min_val = float(min_sal)
                    results = [e for e in results if float(e.get("base_salary", 0)) >= min_val]
                if max_sal:
                    max_val = float(max_sal)
                    results = [e for e in results if float(e.get("base_salary", 0)) <= max_val]
            except ValueError:
                messagebox.showerror("Lỗi", "Lương phải là số")
                return
            
            if not results:
                messagebox.showwarning("Tìm kiếm", "Không tìm thấy kết quả phù hợp.")
                return
            
            messagebox.showinfo("Tìm kiếm", f"Tìm thấy {len(results)} kết quả")
            self.show_search_results(results, show_export=True)
            search_window.destroy()
        
        tk.Button(search_window, text="Tìm kiếm", width=20, command=perform_search).grid(row=4, column=0, columnspan=2, pady=20)

    def export_results_to_csv(self, results):
        if not results:
            messagebox.showwarning("Lỗi", "Không có dữ liệu để xuất.")
            return
        
        exports_dir = os.path.join(PROJECT_ROOT, "exports")
        os.makedirs(exports_dir, exist_ok=True)
        file_path = os.path.join(exports_dir, "search_results.csv")
        
        try:
            with open(file_path, "w", newline="", encoding="utf-8-sig") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "Mã nhân viên", "Họ tên", "Năm sinh", "Giới tính", "Số điện thoại",
                    "Email", "Địa chỉ", "Phòng ban", "Chức vụ", "Lương cơ bản", "Ngày vào làm"
                ])
                for emp in results:
                    writer.writerow([
                        emp["emp_id"], emp["name"], emp["birth_year"], emp["gender"],
                        emp["phone"], emp["email"], emp["address"], emp["department"],
                        emp["position"], emp["base_salary"], emp["start_date"]
                    ])
            messagebox.showinfo("Thành công", f"Đã xuất CSV: {file_path}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi xuất file: {str(e)}")

    def export_results_to_excel(self, results):
        if not results:
            messagebox.showwarning("Lỗi", "Không có dữ liệu để xuất.")
            return
        
        exports_dir = os.path.join(PROJECT_ROOT, "exports")
        os.makedirs(exports_dir, exist_ok=True)
        file_path = os.path.join(exports_dir, "search_results.xlsx")
        
        try:
            workbook = Workbook()
            sheet = workbook.active
            sheet.title = "Search Results"
            
            sheet.append([
                "Mã nhân viên", "Họ tên", "Năm sinh", "Giới tính", "Số điện thoại",
                "Email", "Địa chỉ", "Phòng ban", "Chức vụ", "Lương cơ bản", "Ngày vào làm"
            ])
            
            for emp in results:
                sheet.append([
                    emp["emp_id"], emp["name"], emp["birth_year"], emp["gender"],
                    emp["phone"], emp["email"], emp["address"], emp["department"],
                    emp["position"], emp["base_salary"], emp["start_date"]
                ])
            
            workbook.save(file_path)
            messagebox.showinfo("Thành công", f"Đã xuất Excel: {file_path}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi xuất file: {str(e)}")

    def export_all_to_csv(self):
        if not self.employees:
            messagebox.showwarning("Lỗi", "Danh sách nhân viên đang rỗng.")
            return
        
        exports_dir = os.path.join(PROJECT_ROOT, "exports")
        os.makedirs(exports_dir, exist_ok=True)
        file_path = os.path.join(exports_dir, "employees.csv")
        
        try:
            with open(file_path, "w", newline="", encoding="utf-8-sig") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "Mã nhân viên", "Họ tên", "Năm sinh", "Giới tính", "Số điện thoại",
                    "Email", "Địa chỉ", "Phòng ban", "Chức vụ", "Lương cơ bản", "Ngày vào làm"
                ])
                for emp in self.employees:
                    writer.writerow([
                        emp["emp_id"], emp["name"], emp["birth_year"], emp["gender"],
                        emp["phone"], emp["email"], emp["address"], emp["department"],
                        emp["position"], emp["base_salary"], emp["start_date"]
                    ])
            messagebox.showinfo("Thành công", f"Đã xuất CSV: {file_path}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi xuất file: {str(e)}")

    def export_all_to_excel(self):
        if not self.employees:
            messagebox.showwarning("Lỗi", "Danh sách nhân viên đang rỗng.")
            return
        
        exports_dir = os.path.join(PROJECT_ROOT, "exports")
        os.makedirs(exports_dir, exist_ok=True)
        file_path = os.path.join(exports_dir, "employees.xlsx")
        
        try:
            workbook = Workbook()
            sheet = workbook.active
            sheet.title = "Employees"
            
            sheet.append([
                "Mã nhân viên", "Họ tên", "Năm sinh", "Giới tính", "Số điện thoại",
                "Email", "Địa chỉ", "Phòng ban", "Chức vụ", "Lương cơ bản", "Ngày vào làm"
            ])
            
            for emp in self.employees:
                sheet.append([
                    emp["emp_id"], emp["name"], emp["birth_year"], emp["gender"],
                    emp["phone"], emp["email"], emp["address"], emp["department"],
                    emp["position"], emp["base_salary"], emp["start_date"]
                ])
            
            workbook.save(file_path)
            messagebox.showinfo("Thành công", f"Đã xuất Excel: {file_path}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi xuất file: {str(e)}")
            
    def load_from_json(self):
        if not os.path.exists(self.data_file):
            self.employees = []
            return

        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                self.employees = json.load(file)
        except json.JSONDecodeError:
            self.employees = []
            
    def save_to_json(self):
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump(self.employees, file, ensure_ascii=False, indent=4)
            
    def refresh_table(self):
        for item in self.table.get_children():
            self.table.delete(item)

        for employee in self.employees:
            self.table.insert(
                "",
                "end",
                values=(
                    employee["emp_id"],
                    employee["name"],
                    employee["birth_year"],
                    employee["gender"],
                    employee["phone"],
                    employee["email"],
                    employee["address"],
                    employee["department"],
                    employee["position"],
                    employee["base_salary"],
                    employee["start_date"],
                )
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeApp(root)
    root.mainloop()