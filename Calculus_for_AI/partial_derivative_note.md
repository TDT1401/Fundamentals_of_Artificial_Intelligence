# Partial Derivative

## 1. Đạo hàm riêng là gì?

Đạo hàm riêng dùng cho **hàm nhiều biến**.

Ví dụ:

$$
f(x,y)=x^2+3xy+y^2
$$

Hàm này phụ thuộc vào cả $x$ và $y$.

Khi lấy đạo hàm riêng:

- Theo $x$: xem $y$ là hằng số
- Theo $y$: xem $x$ là hằng số

Nói đơn giản:

> Đạo hàm riêng cho biết hàm thay đổi như thế nào khi chỉ một biến thay đổi, còn các biến khác giữ nguyên.

## 2. Ký hiệu cơ bản

Nếu có hàm:

$$f(x,y)$$

Đạo hàm riêng theo $x$:

$$\frac{\partial f}{\partial x}$$

Đạo hàm riêng theo $y$:

$$\frac{\partial f}{\partial y}$$

Ký hiệu $\partial$ dùng để phân biệt với đạo hàm thường $d$, vì đây là hàm nhiều biến.

## 3. Quy tắc tính nhanh

Muốn tính đạo hàm riêng theo biến nào:

1. Giữ biến đó là biến chính.
2. Các biến còn lại xem như hằng số.
3. Đạo hàm từng hạng tử như đạo hàm bình thường.

Ví dụ:

$$
f(x,y)=x^2+3xy+y^2
$$

Theo $x$:

$$\frac{\partial f}{\partial x}=2x+3y$$

Vì:

- $x^2 \rightarrow 2x$
- $3xy \rightarrow 3y$
- $y^2 \rightarrow 0$

Theo $y$:

$$\frac{\partial f}{\partial y}=3x+2y$$

Vì:

- $x^2 \rightarrow 0$
- $3xy \rightarrow 3x$
- $y^2 \rightarrow 2y$

## 4. Ví dụ đã giải

Cho:

$$
f(x,y)=3x^2y+2xy^2+y^3
$$

### Đạo hàm riêng theo $x$

Xem $y$ là hằng số:

$$\frac{\partial f}{\partial x}=6xy+2y^2$$

### Đạo hàm riêng theo $y$

Xem $x$ là hằng số:

$$\frac{\partial f}{\partial y}=3x^2+4xy+3y^2$$

### Đáp án cuối cùng

$$\boxed{\frac{\partial f}{\partial x}=6xy+2y^2}$$

$$\boxed{\frac{\partial f}{\partial y}=3x^2+4xy+3y^2}$$

## 5. Tính đạo hàm riêng bằng Python

Notebook dùng thư viện `sympy` để tính đạo hàm riêng.

Trong `sympy`:

```python
sp.diff(f, x)
```

nghĩa là lấy đạo hàm của hàm `f` theo biến `x`.

Với hàm:

$$f(x,y)=3x^2y+2xy^2+y^3$$

ta có thể tính:

- $\frac{\partial f}{\partial x}$
- $\frac{\partial f}{\partial y}$

bằng `sp.diff`.

## 6. Gradient là gì?

Gradient là vector chứa tất cả đạo hàm riêng.

Nếu:

$$f(x,y)$$

thì:

$$\nabla f = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right)$$

Ví dụ với:

$$f(x,y)=3x^2y+2xy^2+y^3$$

thì:

$$\nabla f = (6xy+2y^2,\ 3x^2+4xy+3y^2)$$

Trong Machine Learning, gradient rất quan trọng vì nó cho biết hướng để cập nhật tham số trong Gradient Descent.

## 7. Bài tập Python

### Bài 1

Cho:

$$f(x,y)=x^2y+xy^2$$

Yêu cầu:

- Tính $\frac{\partial f}{\partial x}$
- Tính $\frac{\partial f}{\partial y}$

### Bài 2

Cho:

$$f(x,y)=4x^3y^2+5xy$$

Yêu cầu:

- Tính $\frac{\partial f}{\partial x}$
- Tính $\frac{\partial f}{\partial y}$

### Bài 3

Cho:

$$f(x,y)=x^2+2xy+3y^2$$

Yêu cầu:

- Tính $\frac{\partial f}{\partial x}$
- Tính $\frac{\partial f}{\partial y}$

### Bài 4

Cho:

$$f(x,y)=x^2y+3xy^2$$

Yêu cầu:

- Tính $\frac{\partial f}{\partial x}$
- Tính $\frac{\partial f}{\partial y}$
- Tính tại điểm $(x,y)=(2,3)$

### Bài 5

Cho:

$$f(x,y)=2x^3+4x^2y+xy^2+5y^3$$

Yêu cầu:

- Tính đạo hàm riêng theo $x$
- Tính đạo hàm riêng theo $y$
- Tính gradient của hàm
- Tính gradient tại điểm $(1,2)$

## 8. Tóm tắt nhanh

- Đạo hàm riêng dùng cho hàm nhiều biến.
- Khi lấy đạo hàm riêng theo một biến, các biến còn lại xem là hằng số.
- $\partial$ là ký hiệu dùng cho đạo hàm riêng.
- Gradient là vector chứa tất cả đạo hàm riêng.
- Gradient được dùng rất nhiều trong tối ưu hóa và Machine Learning.
