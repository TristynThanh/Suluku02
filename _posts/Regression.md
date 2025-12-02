---
title: Regression
date: 2025-12-02 09:00:00 +0700
categories: [Data Science, Machine Learning]
tags: [python]
toc: true      # Dòng này để hiện MỤC LỤC tự động bên phải
math: true     # Dòng này để gõ công thức TOÁN
---
Chào bạn, chào mừng bạn đến với thế giới AI! Video này là một bài giảng chuyên sâu về **các phương pháp đánh giá độ chính xác cho bài toán Hồi quy (Regression)**.

Để mình giải thích cho bạn một cách đơn giản, dễ hiểu nhất, bỏ qua các công thức toán học phức tạp nhé.

### 1. Bài toán Hồi quy (Regression) là gì?
Trước khi đi vào nội dung chính, bạn cần hiểu bài toán này là gì. Hãy tưởng tượng bạn muốn dạy máy tính **dự đoán giá nhà**.
*   Đầu vào: Diện tích, số phòng, vị trí...
*   Đầu ra: Một con số cụ thể (ví dụ: 5 tỷ, 3.5 tỷ...).
Việc dự đoán ra một **con số liên tục** như vậy gọi là Hồi quy.

### 2. Nội dung chính của video: "Cây thước" đo lường sai số
Khi máy tính dự đoán giá nhà là 5 tỷ, nhưng thực tế nhà đó bán 5.2 tỷ. Vậy máy tính sai bao nhiêu? Làm sao biết mô hình này tốt hay dở? Video này giới thiệu các loại "thước đo" (Metrics) để trả lời câu hỏi đó.

Dưới đây là các loại thước đo chính được nhắc đến trong video, mình sẽ diễn giải bình dân nhất:

#### A. Nhóm đo sai số theo đơn vị gốc (Scale-dependent)
Nhóm này tính toán dựa trên sự chênh lệch trực tiếp (ví dụ: chênh lệch bao nhiêu tiền).

1.  **ME (Mean Error - Sai số trung bình):**
    *   *Cách tính:* Lấy (Giá thực - Giá dự đoán) rồi tính trung bình.
    *   *Vấn đề:* Nếu nhà A dự đoán thấp hơn 200tr (-200), nhà B dự đoán cao hơn 200tr (+200). Cộng lại chia đôi ra 0. Trông có vẻ hoàn hảo nhưng thực ra dự đoán sai bét. Đây gọi là lỗi "triệt tiêu lẫn nhau".

2.  **MAE (Mean Absolute Error - Sai số tuyệt đối trung bình):**
    *   *Cách tính:* Lấy trị tuyệt đối của sai lệch (luôn là số dương) rồi tính trung bình. Bất kể đoán cao hay thấp, cứ lệch 200tr là tính lỗi 200tr.
    *   *Ưu điểm:* Dễ hiểu, không bị triệt tiêu lỗi.
    *   *Nhược điểm:* Không biết được máy đang đoán quá cao (over) hay quá thấp (under).

3.  **MSE (Mean Squared Error) & RMSE:**
    *   *Cách tính:* Bình phương độ lệch lên. (Ví dụ lệch 2 thì bình phương thành 4, lệch 10 thì bình phương thành 100).
    *   *Tại sao phải làm khó vậy?* Để **phạt nặng những lỗi lớn**. Nếu máy đoán sai một chút thì không sao, nhưng sai quá lớn (gọi là *outlier* - ngoại lai) thì chỉ số này sẽ tăng vọt lên để cảnh báo.

#### B. Nhóm đo sai số theo phần trăm (Percentage Errors)
Nhóm này trả lời câu hỏi: "Sai số chiếm bao nhiêu % giá trị thật?". Nó giúp so sánh dễ hơn giữa các tập dữ liệu khác nhau (ví dụ so sánh giá nhà ở quê và giá nhà phố cổ).

1.  **MAPE (Mean Absolute Percentage Error):**
    *   *Ý nghĩa:* Dự đoán sai lệch bao nhiêu phần trăm (ví dụ sai 10%).
    *   *Vấn đề:* Nếu giá trị thực tế bằng 0 (ví dụ doanh thu ngày hôm đó là 0 đồng), thì phép chia cho 0 sẽ bị lỗi vô cực. Ngoài ra, nó phạt việc dự đoán cao hơn và thấp hơn không công bằng.

2.  **sMAPE (Symmetric MAPE):**
    *   Một phiên bản cải tiến của MAPE để cố gắng khắc phục sự mất cân bằng và vấn đề chia cho 0, nhưng cách giải thích kết quả của nó hơi khó hiểu với người thường.

#### C. Nhóm đo sai số tương đối (Relative Errors)
*   **MRAE / RSE:** So sánh mô hình của bạn với một mô hình "ngây thơ" (naive) hoặc mô hình chuẩn (baseline). Ví dụ: So sánh mô hình AI xịn xò của bạn với việc cứ lấy trung bình giá nhà của tháng trước làm dự đoán. Nếu chỉ số này < 1, nghĩa là mô hình của bạn tốt hơn cách đoán mò đơn giản.

### 3. Từ thước đo (Metric) đến Hàm mất mát (Loss Function)
Phần cuối video, giảng viên nói về mối liên hệ giữa việc đánh giá và việc dạy máy học.
*   **Metric (Thước đo):** Dùng để con người nhìn vào và báo cáo kết quả (Ví dụ: Sếp ơi, mô hình sai số khoảng 5%).
*   **Loss Function (Hàm mất mát):** Là công thức toán học để máy tính tự "phạt" mình trong quá trình học nhằm giảm thiểu sai số.
*   *Ví dụ:* Nếu dùng MSE làm hàm mất mát, máy sẽ sợ các lỗi lớn và cố gắng tránh xa các dự đoán sai lệch quá nhiều. Nếu dùng MAE, máy sẽ học một cách "bình thản" hơn.
*   **Huber Loss:** Một sự kết hợp thông minh giữa MAE và MSE để tận dụng ưu điểm của cả hai (vừa bền vững, vừa phạt lỗi lớn hợp lý).

### Tóm lại cho người mới bắt đầu:
Video này dạy bạn cách **chấm điểm** cho một con AI dự đoán số liệu.
1.  Nếu muốn biết sai lệch bao nhiêu đơn vị (ví dụ bao nhiêu tiền): Dùng **MAE** hoặc **RMSE**.
2.  Nếu muốn trừng phạt thật nặng các dự đoán sai ngớ ngẩn (sai quá lớn): Dùng **MSE/RMSE**.
3.  Nếu muốn báo cáo cho sếp theo kiểu dễ hiểu (sai bao nhiêu %): Dùng **MAPE**.
4.  Hiểu được các chỉ số này giúp bạn chọn đúng "thước đo" để huấn luyện AI tốt hơn.
