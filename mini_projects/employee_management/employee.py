class Employee:
    def __init__(
        self,
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
    ):
        self.emp_id = emp_id
        self.name = name
        self.birth_year = birth_year
        self.phone = phone
        self.email = email
        self.address = address
        self.department = department
        self.position = position
        self.gender = gender
        self.start_date = start_date
        self.base_salary = base_salary

    def display_info(self):
        print(f"""
Mã nhân viên   : {self.emp_id}
Họ tên         : {self.name}
Năm sinh       : {self.birth_year}
Số điện thoại  : {self.phone}
Email          : {self.email}
Địa chỉ        : {self.address}
Phòng ban      : {self.department}
Chức vụ        : {self.position}
Giới tính      : {self.gender}
Ngày vào làm   : {self.start_date}
Lương cơ bản   : {self.base_salary}
""")
        
    def to_dict(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "birth_year": self.birth_year,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
            "department": self.department,
            "position": self.position,
            "gender": self.gender,
            "start_date": self.start_date,
            "base_salary": self.base_salary
        }

    @staticmethod
    def from_dict(data):
        return Employee(
            data["emp_id"],
            data["name"],
            data["birth_year"],
            data["phone"],
            data["email"],
            data["address"],
            data["department"],
            data["position"],
            data["gender"],
            data["start_date"],
            data["base_salary"]
        )