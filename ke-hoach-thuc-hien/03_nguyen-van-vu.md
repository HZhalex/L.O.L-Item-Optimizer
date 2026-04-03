# Kế Hoạch Thực Hiện — Nguyễn Văn Vũ

**Vai trò:** Nghiên cứu, cài đặt code và viết tài liệu báo cáo cho thuật toán Rabin-Karp; phụ trách nửa sau slide thuyết trình

---

## 1. Tổng Quan Nhiệm Vụ

Nguyễn Văn Vũ phụ trách thuật toán Rabin-Karp và phần slide cuối của nhóm:

1. Nghiên cứu và cài đặt Rabin-Karp, tập trung vào cơ chế hash trượt.
2. Viết tài liệu báo cáo cho Rabin-Karp.
3. Thiết kế nửa sau bộ slide thuyết trình (slide 13-24).

---

## 2. Nội Dung Công Việc Chi Tiết

### 2.1 Cài đặt thuật toán Rabin-Karp

**Mục tiêu:** so khớp chuỗi bằng hash để hỗ trợ phát hiện nhiều đoạn trùng lặp trong văn bản.

**Việc cần làm cụ thể:**

- Xây dựng hàm hash cho pattern và từng cửa sổ của text.
- Cài đặt rolling hash để cập nhật nhanh khi cửa sổ dịch chuyển.
- Xử lý va chạm hash bằng bước so sánh chuỗi thật khi hash trùng.
- Trả về danh sách vị trí match và số lần kiểm tra hợp lệ.

**Yêu cầu kỹ thuật:**

- Chọn base và modulo hợp lý để giảm va chạm.
- Hỗ trợ nhiều file văn bản trong một corpus.

### 2.2 Viết tài liệu báo cáo cho Rabin-Karp

**Nội dung cần có:**

- Giới thiệu ý tưởng dùng hash trượt.
- Mô tả ưu điểm khi cần kiểm tra trên nhiều văn bản.
- Phân tích độ phức tạp trung bình và trường hợp xấu nhất.
- Giải thích cách xử lý va chạm hash và vai trò của bước xác minh lại.
- So sánh Rabin-Karp với Naive, KMP và Boyer-Moore.

### 2.3 Thiết kế nửa sau slide thuyết trình

**Slide 13-24 đề xuất:**

1. Slide 13: Giới thiệu Rabin-Karp.
2. Slide 14: Cơ chế hash trượt.
3. Slide 15: Ví dụ minh họa rolling hash.
4. Slide 16: Xử lý va chạm hash.
5. Slide 17: Kết quả chạy trên bộ test nhỏ.
6. Slide 18: Kết quả chạy trên kho dữ liệu lớn.
7. Slide 19: So sánh Rabin-Karp với Naive và KMP.
8. Slide 20: So sánh Rabin-Karp với Boyer-Moore.
9. Slide 21: Biểu đồ thời gian thực nghiệm.
10. Slide 22: Biểu đồ tỷ lệ match/phát hiện đạo văn.
11. Slide 23: Hạn chế và hướng tối ưu.
12. Slide 24: Kết luận và chuyển sang Q&A.

**Quy tắc trình bày slide:**

- Mỗi slide một ý chính.
- Ít chữ, nhiều hình minh họa.
- Dùng thống nhất font và màu với nửa đầu slide của Hoàng Văn Hưng.

---

## 3. Timeline (Tuần 4 đến Tuần 8)

| Tuần | Công việc | Đầu ra cụ thể |
|---|---|---|
| Tuần 4 | Nghiên cứu Rabin-Karp và xác định base/hash | Dàn ý thuật toán và slide |
| Tuần 5 | Cài đặt hash trượt và hàm search | File code Rabin-Karp chạy được |
| Tuần 6 | Viết doc báo cáo cho Rabin-Karp | Mục Rabin-Karp trong báo cáo |
| Tuần 7 | Thiết kế slide 13-24 | Bộ slide nửa sau hoàn chỉnh |
| Tuần 8 | Rà soát, tối ưu trình bày, chốt demo | Slide và code sẵn sàng nộp |

---

## 4. Phối Hợp

- Phối hợp với Lê Thiên Lộc để tích hợp thuật toán vào giao diện chung.
- Phối hợp với Đỗ Đình Chiến để so sánh Rabin-Karp với Naive/KMP.
- Phối hợp với Huỳnh Gia Huy để lấy dữ liệu benchmark và file test.
- Phối hợp với Nguyễn Thái Lộc để đưa số liệu thực nghiệm vào báo cáo và biểu đồ.
