## 1. Mở đầu – Vì sao dễ lạc lối khi học AI


&nbsp;&nbsp;&nbsp;Trí tuệ nhân tạo (AI) xuất hiện khắp nơi: hệ thống gợi ý phim, trợ lý giọng nói hay chatbot **ChatGPT** có thể trả lời câu hỏi và viết mã. Điều này khiến nhiều người nghĩ rằng “học AI” là phải nhớ công thức khó hiểu hoặc nhảy ngay vào thuật toán phức tạp. Để không bị ngợp, bạn cần hiểu nền tảng, nguyên lý, lý do theo học và định hướng phù hợp với bản thân. Bài viết này mang đến cho bạn đọc thêm góc nhìn mới chi tiết, so sánh các hướng nghề nghiệp (Research vs Production) và giúp bạn chọn lĩnh vực chuyên sâu phù hợp.




## 2. AI là gì? Định nghĩa, mục đích và phạm vi.


&nbsp;&nbsp;&nbsp;**Trí tuệ nhân tạo** là lĩnh vực làm cho máy móc bắt chước trí thông minh của con người để thực hiện các nhiệm vụ như suy luận và học hỏi. Chẳng hạn như:
- **học tập (learning)**
- **suy luận (reasoning)**
- **nhận thức (perception)**
- **hiểu ngôn ngữ tự nhiên (natural language)**
- **ra quyết định (decision making).**

&nbsp;&nbsp;&nbsp;AI bao gồm nhiều cấp độ:
        
- **Học máy (Machine Learning – ML):** thuật toán học mẫu từ dữ liệu mà không cần lập trình tường minh.

- **Học sâu (Deep Learning):** một nhánh của học máy sử dụng mạng nơ‑ron nhiều lớp. Kiến trúc transformer – nền tảng của ChatGPT – giúp xử lý chuỗi dài.


- **AI tạo sinh:** mô hình như ChatGPT hoặc DALL‑E tạo ra nội dung mới (văn bản, hình ảnh, âm nhạc) bằng cách học mô hình thống kê trên dữ liệu.



## 3. Bản đồ Roadmap – Học gì và tại sao

&nbsp;&nbsp;&nbsp;Để học về AI, bạn cần nắm các nhánh kiến thức chính dưới đây. Bỏ qua bất kỳ nhánh nào đều dẫn đến lỗ hổng cho quá trình học tập và làm việc sau này.




| Nhánh | Nội dung cần học | Lý do quan trọng |
|---|---|---|
| Toán & Thống kê | Đại số tuyến tính (vectơ, ma trận), xác suất, thống kê cơ bản | Là ngôn ngữ mô tả thuật toán. Ví dụ, ChatGPT dựa trên phép nhân ma trận trong transformer; không có đại số tuyến tính, bạn khó hiểu và tối ưu mô hình. Xác suất giúp diễn giải đầu ra và độ bất định.. |
| Lập trình | Python, cấu trúc điều khiển, thư viện NumPy/pandas/PyTorch | Giúp bạn triển khai và thử nghiệm thuật toán. Không biết lập trình, bạn   khó phát triển dự án AI. |
| Xử lý dữ liệu | Thu thập, làm sạch, phân tích, trực quan hóa dữ liệu | Mô hình AI tốt phụ thuộc vào dữ liệu; dữ liệu kém sẽ tạo mô hình   thiên lệch. |
| Học máy | Hồi quy tuyến tính, K‑NN, thuật toán Boostraping: Decision Tree, Random Forest hay thuật toán Boosting: Gradient Boost, XG Boost, Ada Boost, Light Boost| Những thuật toán này xây dựng trực giác về cách mô hình học. |
| Học sâu | Mạng nơ‑ron cơ bản, CNN, RNN,   Transformer | Học sâu mở ra khả năng xử lý dữ liệu phức tạp như hình ảnh, âm thanh   và văn bản. |
| MLOps & Triển khai | Gói mô hình thành API, Docker, CI/CD | Mô hình chỉ có giá trị khi được triển khai để người dùng sử dụng. |
| Ứng dụng | NLP, Computer Vision, hệ gợi ý, đạo đức AI | Giúp bạn định hướng chuyên môn và xây dựng hệ thống công bằng, an   toàn. |



&nbsp;&nbsp;&nbsp; Nói tóm lại thì theo như tôi quan sát nó sẽ theo 1 cái flow như thế này: Toán quan trọng vì nó là ngôn ngữ để máy tính "Hiểu và tính toán" ví nó chỉ hiểu số, ma trận, vector chứ không hiểu như ngôn ngữ mà tôi đang viết, sau đó cần học lập trình để "Nói chuyện và ra lệch" cho máy tính xử lý thông tin. Còn về xử lý dữ liệu lý do cần có bước này thì bạn cứ hiểu đơn giản "Garbage in Garbage out". Machine Learning thì dạy máy học từ dữ liệu qua các thuật toán mà tôi đã nêu ở bảng thực ra còn nhiều thuật toán khác nữa mỗi cái có ưu và nhược điểm khác nhau, kiểu như đâu là "phương pháp học" tốt nhất cho trường hợp này.


## 4. Lộ trình học AI – Từ cơ bản đến nâng cao



### Cấp độ 1: Nền tảng

 1. **Toán & Thống kê**

	Bạn cần Toán trong AI vì:
	- hiểu thuật toán đang làm gì,
	- biết mô hình học như thế nào,
	- và hiểu tại sao kết quả lại đúng hoặc sai.

	**Những nội dung cốt lõi bao gồm:**
	- **Đại số tuyến tính**: vector, ma trận – dùng để biểu diễn dữ liệu và tham số mô hình  
	- **Giải tích**: đạo hàm – giúp mô hình tự điều chỉnh để học tốt hơn  
	- **Xác suất – thống kê**: giúp đo độ bất định, đánh giá sai số và độ tin cậy của mô hình  

	 **Nếu không có nền tảng toán:**
	- Mô hình sẽ giống như “hộp đen” kiểu như bạn rõ `input` và rõ `output` nhưng không hiểu được quy trình xử lý bên trong như thế nào.
	- Bạn không biết vì sao nó hội tụ, vì sao nó **overfit**, hay vì sao đổi tham số thì kết quả lại khác

 
2. **Python** 
	- nắm vững cú pháp cơ bản (if, loop, function)  
	- hiểu cấu trúc dữ liệu (list, dict, array)  
	- sử dụng được các thư viện nền tảng như:  
  	- **NumPy**: tính toán số học  
  	- **pandas**: xử lý bảng dữ liệu  
  	- **matplotlib**: vẽ biểu đồ

        
3. **Xử lý dữ liệu (Data Processing)**

	Bạn phải hiểu là AI không học từ thuật toán, mà học từ dữ liệu.
	Ở bước này, bạn học cách:
	- Đọc dữ liệu từ file (CSV, Excel, database),
	- Làm sạch dữ liệu (thiếu, sai, trùng lặp),
	- Phân tích và trực quan hóa dữ liệu để hiểu bản chất vấn đề.

	👉 **Một mô hình AI tốt phụ thuộc rất lớn vào dữ liệu đầu vào. Như tôi đã nói ở trên "Garbage in Garbage out"**  

	> Dữ liệu kém → mô hình học sai → kết quả sai.



### Cấp độ 2: Học máy
 
&nbsp;&nbsp;&nbsp;Sau khi có nền tảng, bạn bắt đầu bước vào **Machine Learning** – nơi máy không còn chạy theo luật cố định, mà **tự rút ra quy luật từ dữ liệu**. Có hai cách học, **học có giám sát (supervised learning)** và **học không có giám sát (unsupervised learning)**, nói dễ hiểu và ngắn gọn thì học có giám sát là cách học có dựa trên label, có gắn nhãn kiểu như trong data  bệnh nhân A có những đặc điểm ABCD này thì được gắn là "Khỏe Mạnh", còn bệnh nhân B thì có những đặc điểm ABCD kia thì gắn là "Có Bệnh" sau đó mô hình sẽ học và rút ra quy luật từ đó
  
  
  &nbsp;&nbsp;&nbsp;Ở AIO 2025 thì kiến thức này thường rơi vào Module 3 và Module 4, các projects của hai module đó thường sẽ là giải các bài toán về  **Regression ( Hồi quy)** và **Classification ( Phân loại)** 
  
 &nbsp;&nbsp;&nbsp;Ví dụ có project yêu cầu ta dự đoán giá nhà, giá thuê phòng hay kiểu dự đoán kết quả gì đó từ tệp data đó là Hồi Quy, còn những kiểu xác định bệnh nhân có bệnh hay không có bệnh, cháy nắng hay không cháy nắng, thư spam hay không spam dựa trên tệp dữ liệu thì đó là bài toán Phân Loại. 

&nbsp;&nbsp;&nbsp;Theo tôi thì, ở phần này hiểu đơn các **thuật toán Machine Learning chính là cách (hay phương pháp) để mô hình học từ dữ liệu**. Ở module 4 có một vài thuật toán quan trọng bạn sẽ được tìm hiểu, thường được chia theo thuật toán Bootstraping và Boosting

| Thuật toán | Có thể gọi là | Cách mô hình học |
|---|---|---|
| KNN | Phương pháp học theo khoảng cách | So sánh điểm dữ liệu |
| Decision Tree | Phương pháp học theo luật | Chia dữ liệu |
| Random Forest | Phương pháp học tập hợp | Học từ nhiều cây |
| AdaBoost | Phương pháp học sửa sai | Tăng trọng số mẫu khó |
| Gradient Boost | Phương pháp học tối ưu lỗi | Giảm loss từng bước |
| XGBoost | Boosting tối ưu | Boost + regularization |


 

![Cartoon_ Future Machine Learning Class - KDnuggets.jpg](assets/picture4.png)




### Cấp độ 3: Học sâu



&nbsp;&nbsp;&nbsp;**Nếu Machine Learning là giai đoạn con người còn phải chỉ cho mô hình “nên nhìn cái gì”, thì Deep Learning là bước mà mô hình tự học xem cái gì là quan trọng.** 

&nbsp;&nbsp;&nbsp;Học sâu (Deep Learning) là một nhánh của Machine Learning,
sử dụng mạng nơ-ron nhiều tầng để tự động học đặc trưng (features) từ dữ liệu thô.

👉 Sự khác biệt ở đây là:

- ML truyền thống: con người thiết kế đặc trưng
- Deep Learning: mô hình tự học đặc trưng

&nbsp;&nbsp;&nbsp;Vậy có thể coi Deep Learning là “phương pháp học của mô hình” mà tôi đã so sánh như Machine Learning ở trên không?

=> Có, và còn đúng hơn cả ML truyền thống, vì: Deep Learning định nghĩa cách mô hình học từ dữ liệu thô thông qua nhiều tầng biểu diễn.

&nbsp;&nbsp;&nbsp;Các kiến trúc học sâu tiêu biểu


**Nói cách khác:**
- **KNN** học bằng so sánh  
- **Decision Tree** học bằng chia dữ liệu  
- **Boosting** học bằng sửa sai  
- **Deep Learning** học bằng cách xây dựng biểu diễn tầng bậc

&nbsp;&nbsp;&nbsp;Các kiến trúc học sâu tiêu biểu (và cách chúng “học”):

1. **Mạng nơ-ron cơ bản (Neural Network):** 
	- **Học quan hệ phi tuyến phức tạp**
	- Nền tảng của mọi mô hình deep learning  
	- Mạnh hơn Machine Learning tuyến tính  

2. **CNN (Convolutional Neural Network)**
	- **Học bằng cách quét cục bộ**
	- Rất hiệu quả với dữ liệu hình ảnh  
	- Học cấu trúc và không gian  

3. **RNN / LSTM**
	- **Học bằng cách ghi nhớ chuỗi**
	- Dữ liệu theo thời gian  
	- Văn bản, chuỗi, tín hiệu  

4. **Transformer**
	- **Học bằng cách chú ý (attention)**
	- Không học tuần tự  
	- Tập trung vào phần quan trọng nhất của dữ liệu  

👉 Nền tảng của các mô hình ngôn ngữ lớn hiện nay.


![1.jpeg](/static/uploads/20260118_180745_c3e58533.jpeg)


### Cấp độ 4: MLOps & Triểnkhai



Sau khi bạn huấn luyện được một mô hình chạy ổn, bước tiếp theo là đưa nó ra dùng ngoài đời thật. **MLOps** đơn giản là tập hợp các công cụ và quy trình giúp bạn đóng gói mô hình, triển khai cho người dùng, theo dõi nó hoạt động ra sao và cập nhật khi cần. Nếu không có MLOps, mô hình chỉ dừng lại ở notebook để thử nghiệm, không tạo ra giá trị thực tế. Ví dụ phổ biến là biến mô hình thành API bằng FastAPI, dùng Docker để chạy ổn định và thiết lập CI/CD để cập nhật tự động.





### Cấp độ 5: Ứng dụng & Đạo đức



&nbsp;&nbsp;&nbsp;Học cách áp dụng AI vào các lĩnh vực thực tế như NLP, thị giác máy tính, hệ gợi ý, robot tự hành và AI tạo sinh. Đồng thời, tìm hiểu đạo đức AI để đảm bảo công bằng, minh bạch và tôn trọng quyền riêng tư.




## 5. Định hướng Research hay Production

&nbsp;&nbsp;&nbsp;Sau khi có nền tảng, bạn cần xác định con đường phù hợp: **nghiên cứu** hay **sản phẩm**. Mỗi hướng có ưu và nhược điểm. Mình nhớ là ở AIO có một buổi zoom TA Thanh Huy có chia sẻ về ưu và nhược điểm của mỗi cái.

| Khía cạnh | Nghiên cứu / Thử nghiệm | Sản phẩm / Ứng dụng | Lý do chọn |
|---|---|---|---|
| Mục tiêu | Tạo thuật toán mới, viết bài báo, chứng minh khái niệm | Xây dựng hệ thống ổn định phục vụ người dùng, giải quyết bài toán thực   tế | Chọn nghiên cứu nếu bạn thích khám phá, yêu thích toán và lý thuyết;   chọn sản phẩm nếu bạn muốn thấy tác động trực tiếp và thích xây dựng phần mềm   ổn định |
| Dữ liệu | Bộ dữ liệu nhỏ, được tuyển chọn cẩn thận | Dữ liệu lớn, phức tạp và thay đổi theo thời gian; cần pipeline, giám sát | Nghiên cứu phù hợp khi bạn có nguồn dữ liệu hạn chế; sản phẩm yêu cầu   năng lực xử lý big data và hạ tầng |
| Đánh giá | Tập trung vào chỉ số mô hình (accuracy, F1) và bài báo | Tập trung vào trải nghiệm người dùng, độ trễ, khả năng mở rộng và tác   động kinh doanh | Nếu thích giải bài toán tối ưu và công bố kết quả khoa học, chọn   nghiên cứu; nếu quan tâm tới tác động kinh doanh và trải nghiệm người dùng,   chọn sản phẩm |
| Hạ tầng | Thường chỉ cần notebook hoặc máy cục bộ | Yêu cầu kiến trúc CI/CD, Docker, server và giám sát | Sản phẩm phù hợp nếu bạn thích xây dựng hệ thống quy mô, làm việc với DevOps |
| Rủi ro | Rủi ro thấp; thất bại chủ yếu ảnh hưởng đến bài báo | Rủi ro cao; lỗi có thể gây hậu quả cho khách hàng và phải tuân thủ   quy định | Nghiên cứu phù hợp nếu bạn chấp nhận rủi ro thấp; sản phẩm yêu cầu   trách nhiệm cao |
| Công việc mẫu | Nghiên cứu sinh, nhà khoa học dữ liệu, nghiên cứu tại viện hoặc doanh   nghiệp | Kỹ sư học máy, kỹ sư MLOps, chuyên gia triển khai AI |  |




## 6. Chọn lĩnh vực chuyên sâu



&nbsp;&nbsp;&nbsp;Sau khi nắm vững nền tảng và định hướng nghề nghiệp, bước tiếp theo là chọn lĩnh vực chuyên sâu. Dưới đây là các chủ đề phổ biến, cùng ưu và nhược điểm và ví dụ công việc tương ứng.


| Lĩnh vực | Mô tả & kỹ năng    chính | Ưu điểm | Nhược điểm | Ví dụ công việc |
|---|---|---|---|---|
| Thị giác máy tính (Computer Vision) | Xây dựng mô hình xử lý và hiểu hình ảnh/video   bằng CNN, segmentation | Nhiều ứng dụng (xe tự lái, y tế) và nhu cầu   cao | Yêu cầu dữ liệu lớn và GPU mạnh; cần hiểu đặc   thù ảnh | Kỹ sư Computer Vision thiết kế hệ thống nhận   diện vật thể cho xe tự hành; nhà nghiên cứu phát triển mạng CNN cải tiến |
| Xử lý ngôn ngữ tự nhiên & Mô hình ngôn   ngữ lớn (NLP & LLMs) | Làm việc với văn bản, tokenization, embedding,   transformer | Nhiều ứng dụng (chatbot, dịch máy), đang “hot” | Ngôn ngữ phức tạp, dữ liệu không đồng nhất; mô   hình lớn tốn chi phí | Kỹ sư NLP phát triển chatbot hỗ trợ khách   hàng; nhà nghiên cứu LLM cải tiến kiến trúc để giảm thiên lệch |
| Chuỗi thời gian (Time Series) | Phân tích, dự báo dữ liệu dạng chuỗi; sử dụng   RNN/transformer | Thực tế trong tài chính, năng lượng, IoT | Phụ thuộc vào dữ liệu lịch sử và dễ bị nhiễu;   yêu cầu hiểu thống kê | Data scientist dự đoán nhu cầu điện; nhà phân   tích tài chính xây dựng mô hình dự báo giá cổ phiếu |
| Y tế (Medical AI) | Ứng dụng AI vào chẩn đoán và điều trị; sử dụng   CNN và transformer cho ảnh y tế | Tác động xã hội lớn, cải thiện chăm sóc sức khỏe | Đòi hỏi kiến thức y khoa, tuân thủ pháp lý và   dữ liệu nhạy cảm | Kỹ sư ML hợp tác với bác sĩ phát triển hệ thống   phát hiện ung thư; nhà nghiên cứu phát triển thuật toán chẩn đoán tự động |
| Agent AI & Học tăng cường   (Reinforcement Learning) | Phát triển agent học bằng tương tác và phần   thưởng; áp dụng trong game, robot | Mô phỏng hành vi thông minh, áp dụng trong   robot và tự động hóa | Thuật toán phức tạp, cần nhiều tính toán; khó ổn   định | Nhà nghiên cứu RL thiết kế agent chơi game; kỹ   sư robot áp dụng RL để điều khiển cánh tay robot |
| Tài chính (Finance) | Ứng dụng AI vào phân tích rủi ro, phát hiện   gian lận, giao dịch tự động | Cơ hội thu nhập cao, nhu cầu trong ngân hàng   và fintech | Áp lực lớn, phải tuân thủ quy định chặt chẽ; dữ   liệu nhạy cảm | Kỹ sư dữ liệu tài chính xây dựng mô hình chấm   điểm tín dụng; nhà giao dịch thuật toán thiết kế chiến lược tự động |
| Đa phương thức & Tạo sinh (Multimodal   & Generative AI) | Kết hợp nhiều loại dữ liệu (văn bản, hình ảnh,   âm thanh); phát triển mô hình tạo nội dung | Thú vị, sáng tạo; mở ra các ứng dụng mới như tạo   ảnh từ văn bản | Đòi hỏi tài nguyên tính toán lớn; dễ gây tranh   cãi (bản quyền, đạo đức) | Kỹ sư generative AI xây dựng hệ thống tạo hình   ảnh; nhà nghiên cứu phát triển mô hình text-to-video |
| Học máy truyền thống (ML) | Tập trung vào thuật toán cổ điển (hồi quy,   phân cụm, cây quyết định) | Nền tảng cho mọi ứng dụng, yêu cầu tính toán   thấp | Độ phức tạp thấp hơn, có thể bị thay thế trong   các bài toán phức tạp | Data scientist dùng random forest dự đoán   churn; kỹ sư phân tích dữ liệu marketing |
| Giáo dục (Education) | Ứng dụng AI trong dạy học: hệ gợi ý bài tập,   chấm bài tự động | Tác động xã hội tích cực, nhu cầu tăng trong   edtech | Thường thiếu dữ liệu lớn; cần hiểu phương pháp   giáo dục | Kỹ sư AI xây dựng hệ thống khuyến nghị bài học   cá nhân hóa; nhà nghiên cứu phát triển mô hình chấm điểm tự động |
| Robot & Tự động hóa (Robotics &   Automation) | Kết hợp AI với cảm biến, điều khiển và phần cứng | Tạo nên sản phẩm hữu hình (robot, drone); nhiều   ngành cần | Phức tạp vì phải hiểu cả phần cứng và phần mềm | Kỹ sư robot thiết kế robot công nghiệp; nhà   nghiên cứu phát triển thuật toán điều khiển tự trị |
| Vận hành máy học (MLOps) | Xây dựng pipeline dữ liệu, triển khai và giám   sát mô hình[15] | Nhu cầu cao trong doanh nghiệp; đảm bảo mô   hình hoạt động ổn định | Ít thiên về thuật toán, nhiều về hạ tầng và   quy trình | Kỹ sư MLOps xây dựng CI/CD cho mô hình; quản   lý hệ thống theo dõi hiệu suất |
| AI có thể giải thích được (XAI) | Phát triển phương pháp giải thích kết quả mô   hình, đánh giá fairness | Giúp tăng niềm tin của người dùng và tuân thủ   pháp lý | Đang nghiên cứu mạnh, chưa có phương pháp chuẩn;   đôi khi giảm độ chính xác | Nhà nghiên cứu XAI phát triển thuật toán giải   thích; chuyên gia tư vấn áp dụng XAI trong lĩnh vực nhạy cảm (tài chính, y tế) |

&nbsp;&nbsp;&nbsp;Việc chọn lĩnh vực phù hợp phụ thuộc vào sở thích, kỹ năng và mục tiêu của bạn. Nếu yêu thích sáng tạo và ngôn ngữ, hãy chọn NLP hoặc Generative AI; nếu đam mê hình ảnh và ứng dụng thực tế, Computer Vision là lựa chọn tốt. Người thích xây dựng hệ thống ổn định có thể hướng tới MLOps hoặc Robotics. 




## 7. Bài Blog của tôi đã chia sẻ những gì?

&nbsp;&nbsp;&nbsp; Qua bài Blog này tôi hi vọng sẽ giúp ích được cho các quý bạn đọc có thêm góc nhìn mới, phía dưới là checklist để quý bạn đọc đối chiếu với bản thân dựa trên những gì mà tôi đã chia sẻ.

- [ ] Tôi hiểu đại số tuyến tính, xác suất và thống kê cơ bản.
- [ ] Tôi có thể lập trình Python và sử dụng NumPy/pandas.
- [ ] Tôi đã thực hành hồi quy và phân loại bằng scikit‑learn.
- [ ] Tôi đã triển khai mạng nơ‑ron đơn giản với thư viện học sâu.
- [ ] Tôi hiểu sự khác biệt giữa nghiên cứu và sản phẩm, ưu và nhược điểm của từng hướng.
- [ ] Tôi biết các lĩnh vực chuyên sâu, ưu nhược điểm và ví dụ công việc.





## 8. Kết luận



&nbsp;&nbsp;&nbsp; Học AI là hành trình dài và phong phú. Bằng cách hiểu bức tranh tổng quan, xác định con đường (nghiên cứu hay sản phẩm) và chọn lĩnh vực chuyên sâu phù hợp, bạn sẽ tránh cảm giác lạc lối. Hãy bắt đầu với nền tảng vững chắc, thực hành đều đặn, và luôn đặt câu hỏi “Vì sao?” cho mỗi khái niệm. Và luôn kiên trì giữ thói quen học tập đều đặn mỗi ngày tôi nghĩ chỉ trong vòng 1 năm khi nhìn lại thì bạn sẽ thấy sự khác biệt của bản thân, Còn để làm sao mà biết là mình thực sự thích một lĩnh vực nào đấy hay không thì bạn phải join vào và "LÀM THỬ" mình nghĩ là cách tốt nhất. Bản thân mình cũng không phải dân gốc IT và mình hiện đang học trái nghành trái 360 độ luôn nhưng mình vẫn đang đang đi trên con đường này và mình tin chỉ cần bạn kiên trì theo đuổi thì cuối cùng bạn cũng sẽ đạt được nó!








---

________________________________________
## Tài Liệu Tham Khảo
[1] [What is Artificial Intelligence? - NASA](https://www.nasa.gov/what-is-artificial-intelligence/)
[2] [Machine learning, explained | MIT Sloan](https://mitsloan.mit.edu/ideas-made-to-matter/machine-learning-explained)
[3] [Explained: Neural networks | MIT News | Massachusetts Institute of Technology](https://news.mit.edu/2017/explained-neural-networks-deep-learning-0414)
[4] [Transformer Explainer: LLM Transformer Model Visually Explained](https://poloclub.github.io/transformer-explainer/)
[5] [What is ChatGPT, DALL-E, and generative AI? | McKinsey](https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-generative-ai)
[6] [What Is Linear Regression? | Master's in Data Science](https://www.mastersindatascience.org/learning/machine-learning-algorithms/linear-regression/)
[7] [1.6. Nearest Neighbors — scikit-learn 1.8.0 documentation](https://scikit-learn.org/stable/modules/neighbors.html)
[8] [1.10. Decision Trees — scikit-learn 1.8.0 documentation](https://scikit-learn.org/stable/modules/tree.html)
[9] [1.11. Ensembles: Gradient boosting, random forests, bagging, voting, stacking — scikit-learn 1.8.0 documentation](https://scikit-learn.org/stable/modules/ensemble.html)
[10] [CNN Explainer](https://poloclub.github.io/cnn-explainer/)
[11] [Working with RNNs  |  TensorFlow Core](https://www.tensorflow.org/guide/keras/working_with_rnns)
[12] [What Is Model Deployment in Machine Learning? | Built In](https://builtin.com/machine-learning/model-deployment)
[13] [What is Machine Learning Operations (MLOps)? | NVIDIA Glossary](https://www.nvidia.com/en-us/glossary/mlops/)
[14] [AI Experiments vs AI Products: From Prototype to Production](https://codingcops.com/difference-between-ai-experiments-and-ai-products/)
[15] [Artificial intelligence in healthcare and medicine: clinical applications, therapeutic advances, and future perspectives - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12455834/)
