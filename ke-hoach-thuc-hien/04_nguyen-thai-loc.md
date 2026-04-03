# Kế Hoạch Thực Hiện — Nguyễn Thái Lộc

**Vai trò:** Phụ trách học thuật, viết báo cáo phân tích độ phức tạp, so sánh 4 thuật toán, vẽ biểu đồ thực nghiệm

---

## 1. Tổng Quan Nhiệm Vụ

Nguyễn Thái Lộc là người phụ trách phần học thuật và đánh giá định lượng của dự án. Công việc gồm:

1. Viết toàn bộ phần phân tích độ phức tạp của 4 thuật toán string matching.
2. So sánh hiệu năng lý thuyết và thực nghiệm giữa Brute-Force, KMP, Rabin-Karp và Boyer-Moore.
3. Vẽ biểu đồ, bảng số liệu và kết luận học thuật cho báo cáo.

---

## 2. Nội Dung Công Việc Chi Tiết

### 2.1 Viết phần phân tích lý thuyết

**Nội dung cần có trong báo cáo:**

- Trình bày bài toán phát hiện đạo văn dưới góc nhìn String Matching.
- Mô tả vai trò của pattern, text và corpus.
- Giải thích nguyên lý của 4 thuật toán ở mức học thuật.
- Phân tích độ phức tạp thời gian và không gian của từng thuật toán.

**Các ý cần nhấn mạnh:**

- Brute-Force là baseline, dễ hiểu nhưng chậm.
- KMP ổn định vì có tiền xử lý prefix.
- Rabin-Karp mạnh ở hash và kiểm tra nhiều văn bản.
- Boyer-Moore thường rất nhanh trong thực tế nhờ dịch chuyển thông minh.

### 2.2 So sánh độ phức tạp và hiệu năng

**Việc cần làm cụ thể:**

- Lập bảng so sánh thời gian, bộ nhớ và độ phù hợp của từng thuật toán.
- Giải thích trường hợp tốt, trung bình và xấu nếu cần.
- Viết nhận xét vì sao không thể chọn một thuật toán duy nhất cho mọi loại dữ liệu.
- Nêu rõ thuật toán nào phù hợp với văn bản ngắn, văn bản dài, hoặc nhiều file.

### 2.3 Vẽ biểu đồ thực nghiệm

**Biểu đồ cần chuẩn bị:**

1. Biểu đồ cột thời gian chạy trung bình của 4 thuật toán.
2. Biểu đồ cột tỷ lệ trùng lặp phát hiện được.
3. Biểu đồ so sánh theo kích thước dữ liệu nếu bộ số liệu đủ lớn.

**Nguồn dữ liệu:**

- Script benchmark do Huỳnh Gia Huy cung cấp.
- Kết quả chạy thuật toán từ Chiến, Vũ và Hưng.

### 2.4 Kết luận học thuật

**Phần kết luận cần viết:**

- Thuật toán nào nhanh nhất trong thực nghiệm.
- Thuật toán nào dễ cài đặt và dễ giải thích nhất.
- Thuật toán nào phù hợp cho dữ liệu lớn.
- Nhận xét tổng quát về tính ứng dụng của String Matching trong phát hiện đạo văn.

---

## 3. Timeline (Tuần 4 đến Tuần 8)

| Tuần | Công việc | Đầu ra cụ thể |
|---|---|---|
| Tuần 4 | Chốt dàn ý báo cáo học thuật và tiêu chí đo lường | Mục lục phần phân tích hoàn chỉnh |
| Tuần 5 | Viết lý thuyết và công thức độ phức tạp | Bản nháp phần phân tích thuật toán |
| Tuần 6 | Tổng hợp số liệu thực nghiệm | Bảng dữ liệu và nhận xét sơ bộ |
| Tuần 7 | Vẽ biểu đồ và hoàn thiện so sánh | Biểu đồ, bảng, nhận xét hoàn chỉnh |
| Tuần 8 | Rà soát và chốt báo cáo học thuật cuối | Chương phân tích sẵn sàng nộp |

---

## 4. Phối Hợp

- Phối hợp với Huỳnh Gia Huy để nhận số liệu benchmark và dữ liệu test.
- Phối hợp với Lê Thiên Lộc để thống nhất cách trình bày trong báo cáo và README.
- Phối hợp với Đỗ Đình Chiến, Nguyễn Văn Vũ và Hoàng Văn Hưng để lấy mô tả thuật toán và kết quả thực nghiệm.
