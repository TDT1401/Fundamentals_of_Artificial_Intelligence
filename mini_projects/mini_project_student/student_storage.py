import json
import os

# Tính toán đường dẫn file từ folder hiện tại
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
FILE_NAME = os.path.join(PROJECT_ROOT, "data", "students", "students.json")

def ensure_data_folder_exists():
    """Tạo folder nếu chưa tồn tại"""
    folder = os.path.dirname(FILE_NAME)
    if not os.path.exists(folder):
        os.makedirs(folder)


def load_students_from_file():
    """Đọc danh sách sinh viên từ file JSON"""
    ensure_data_folder_exists()
    
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError:
        print("File du lieu bi loi JSON. Tao danh sach rong.")
        return []
    except Exception as e:
        print("Co loi khi doc file:", e)
        return []


def save_students_to_file(students):
    """Lưu danh sách sinh viên vào file JSON"""
    ensure_data_folder_exists()
    
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(students, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print("Co loi khi ghi file:", e)
