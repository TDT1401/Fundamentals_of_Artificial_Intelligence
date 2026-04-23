# 📘 PyTorch Starter Guide

> Bản hướng dẫn chuẩn để sử dụng lâu dài

## Table of Contents

1. [PyTorch là gì?](#1-pytorch-là-gì)
2. [Setup chuẩn](#2-setup-chuẩn)
3. [Tensor - Cốt lõi](#3-tensor--cốt-lõi)
4. [Autograd - Tự tính Gradient](#4-autograd--tự-tính-gradient)
5. [Model cơ bản](#5-model-cơ-bản)
6. [Training Loop](#6-training-loop)
7. [GPU (CUDA)](#7-gpu-cuda)
8. [Cấu trúc Project](#8-cấu-trúc-project)
9. [Các Module quan trọng](#9-các-module-quan-trọng)
10. [Ví dụ hoàn chỉnh](#10-ví-dụ-hoàn-chỉnh)
11. [Lỗi phổ biến](#11-lỗi-phổ-biến)
12. [Checklist](#12-checklist-mỗi-project)
13. [Lộ trình 2 tuần](#13-lộ-trình-2-tuần)

---

## 1. PyTorch là gì?

PyTorch là thư viện Python dùng để:

- ✅ Xây dựng mô hình AI
- ✅ Train deep learning models
- ✅ Chạy trên CPU hoặc GPU (CUDA)

### Hiểu nhanh:

| Thư viện | Chức năng                  |
| -------- | -------------------------- |
| NumPy    | Tính toán số               |
| PyTorch  | Tính toán + Học từ dữ liệu |

---

## 2. Setup chuẩn

### Nguyên tắc

- 1 project = 1 virtual env
- Driver NVIDIA cài 1 lần cho máy
- PyTorch cài trong env

### Bước 1: Tạo môi trường

```bash
python -m venv .venv
```

### Bước 2: Activate virtual env

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/Mac:**

```bash
source .venv/bin/activate
```

**Chọn đúng Python interpreter** (nút Run trên vsCode)

- Nhấn: Ctrl + Shift + P
- Gõ: Python: Select Interpreter
- Chọn đúng env của bạn (venv / conda / poetry…)

### Bước 3: Cài PyTorch (GPU)

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

---

## 3. Tensor - Cốt lõi

Tensor là mảng multi-dimensional - cốt lõi của PyTorch.

```python
import torch

# Tạo tensor
x = torch.tensor([[1, 2], [3, 4]])
print(x.shape)   # torch.Size([2, 2])
print(x)
```

### Ghi nhớ:

- ✅ Mọi thứ trong PyTorch = tensor
- ✅ Luôn để ý **shape** của tensor
- ✅ Tensor có thể trên CPU hoặc GPU

---

## 4. Autograd - Tự tính Gradient

Autograd tự động tính đạo hàm (gradient) - đây là nền tảng của machine learning.

```python
import torch

x = torch.tensor(2.0, requires_grad=True)
y = x**2

y.backward()
print(x.grad)  # tensor(4.)
```

**Giải thích:**

- `requires_grad=True` → theo dõi gradient
- `y.backward()` → tính đạo hàm
- `x.grad` → gradient của x

---

## 5. Model cơ bản

```python
import torch.nn as nn

# Model linear: y = w*x + b
model = nn.Linear(1, 1)
```

### Các layer phổ biến:

| Layer       | Công dụng              |
| ----------- | ---------------------- |
| `nn.Linear` | Fully connected        |
| `nn.Conv2d` | Convolution (hình ảnh) |
| `nn.LSTM`   | Recurrent (chuỗi)      |
| `nn.ReLU`   | Activation             |

---

## 6. Training Loop

Training loop là quy trình lặp để train model - **quan trọng nhất**.

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Setup
model = nn.Linear(1, 1)
optimizer = optim.SGD(model.parameters(), lr=0.01)
loss_fn = nn.MSELoss()

# Training loop
for epoch in range(100):
    # 1. Forward pass
    pred = model(x)

    # 2. Tính loss
    loss = loss_fn(pred, y)

    # 3. Backward pass
    loss.backward()

    # 4. Update weights
    optimizer.step()
    optimizer.zero_grad()
```

### 4 bước chính:

| Bước     | Mục đích         |
| -------- | ---------------- |
| Forward  | Dự đoán          |
| Loss     | Tính sai số      |
| Backward | Tính gradient    |
| Update   | Cập nhật weights |

---

## 7. GPU (CUDA)

GPU giúp training nhanh gấp 10-100 lần.

```python
# Kiểm tra GPU
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Move model & data to device
model.to(device)
x = x.to(device)
y = y.to(device)

# Hoặc dùng trong training
pred = model(x.to(device))
```

> ⚠️ **Quan trọng:** Quên `.to(device)` = GPU vô dụng

---

## 8. Cấu trúc Project

```
my_project/
│
├── .venv/                 # Virtual environment
├── data/                  # Dữ liệu
│   ├── train/
│   └── test/
├── models/                # Code model
│   ├── __init__.py
│   └── net.py
├── train.py              # Script training
├── eval.py               # Script evaluate
├── requirements.txt      # Dependencies
└── README.md
```

---

## 9. Các Module quan trọng

| Module                | Chức năng                   |
| --------------------- | --------------------------- |
| `torch`               | Tensor & các hàm cơ bản     |
| `torch.nn`            | Neural network layers       |
| `torch.optim`         | Optimizers (SGD, Adam, ...) |
| `torch.utils.data`    | DataLoader, Dataset         |
| `torch.nn.functional` | Activation functions        |

---

## 10. Ví dụ hoàn chỉnh

```python
import torch
import torch.nn as nn
import torch.optim as optim

# 1. Dữ liệu
x = torch.randn(100, 1)
y = 2 * x + 1 + torch.randn(100, 1) * 0.1

# 2. Model
model = nn.Linear(1, 1)

# 3. Setup training
optimizer = optim.SGD(model.parameters(), lr=0.01)
loss_fn = nn.MSELoss()

# 4. Training
for epoch in range(100):
    pred = model(x)
    loss = loss_fn(pred, y)

    loss.backward()
    optimizer.step()
    optimizer.zero_grad()

    if (epoch + 1) % 20 == 0:
        print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

# 5. Kết quả
print(f"Weight: {model.weight.item():.4f} (Expected: 2.0)")
print(f"Bias: {model.bias.item():.4f} (Expected: 1.0)")
```

---

## 11. Lỗi phổ biến

| Lỗi                 | Nguyên nhân               | Cách fix              |
| ------------------- | ------------------------- | --------------------- |
| ❌ GPU vô dụng      | Quên `.to(device)`        | Thêm `.to(device)`    |
| ❌ Shape mismatch   | Tensor shape sai          | Kiểm tra `.shape`     |
| ❌ Chậm             | Cài PyTorch CPU           | Cài đúng CUDA version |
| ❌ Module not found | Không dùng venv           | Dùng virtual env      |
| ❌ Gradient bằng 0  | Quên `requires_grad=True` | Thêm flag             |

---

## 12. Checklist mỗi project

```
✅ Tạo .venv
✅ Cài PyTorch với CUDA đúng
✅ Test torch.cuda.is_available()
✅ Chuẩn hóa dữ liệu
✅ Viết training loop đúng
✅ Log loss, metrics
✅ Save model thường xuyên
✅ Test trên validation set
```

---

## 13. Lộ trình 2 tuần

### Tuần 1 - Nền tảng

- [x] Tensor & operations
- [x] Autograd & backward
- [x] Linear model & training loop
- [x] GPU setup

### Tuần 2 - Thực hành

- [x] CNN (Image Classification)
- [x] Dataset + DataLoader
- [x] Train model thật
- [x] Evaluate & save model

---

## 🎯 Kết luận

> PyTorch không khó - chỉ cần nắm vững **tensor** + **training loop**

| Điểm       | Chi tiết                       |
| ---------- | ------------------------------ |
| 💡 Cốt lõi | Tensor + Autograd + Loop       |
| ⚡ GPU     | CUDA chỉ là tăng tốc           |
| 📚 Học tập | Thực chiến > Lý thuyết         |
| 🚀 Bắt đầu | Clone example → Modify → Train |

**Hãy bắt đầu coding ngay! 🔥**
