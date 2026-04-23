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
