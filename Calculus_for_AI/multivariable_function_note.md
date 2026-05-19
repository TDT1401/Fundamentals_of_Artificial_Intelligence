# Hàm Nhiều Biến - Ghi Chú Lý Thuyết

Tài liệu này tóm tắt lại nội dung trong notebook `multivariable_function.ipynb`.

## 1. Hàm nhiều biến là gì?

Hàm nhiều biến là hàm có **nhiều hơn một biến đầu vào**.

Ví dụ:

$$y = f(x)$$

đây là hàm một biến, còn:

$$z = f(x, y)$$

là hàm nhiều biến.

Tổng quát hơn:

$$f(x_1, x_2, x_3, ..., x_n)$$

Nghĩa là output phụ thuộc vào nhiều input cùng lúc.

## 2. Ví dụ đơn giản

Xét hàm:

$$f(x, y) = x^2 + y^2$$

Đây là hàm có 2 biến đầu vào là $x$ và $y$.

Ta có:

$$f(1,2)=1^2+2^2=5$$

$$f(3,4)=3^2+4^2=25$$

## 3. Hàm nhiều biến dùng để làm gì?

Hàm nhiều biến được dùng để mô tả các bài toán mà kết quả phụ thuộc vào nhiều yếu tố.

Ví dụ:

### Giá nhà

$$Price = f(area, location, age)$$

Giá nhà phụ thuộc vào:

- Diện tích
- Vị trí
- Tuổi căn nhà

### Điểm sinh viên

$$Score = f(math, english, attendance)$$

Điểm số phụ thuộc vào nhiều yếu tố, không chỉ một biến.

## 4. Cách làm việc với hàm nhiều biến

Tùy mục tiêu bài toán mà ta dùng công cụ khác nhau:

| Mục tiêu                        | Công cụ dùng             |
| ------------------------------- | ------------------------ |
| Tính output                     | Thay số vào hàm          |
| Xem từng biến ảnh hưởng thế nào | Đạo hàm riêng            |
| Xem hướng tăng nhanh nhất       | Gradient                 |
| Tìm điểm nhỏ nhất / lớn nhất    | Đạo hàm riêng + Gradient |
| Tối ưu trong AI                 | Gradient Descent         |

## 5. Đạo hàm riêng trong hàm nhiều biến

Xét hàm:

$$f(x,y)=x^2+3y^2$$

Đạo hàm riêng theo $x$:

$$\frac{\partial f}{\partial x}=2x$$

Đạo hàm riêng theo $y$:

$$\frac{\partial f}{\partial y}=6y$$

Ý nghĩa:

- $\frac{\partial f}{\partial x}$ cho biết nếu chỉ đổi $x$ thì hàm thay đổi nhanh thế nào.
- $\frac{\partial f}{\partial y}$ cho biết nếu chỉ đổi $y$ thì hàm thay đổi nhanh thế nào.

## 6. Gradient

Gradient là vector gom tất cả đạo hàm riêng lại.

Với hàm:

$$f(x,y)=x^2+3y^2$$

gradient là:

$$\nabla f(x,y)=\left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right)$$

Thay đạo hàm riêng vào ta được:

$$\nabla f(x,y)=(2x, 6y)$$

Ý nghĩa:

- Gradient chỉ hướng hàm tăng nhanh nhất.
- Độ lớn của gradient cho biết hàm tăng mạnh hay yếu.

## 7. Tính gradient bằng Python

Trong notebook, SymPy được dùng để tính đạo hàm riêng và gradient ký hiệu.

Với hàm $f(x, y) = x^2 + 3y^2$:

- $\frac{\partial f}{\partial x} = 2x$
- $\frac{\partial f}{\partial y} = 6y$
- Gradient là $[2x, 6y]$

Tại điểm $(2,1)$, gradient là $[4, 6]$.

## 8. Gradient Descent

Nếu muốn tìm điểm làm hàm nhỏ nhất, ta đi ngược hướng gradient.

Công thức cập nhật:

$$x = x - \eta \frac{\partial f}{\partial x}$$

$$y = y - \eta \frac{\partial f}{\partial y}$$

Trong đó:

- $\eta$ là learning rate
- Gradient chỉ hướng tăng nhanh nhất
- Muốn giảm hàm thì đi ngược hướng gradient

## 9. Demo Gradient Descent

Với hàm:

$$f(x,y)=x^2+y^2$$

gradient là:

$$\nabla f(x,y)=[2x,2y]$$

Khi áp dụng Gradient Descent, giá trị của $x$, $y$ và $f(x,y)$ sẽ giảm dần qua từng bước, tiến gần về điểm nhỏ nhất tại $(0,0)$.

## 10. Liên hệ với AI

Trong AI, model thường có rất nhiều tham số:

$$w_1, w_2, w_3, ..., w_n$$

Loss function thường là hàm nhiều biến:

$$L(w_1, w_2, w_3, ..., w_n)$$

Mục tiêu của AI là tìm bộ tham số làm loss nhỏ nhất.

Quy trình cơ bản:

1. Có loss function
2. Tính đạo hàm riêng theo từng tham số
3. Gom lại thành gradient
4. Dùng gradient descent để update tham số

Nói ngắn gọn:

> Machine Learning và Deep Learning về bản chất là tối ưu một hàm nhiều biến rất lớn.

## 11. Bài tập tự luyện

### Bài 1

Cho hàm:

$$f(x,y)=x^2+y^2+2x$$

Yêu cầu:

- Tính $f(2,3)$
- Tính $\frac{\partial f}{\partial x}$
- Tính $\frac{\partial f}{\partial y}$
- Viết gradient

### Bài 2

Cho hàm:

$$g(x,y)=3x^2+4xy+y^2$$

Yêu cầu:

- Tính đạo hàm riêng theo $x$
- Tính đạo hàm riêng theo $y$
- Tính gradient tại điểm $(1,2)$

### Bài 3

Dùng Python để chạy Gradient Descent cho hàm:

$$h(x,y)=x^2+2y^2$$

## 12. Tóm tắt cuối bài

- Hàm nhiều biến là hàm có nhiều input.
- Muốn tính output thì thay số vào hàm.
- Muốn xem từng biến ảnh hưởng thế nào thì dùng đạo hàm riêng.
- Muốn biết hướng tăng mạnh nhất thì dùng gradient.
- Muốn tối ưu hàm thì dùng gradient descent.
- Trong AI, loss function thường là hàm nhiều biến rất lớn.
