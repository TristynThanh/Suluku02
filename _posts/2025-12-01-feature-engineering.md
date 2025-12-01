---
title: Bài 1 - Kỹ thuật Feature Engineering
date: 2025-12-01 09:00:00 +0700
categories: [Data Science, Machine Learning]
tags: [feature-engineering, python]
toc: true      # Dòng này để hiện MỤC LỤC tự động bên phải
math: true     # Dòng này để gõ công thức TOÁN
---

Hiện nay các phương pháp học máy xuất hiện ngày càng nhiều...

## 1. Giới thiệu về Feature Engineering
Feature Engineering là quá trình sử dụng kiến thức chuyên môn...

> **Ghi chú:** Đây là kỹ thuật quan trọng nhất trong ML.

## 2. Các kỹ thuật chính
Về kỹ thuật thì chúng ta có 3 phương pháp chính:

### 2.1. Trích lọc đặc trưng (Feature Extraction)
Không phải toàn bộ thông tin được cung cấp từ một biến dự báo...

* **Xử lý ảnh:** CNN lọc ra các cạnh, góc...
* **Xử lý ngôn ngữ:** Túi từ (Bag of Words)...

### 2.2. Biến đổi dữ liệu (Feature Transformation)
Biến đổi dữ liệu gốc thành những dữ liệu phù hợp với mô hình.

Công thức chuẩn hóa Min-Max:

$$x_{new} = \frac{x - min(x)}{max(x) - min(x)}$$

### 2.3. Lựa chọn đặc trưng (Feature Selection)
Chọn ra những biến quan trọng nhất.

1. Phương pháp thống kê.
2. Sử dụng mô hình có sẵn.
3. Sử dụng Grid Search.
