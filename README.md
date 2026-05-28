# Intro to AI

> Dự án học tập về các khái niệm cơ bản của AI, Machine Learning và Deep Learning.

## Mục tiêu

Repository này được dùng để học theo từng chủ đề nền tảng của AI:

- Python và xử lý dữ liệu cơ bản
- Đại số tuyến tính, giải tích và xác suất thống kê
- Machine Learning với các mô hình kinh điển
- PyTorch, tensor, neural network và training loop
- Thực hành qua notebook và các mini project Python

## Cấu trúc chính

```
intro_to_AI/
├── check.py
├── docs/
│   └── pytorch.md
├── data/
├── models/
├── calculus_for_ai/
├── linear_algebra/
├── probability_and_statistics/
├── dataset_analysis/
├── machine_learning/
├── pytorch/
├── employee_management/
└── mini_project_student/
```

### Các phần nổi bật

- `calculus_for_ai/`: đạo hàm, gradient, partial derivative
- `linear_algebra/`: vector, matrix, norm, rank, eigenvalues/eigenvectors
- `probability_and_statistics/`: phân phối, xác suất, thống kê cơ bản
- `dataset_analysis/`: phân tích dữ liệu bằng notebook
- `machine_learning/`: logistic regression, decision tree, KNN, naive bayes, random forest
- `pytorch/`: tensor, training, FashionMNIST và các ví dụ PyTorch
- `employee_management/`: mini app quản lý nhân viên chạy bằng console
- `mini_project_student/`: mini app quản lý sinh viên chạy bằng console

## Bắt đầu nhanh

### 1. Tạo và kích hoạt môi trường ảo

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Cài thư viện cần thiết

```bash
pip install torch torchvision torchaudio
pip install jupyter numpy pandas matplotlib seaborn scikit-learn
```

Nếu bạn dùng GPU, hãy cài PyTorch đúng phiên bản CUDA theo hướng dẫn trên trang chủ PyTorch.

### 3. Kiểm tra PyTorch và CUDA

```bash
python check.py
```

Script này sẽ in ra phiên bản PyTorch, trạng thái CUDA và thông tin GPU nếu máy có hỗ trợ.

### 4. Mở notebook

```bash
jupyter notebook
```

Sau đó mở các notebook theo chủ đề bạn muốn học, ví dụ:

- `pytorch/fashionMNISTImageClassifier.ipynb`
- `machine_learning/machine_learning_algorithms/logistic_regression.ipynb`
- `linear_algebra/vector.ipynb`
- `calculus_for_ai/derivative.ipynb`

### 5. Chạy các mini project Python

Các app console trong repo dùng import nội bộ theo thư mục, vì vậy nên chạy ngay trong folder của từng project:

```bash
cd employee_management
python main.py
```

```bash
cd mini_project_student
python main.py
```

## Dữ liệu và model

- `data/` chứa các bộ dữ liệu mẫu như Titanic, Diabetes, FashionMNIST, email spam, employees, students
- `models/` chứa model đã train sẵn, hiện có `model.pth` và các file model khác tùy notebook

## Tài liệu tham khảo

- `docs/pytorch.md`: hướng dẫn PyTorch tiếng Việt
- [PyTorch Docs](https://pytorch.org/docs/)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)

## Ghi chú

- Đây là project học tập, ưu tiên rõ ràng và dễ thử nghiệm hơn là tối ưu production
- Bạn có thể thay đổi epochs, learning rate, batch size và kiến trúc model để quan sát kết quả
- Nên chọn đúng Python interpreter của `.venv` trong VS Code để notebook và script chạy nhất quán
