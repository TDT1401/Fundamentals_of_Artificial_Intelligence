# Đạo Hàm - derivative

## 1. Đạo hàm là gì?

Đạo hàm, tiếng Anh là _derivative_, là khái niệm dùng để đo **tốc độ thay đổi** của một hàm số tại một điểm cụ thể.

Nói đơn giản, nếu đầu vào thay đổi một chút thì đầu ra thay đổi nhanh hay chậm bao nhiêu, đạo hàm sẽ cho ta biết điều đó.

Ví dụ trực giác:

- Nếu $x$ là thời gian và $y$ là quãng đường, thì đạo hàm của quãng đường theo thời gian chính là vận tốc.
- Nếu một hàm tăng rất nhanh, đạo hàm của nó sẽ lớn.
- Nếu một hàm giảm, đạo hàm của nó mang giá trị âm.

## 2. Định nghĩa toán học của đạo hàm

Định nghĩa chuẩn của đạo hàm là:

$$
f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}
$$

Ý nghĩa của từng thành phần:

- $f'(x)$: đạo hàm của hàm số $f(x)$ tại điểm $x$.
- $h$: một thay đổi rất nhỏ của biến $x$.
- $f(x+h)-f(x)$: mức thay đổi của đầu ra.
- $\frac{f(x+h)-f(x)}{h}$: tốc độ thay đổi trung bình.
- Khi $h \to 0$, ta có tốc độ thay đổi tức thời tại đúng một điểm.

Tóm lại, đạo hàm chính là **tốc độ thay đổi tức thời**.

## 3. Ý nghĩa hình học của đạo hàm

Trong hình học, đạo hàm tại một điểm chính là **độ dốc của đường tiếp tuyến** tại điểm đó.

Nhìn theo dấu của đạo hàm:

- Nếu đạo hàm $> 0$ thì hàm số đang tăng.
- Nếu đạo hàm $< 0$ thì hàm số đang giảm.
- Nếu đạo hàm $= 0$ thì hàm số có thể đang ở điểm cực đại, cực tiểu hoặc một đoạn phẳng.

## 4. Quy tắc và công thức đạo hàm cơ bản

### 4.1 Đạo hàm của hằng số

Nếu $c$ là một hằng số thì:

$$
\frac{d}{dx}(c)=0
$$

Lý do: hằng số không thay đổi theo $x$ nên tốc độ thay đổi bằng 0.

### 4.2 Quy tắc lũy thừa

Đây là quy tắc quan trọng nhất:

$$
\frac{d}{dx}(x^n)=nx^{n-1}
$$

Cách nhớ nhanh:

1. Kéo số mũ xuống phía trước.
2. Giảm số mũ đi 1.

Ví dụ:

$$
\frac{d}{dx}(x^3)=3x^2
$$

$$
\frac{d}{dx}(x^5)=5x^4
$$

### 4.3 Đạo hàm của $x$

Vì $x=x^1$ nên:

$$
\frac{d}{dx}(x)=1
$$

### 4.4 Đạo hàm của căn

Khi gặp căn, nên đổi về lũy thừa:

$$
\sqrt{x}=x^{1/2}
$$

Suy ra:

$$
\frac{d}{dx}(\sqrt{x})=\frac{1}{2\sqrt{x}}
$$

### 4.5 Đạo hàm của tổng và hiệu

Nếu hàm gồm nhiều hạng tử cộng hoặc trừ nhau, ta lấy đạo hàm từng phần:

$$
(f(x)+g(x))'=f'(x)+g'(x)
$$

$$
(f(x)-g(x))'=f'(x)-g'(x)
$$

### 4.6 Nhân với hằng số

Nếu một hàm được nhân với hằng số $c$ thì:

$$
(cf(x))'=cf'(x)
$$

### 4.7 Một số đạo hàm cơ bản cần nhớ

$$
\frac{d}{dx}(e^x)=e^x
$$

$$
\frac{d}{dx}(\ln x)=\frac{1}{x}
$$

$$
\frac{d}{dx}(\sin x)=\cos x
$$

$$
\frac{d}{dx}(\cos x)=-\sin x
$$

## 5. Ví dụ tính đạo hàm

### Ví dụ 1

Cho:

$$
f(x)=x^2
$$

Đạo hàm là:

$$
f'(x)=2x
$$

Ý nghĩa:

- Tại $x=1$, ta có $f'(1)=2$.
- Tại $x=3$, ta có $f'(3)=6$.

Điều này cho thấy đồ thị $x^2$ dốc hơn khi $x$ lớn hơn.

### Ví dụ 2

Cho:

$$
f(x)=4x^3-2x^2+7
$$

Đạo hàm từng phần:

- $4x^3 \rightarrow 12x^2$
- $-2x^2 \rightarrow -4x$
- $7 \rightarrow 0$

Kết quả:

$$
f'(x)=12x^2-4x
$$

### Ví dụ 3

Cho:

$$
f(x)=\sqrt{x}+3x^5
$$

Ta đổi $\sqrt{x}$ về dạng lũy thừa:

$$
f(x)=x^{1/2}+3x^5
$$

Đạo hàm là:

$$
f'(x)=\frac{1}{2\sqrt{x}}+15x^4
$$

### Ví dụ 4

Cho:

$$
f(x)=\frac{1}{x^2}
$$

Đổi về lũy thừa:

$$
f(x)=x^{-2}
$$

Đạo hàm:

$$
f'(x)=-2x^{-3}=\frac{-2}{x^3}
$$

## 6. Ký hiệu thường gặp

Một số cách viết tương đương của đạo hàm:

$$
f'(x)
$$

$$
\frac{dy}{dx}
$$

$$
\frac{d}{dx}f(x)
$$

Tất cả đều mang ý nghĩa: đạo hàm của $y$ theo $x$.

## 7. Vai trò của đạo hàm trong Machine Learning

Đạo hàm rất quan trọng trong Machine Learning vì nó giúp model biết nên điều chỉnh tham số theo hướng nào để làm loss nhỏ hơn.

Các ý chính:

- Đạo hàm cho biết nếu tăng tham số thì loss tăng hay giảm.
- Đạo hàm cho biết nên điều chỉnh tham số theo hướng nào.
- Đạo hàm cho biết mức điều chỉnh nên mạnh hay nhẹ.

Khái niệm liên quan:

- **Gradient** là vector chứa nhiều đạo hàm.
- **Gradient Descent** là thuật toán dùng đạo hàm để tìm điểm làm loss nhỏ nhất.

## 8. Tóm tắt nhanh

| Khái niệm        | Ý nghĩa                        |
| ---------------- | ------------------------------ |
| Derivative       | Đạo hàm                        |
| Rate of change   | Tốc độ thay đổi                |
| Slope            | Độ dốc                         |
| Tangent line     | Đường tiếp tuyến               |
| $f'(x)$          | Đạo hàm của $f(x)$             |
| $\frac{dy}{dx}$  | Mức thay đổi của $y$ theo $x$  |
| Gradient         | Vector gồm nhiều đạo hàm       |
| Gradient Descent | Thuật toán tối ưu dùng đạo hàm |

## 9. Kết luận

Điều quan trọng nhất cần nhớ là: **đạo hàm cho biết một hàm số đang thay đổi nhanh hay chậm tại một điểm**. Đây là nền tảng rất quan trọng để học tiếp về gradient, tối ưu hóa và các thuật toán trong AI.
