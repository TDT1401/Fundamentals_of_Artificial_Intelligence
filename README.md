# 🤖 Intro to AI - PyTorch Learning Project

> Dự án học tập về **Deep Learning** và **Neural Networks** sử dụng **PyTorch**

## 📋 Mục đích dự án

Dự án này được tạo ra để **học tập** các khái niệm cơ bản của AI:

- ✅ Tensors và PyTorch basics
- ✅ Xây dựng Neural Networks
- ✅ Training loops và optimization
- ✅ Image Classification với FashionMNIST
- ✅ GPU/CUDA acceleration

---

## 📂 Cấu trúc dự án

```
intro_to_AI/
├── check.py                          # Script kiểm tra PyTorch & CUDA
├── listpy.ipynb                      # Notebook về Python basics
├── tensors.ipynb                     # Notebook về Tensors
├── data/
│   └── FashionMNIST/                 # Dataset FashionMNIST
│       └── raw/                      # Raw training & test data
├── docs/
│   └── pytorch.md                    # Hướng dẫn PyTorch tiếng Việt
├── models/
│   └── model.pth                     # Pre-trained model
└── pytorch/
    └── fashionMNISTImageClassifier.ipynb  # Main project notebook
```

---

## 🎯 Các Notebook chính

### 1. **listpy.ipynb**

Giới thiệu **Python basics** cần thiết cho Machine Learning

### 2. **tensors.ipynb**

Tìm hiểu về **Tensors** - đơn vị dữ liệu cơ bản trong PyTorch

### 3. **fashionMNISTImageClassifier.ipynb** ⭐ (Main)

**Phân loại hình ảnh thời trang** từ dataset FashionMNIST

#### Nội dung:

- 📥 Load FashionMNIST dataset (60K training + 10K test images)
- 🏗️ Xây dựng Neural Network (3 layers)
- 🚀 Training loop với SGD optimizer
- 📊 Testing & evaluation
- 💾 Lưu/load pre-trained model

#### Model Architecture:

```
Input (28x28)
  ↓
Flatten
  ↓
Linear (784 → 512) + ReLU
  ↓
Linear (512 → 512) + ReLU
  ↓
Linear (512 → 10)
  ↓
Output (10 classes)
```

---

## 🚀 Hướng dẫn sử dụng

### 1. Cài đặt môi trường

```bash
# Tạo virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Cài đặt dependencies
pip install torch torchvision torchaudio
pip install jupyter
```

### 2. Kiểm tra PyTorch & CUDA

```bash
python check.py
```

Output sẽ hiển thị:

- ✅ PyTorch version
- ✅ CUDA availability
- ✅ GPU info (nếu có)

### 3. Chạy Jupyter Notebook

```bash
jupyter notebook
```

Sau đó:

1. Mở `pytorch/fashionMNISTImageClassifier.ipynb`
2. Chạy từng cell theo thứ tự

---

## 📚 Dataset: FashionMNIST

**FashionMNIST** là dataset chứa hình ảnh các loại quần áo (28×28 pixels, grayscale)

**10 classes:**

- 0: T-shirt/top
- 1: Trouser
- 2: Pullover
- 3: Dress
- 4: Coat
- 5: Sandal
- 6: Shirt
- 7: Sneaker
- 8: Bag
- 9: Ankle boot

**Kích thước:**

- Training: 60,000 images
- Testing: 10,000 images

---

## 🔧 Công cụ & Thư viện

| Thư viện        | Mục đích                          |
| --------------- | --------------------------------- |
| **PyTorch**     | Framework chính cho deep learning |
| **torchvision** | Datasets và image utilities       |
| **Jupyter**     | Notebook interactivelearn         |
| **CUDA**        | GPU acceleration (nếu có)         |

---

## 💡 Các khái niệm chính được học

### 1. **Tensors**

- Cấu trúc dữ liệu nhiều chiều
- So sánh: NumPy arrays vs PyTorch tensors

### 2. **Neural Network**

- Layers: Linear, ReLU, Flatten
- Forward pass & backward pass

### 3. **Training Loop**

```
Epoch:
  ├─ Forward pass (input → model → output)
  ├─ Compute loss
  ├─ Backward pass (gradient calculation)
  └─ Optimizer step (update weights)
```

### 4. **Optimization**

- SGD (Stochastic Gradient Descent)
- Loss functions: CrossEntropyLoss

### 5. **Evaluation**

- Accuracy
- Loss metrics
- Test set validation

---

## ⚡ GPU/CUDA Support

Dự án tự động detect device:

```python
if torch.cuda.is_available():
    device = "cuda"      # GPU
elif hasattr(torch.backends, "mps"):
    device = "mps"       # Apple Silicon
else:
    device = "cpu"       # CPU
```

**Lợi ích GPU:**

- 🚀 Training **10-100x nhanh hơn**
- 💾 Xử lý dataset lớn hơn
- ⚡ Parallel computation

---

## 📖 Tài liệu tham khảo

- Xem file `docs/pytorch.md` để có **hướng dẫn chi tiết tiếng Việt**
- [PyTorch Official Docs](https://pytorch.org/docs/)
- [FashionMNIST Dataset](https://github.com/zalandoresearch/fashion-mnist)

---

## 🔍 Kiểm tra model

Pre-trained model đã được lưu tại `models/model.pth`

Để load và sử dụng:

```python
model = NeuralNetwork()
model.load_state_dict(torch.load('models/model.pth'))
model.eval()
```

---

## 📝 Ghi chú

- 💻 Project này **để học tập**, không phải production
- 🎓 Các comments và docstrings giúp hiểu code
- 🔄 Tự do modify và experiment
- 📊 Thử thay đổi hyperparameters: epochs, batch_size, learning rate

---

## ❓ Câu hỏi thường gặp

**Q: Model chạy chậm?**
A: Kiểm tra `check.py` xem có GPU không. Nếu không có, model sẽ chạy trên CPU.

**Q: Làm sao để cải thiện accuracy?**
A: Thử tăng epochs, điều chỉnh learning rate, hoặc thay đổi network architecture

**Q: Dataset đã download ở đâu?**
A: Được lưu tự động ở folder `data/FashionMNIST/`

---

## 📞 Liên hệ & Support

Nếu có thắc mắc về **PyTorch** hoặc **Deep Learning**:

- Đọc documentation trong `docs/pytorch.md`
- Xem comments trong code
- Tham khảo [PyTorch tutorials](https://pytorch.org/tutorials/)

---

**Happy Learning! 🚀 AI**

---

_Dự án tạo vào: April 2026_  
_PyTorch Version: 2.x_
