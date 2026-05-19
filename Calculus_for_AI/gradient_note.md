# Gradient và Gradient Descent

## 1. Gradient là gì?

**Gradient** là vector chứa các **đạo hàm riêng** của một hàm nhiều biến.

Nếu hàm có dạng:

$$f(x, y)$$

thì gradient của hàm là:

$$\nabla f(x, y) = \left[\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right]$$

Trong đó:

- $\frac{\partial f}{\partial x}$: đạo hàm riêng theo biến $x$
- $\frac{\partial f}{\partial y}$: đạo hàm riêng theo biến $y$
- $\nabla f$: ký hiệu gradient

## 2. Ví dụ cơ bản

Cho hàm:

$$f(x, y) = x^2 + y^2$$

Ta có:

$$\frac{\partial f}{\partial x} = 2x$$

$$\frac{\partial f}{\partial y} = 2y$$

Vậy gradient là:

$$\nabla f(x, y) = [2x, 2y]$$

Tại điểm $(3, 4)$:

$$\nabla f(3, 4) = [6, 8]$$

## 3. Ý nghĩa trực giác của Gradient

Gradient cho biết:

1. Hàm tăng nhanh nhất theo hướng nào.
2. Độ dốc tại điểm đó lớn hay nhỏ.

Hình dung như đang đứng trên một ngọn núi:

- Gradient chỉ hướng leo lên nhanh nhất.
- Đi ngược gradient là hướng đi xuống nhanh nhất.
- Trong Machine Learning, ta thường muốn giảm loss, nên ta đi ngược gradient.

## 4. Gradient khác gì đạo hàm riêng?

Đạo hàm riêng chỉ xét **một biến tại một thời điểm**.

Gradient gom tất cả đạo hàm riêng lại thành **một vector**.

Ví dụ:

$$f(x, y, z) = x^2 + y^2 + z^2$$

Gradient là:

$$\nabla f(x, y, z) = [2x, 2y, 2z]$$

Nói ngắn gọn:

$$\text{Gradient} = \text{vector chứa các đạo hàm riêng}$$

## 5. Tính Gradient bằng Python

Trong notebook, SymPy được dùng để tính đạo hàm riêng và gradient ký hiệu.

Ví dụ với hàm $f(x, y) = x^2 + y^2$:

- $\frac{\partial f}{\partial x} = 2x$
- $\frac{\partial f}{\partial y} = 2y$
- Gradient là $[2x, 2y]$

Tại điểm $(3, 4)$, gradient trở thành $[6, 8]$.

## 6. Gradient Descent là gì?

**Gradient Descent** là thuật toán dùng gradient để tìm điểm làm hàm nhỏ nhất.

Công thức cập nhật cơ bản:

$$x_{new} = x_{old} - \alpha \nabla f(x)$$

Trong đó:

- $x_{old}$: giá trị hiện tại
- $x_{new}$: giá trị sau khi cập nhật
- $\alpha$: learning rate
- $\nabla f(x)$: gradient
- Dấu trừ nghĩa là đi ngược hướng gradient để giảm giá trị hàm

## 7. Demo Gradient Descent với hàm một biến

Với hàm:

$$f(x) = x^2$$

Ta có:

$$f'(x) = 2x$$

Điểm nhỏ nhất của hàm là $x = 0$.

Gradient Descent sẽ bắt đầu từ một giá trị ban đầu và tiến dần về 0 bằng cách liên tục cập nhật theo hướng ngược gradient.

## 8. Demo Gradient Descent với hàm hai biến

Với hàm:

$$f(x, y) = x^2 + y^2$$

Gradient là:

$$\nabla f(x, y) = [2x, 2y]$$

Công thức cập nhật:

$$x_{new} = x_{old} - \alpha (2x)$$

$$y_{new} = y_{old} - \alpha (2y)$$

## 9. Bài tập thực hành

### Bài 1

Cho hàm:

$$f(x, y) = 3x^2 + 2y^2$$

Yêu cầu:

1. Tính gradient bằng tay.
2. Dùng SymPy để kiểm tra.
3. Tính gradient tại điểm $(2, 3)$.

### Bài 2

Cho hàm:

$$f(x, y) = x^2 + 4xy + y^2$$

Yêu cầu:

1. Tính $\frac{\partial f}{\partial x}$.
2. Tính $\frac{\partial f}{\partial y}$.
3. Viết gradient của hàm.

### Bài 3

Viết code Gradient Descent để tìm giá trị nhỏ nhất của:

$$f(x) = (x - 4)^2$$

Gợi ý:

$$f'(x) = 2(x - 4)$$

Điểm nhỏ nhất đúng là $x = 4$.

## 10. Tóm tắt nhanh

- Gradient là vector chứa các đạo hàm riêng.
- Gradient cho biết hướng hàm tăng nhanh nhất.
- Muốn giảm hàm thì đi ngược hướng gradient.
- Gradient Descent là thuật toán dùng gradient để tìm điểm làm hàm nhỏ nhất.
- Trong Machine Learning, Gradient Descent dùng để giảm loss và cập nhật tham số của model.
