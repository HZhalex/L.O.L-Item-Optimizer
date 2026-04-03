# Báo Cáo Mẫu - Hệ Thống Phát Hiện Đạo Văn (String Matching)

## 1. Giới thiệu
- Bối cảnh và lý do chọn đề tài.
- Mục tiêu của hệ thống.
- Phạm vi và giới hạn của nghiên cứu.

## 2. Mô hình bài toán
- Ánh xạ bài toán phát hiện đạo văn về string matching.
- Định nghĩa Pattern, Text, Corpus, Match Position.
- Tiêu chí đánh giá: thời gian, độ chính xác, tỷ lệ trùng lặp.

## 3. Kiến trúc hệ thống
- Sơ đồ tổng quan module: UI, Algorithms, Utils, Data, Report.
- Luồng xử lý từ upload file đến xuất kết quả.
- Cấu trúc dữ liệu đầu vào/đầu ra.

## 4. Cài đặt các thuật toán
### 4.1 Brute-Force (Naive)
- Ý tưởng, pseudocode, độ phức tạp.
### 4.2 KMP
- Ý tưởng bảng LPS, pseudocode, độ phức tạp.
### 4.3 Rabin-Karp
- Ý tưởng rolling hash, va chạm hash, độ phức tạp.
### 4.4 Boyer-Moore
- Heuristic bad character/good suffix, độ phức tạp.

## 5. Dữ liệu thực nghiệm
- Nguồn dữ liệu corpus và cách xây dựng test case.
- Các kịch bản test: copy nguyên văn, copy một phần, không trùng.
- Môi trường chạy: CPU, RAM, Python version.

## 6. Kết quả và phân tích
- Bảng thời gian chạy trung bình theo thuật toán.
- Biểu đồ so sánh thời gian.
- Biểu đồ tỷ lệ trùng lặp phát hiện được.
- Nhận xét ưu/nhược theo từng tình huống dữ liệu.

## 7. Kết luận và hướng phát triển
- Kết luận chính của nhóm.
- Thuật toán phù hợp cho từng nhu cầu thực tế.
- Hướng cải tiến: semantic plagiarism, NLP embedding, tối ưu UI.

## 8. Phân công thành viên
- Tóm tắt trách nhiệm và đóng góp của từng người.
