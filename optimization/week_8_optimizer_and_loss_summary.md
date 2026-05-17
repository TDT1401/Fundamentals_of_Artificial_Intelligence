# Tuần 8 — Loss Function, Gradient Descent, SGD, Adam

---

# 1. Tổng quan

Trong Machine Learning và Deep Learning, model học theo quy trình:

```text
Input data
    ↓
Model dự đoán
    ↓
Loss Function tính độ sai
    ↓
Gradient tính hướng giảm lỗi
    ↓
Optimizer cập nhật weights
    ↓
Model tốt hơn
```

Đây chính là “trái tim” của quá trình training.

---

# 2. Loss Function là gì?

Loss Function là hàm dùng để đo:

> Model đang sai bao nhiêu so với thực tế.

Loss càng nhỏ → model càng tốt.

Loss càng lớn → model càng sai.

---

# 3. Ví dụ trực giác về Loss

Giả sử:

- Giá nhà thật = 10 tỷ
- Model đoán = 7 tỷ

Sai số:

\[
10 - 7 = 3
\]

Nếu dùng MSE:

\[
Loss = (10 - 7)^2 = 9
\]

=> Loss = 9 nghĩa là model đang sai khá nhiều.

---

# 4. Các Loss Function phổ biến

| Loss Function | Dùng cho       | Ý nghĩa             |
| ------------- | -------------- | ------------------- |
| MSE           | Regression     | Bình phương sai số  |
| RMSE          | Regression     | Căn bậc hai của MSE |
| MAE           | Regression     | Sai số tuyệt đối    |
| Cross Entropy | Classification | Đo độ sai xác suất  |

---

# 5. Gradient là gì?

Gradient là vector đạo hàm.

Nó cho biết:

> Muốn loss giảm nhanh nhất thì weights phải thay đổi theo hướng nào.

Ví dụ:

- Gradient dương → giảm weight
- Gradient âm → tăng weight

---

# 6. Gradient Descent là gì?

Gradient Descent là thuật toán tối ưu hóa.

Nhiệm vụ:

> Cập nhật weights để loss nhỏ dần.

Công thức:

$$
w_{new} = w_{old} - \eta \cdot \frac{\partial L}{\partial w}
$$

Trong đó:

| Ký hiệu                         | Ý nghĩa       |
| ------------------------------- | ------------- |
| $w$                             | Weight        |
| $L$                             | Loss          |
| $\eta$                          | Learning rate |
| $\frac{\partial L}{\partial w}$ | Gradient      |

---

# 7. Ý nghĩa trực giác của Gradient Descent

Hãy tưởng tượng:

- Loss function giống một ngọn núi
- Model đang đứng somewhere trên núi
- Gradient chỉ hướng đi xuống nhanh nhất
- Gradient Descent sẽ đi xuống để tìm điểm thấp nhất

Điểm thấp nhất:

$$
Loss \approx 0
$$

=> Model dự đoán rất tốt.

---

# 8. Learning Rate

Learning Rate quyết định:

> Model update nhanh hay chậm.

---

## Learning rate quá nhỏ

```text
Học rất chậm
```

---

## Learning rate quá lớn

```text
Nhảy loạn → không hội tụ
```

---

# 9. SGD (Stochastic Gradient Descent)

Gradient Descent truyền thống:

- Dùng toàn bộ dataset để update.

SGD:

- Update từng sample hoặc mini-batch nhỏ.

---

## Ưu điểm của SGD

- Nhanh hơn
- Tốn ít RAM hơn
- Phù hợp Deep Learning

---

## Nhược điểm

- Dao động mạnh
- Loss không mượt

---

# 10. Adam Optimizer

Adam là optimizer hiện đại và phổ biến nhất.

Adam kết hợp:

- Momentum
- RMSProp
- SGD

Adam thông minh hơn vì:

- Tự điều chỉnh learning rate
- Học nhanh hơn
- Ổn định hơn

---

# 11. So sánh Gradient Descent, SGD và Adam

| Thuật toán       | Đặc điểm                   |
| ---------------- | -------------------------- |
| Gradient Descent | Chậm nhưng ổn định         |
| SGD              | Nhanh nhưng dao động       |
| Adam             | Nhanh + ổn định + phổ biến |

---

# 12. Mối quan hệ giữa Loss và Optimizer

## Loss Function

Trả lời câu hỏi:

> “Model sai bao nhiêu?”

---

## Gradient

Trả lời câu hỏi:

> “Giảm loss theo hướng nào?”

---

## Optimizer

Trả lời câu hỏi:

> “Update weights như thế nào?”

---

# 13. Flow đầy đủ khi training AI

```text
Data
 ↓
Predict
 ↓
Loss Function
 ↓
Gradient
 ↓
Optimizer
 ↓
Update weights
 ↓
Predict tốt hơn
```

---

# 14. Ví dụ thực tế

| Bài toán          | Loss Function |
| ----------------- | ------------- |
| Dự đoán giá nhà   | MSE           |
| Dự đoán nhiệt độ  | MAE           |
| Phân loại mèo/chó | Cross Entropy |
| ChatGPT sinh text | Cross Entropy |

---

# 15. Tổng kết cực ngắn

## Loss Function

> Đo model sai bao nhiêu.

---

## Gradient

> Chỉ hướng giảm loss.

---

## Gradient Descent

> Đi theo hướng gradient để giảm loss.

---

## SGD

> Gradient Descent nhanh hơn bằng mini-batch.

---

## Adam

> SGD nâng cấp, thông minh và ổn định hơn.

---

# 16. Kết luận

Tuần 8 thực chất là học cách:

> Làm cho model dự đoán ngày càng đúng hơn.

Pipeline cốt lõi:

```text
Loss Function
    ↓
Gradient
    ↓
Optimizer
    ↓
Update weights
```

Nếu hiểu được chuỗi này thì bạn đã hiểu nền tảng của toàn bộ Machine Learning và Deep Learning.
