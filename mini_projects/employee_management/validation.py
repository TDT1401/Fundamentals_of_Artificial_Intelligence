from datetime import datetime


def input_not_empty(message):
    while True:
        value = input(message).strip()

        if value != "":
            return value

        print("Dữ liệu không được để trống.")


def input_birth_year(message):
    current_year = datetime.now().year

    while True:
        try:
            year = int(input(message))

            if year > 0 and year <= current_year:
                return year

            print("Năm sinh phải lớn hơn 0 và không lớn hơn năm hiện tại.")

        except ValueError:
            print("Năm sinh phải là số nguyên.")


def input_salary(message):
    while True:
        try:
            salary = float(input(message))

            if salary >= 0:
                return salary

            print("Lương không được âm.")

        except ValueError:
            print("Lương phải là số.")