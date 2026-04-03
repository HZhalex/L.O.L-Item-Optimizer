# Kế Hoạch Thực Hiện — Huỳnh Gia Huy

**Vai trò:** Xây dựng bộ dữ liệu test, crawl/tổng hợp hàng ngàn file text làm kho dữ liệu mẫu, tạo file test đạo văn, viết script đo thời gian chạy và tỷ lệ trùng lặp

---

## 1. Tổng Quan Nhiệm Vụ

Huỳnh Gia Huy phụ trách toàn bộ mảng dữ liệu và đo lường của dự án. Công việc chính gồm:

1. Thu thập và tổng hợp kho văn bản mẫu quy mô lớn.
2. Tạo các bộ test đạo văn phục vụ kiểm thử chức năng và hiệu năng.
3. Viết script benchmark để đo thời gian chạy và tỷ lệ trùng lặp.

---

## 2. Nội Dung Công Việc Chi Tiết

### 2.1 Xây dựng kho dữ liệu text

**Yêu cầu cụ thể:**

- Crawl hoặc tổng hợp hàng ngàn file text từ nguồn phù hợp.
- Phân nhóm dữ liệu theo kích thước, chủ đề hoặc mức độ tương đồng.
- Làm sạch văn bản: chuẩn hóa encoding, khoảng trắng, xuống dòng và ký tự đặc biệt.

**Đầu ra bàn giao:**

- Một thư mục corpus có cấu trúc rõ ràng.
- Danh sách nguồn dữ liệu và nhãn sử dụng.

### 2.2 Tạo file test đạo văn

**Các loại test cần có:**

1. Test sao chép nguyên văn.
2. Test sao chép một phần.
3. Test chèn thêm hoặc xóa bớt ký tự nhẹ.
4. Test văn bản sạch để đo false positive.

**Mục đích:**

- Đảm bảo hệ thống được kiểm tra cả về tốc độ lẫn độ chính xác.
- Tạo ra các tình huống có thể kiểm chứng bằng tay nếu cần.

### 2.3 Viết script đo thời gian chạy và tỷ lệ trùng lặp

**Script cần thực hiện:**

- Đọc dữ liệu text và file test.
- Chạy lần lượt 4 thuật toán trên cùng input.
- Ghi thời gian bằng `time.perf_counter()`.
- Đếm số vị trí match và tính tỷ lệ trùng lặp.
- Xuất kết quả ra `csv` hoặc `json` để Nguyễn Thái Lộc dùng vẽ biểu đồ.

**Đầu ra bắt buộc:**

- Một script benchmark tự động chạy được.
- File kết quả thực nghiệm có cấu trúc rõ ràng.

### 2.4 Hỗ trợ kiểm thử tích hợp

- Cung cấp dataset cho Lê Thiên Lộc test UI.
- Cung cấp test case cho Chiến, Vũ và Hưng kiểm thử thuật toán.
- Cập nhật lại corpus khi phát hiện dữ liệu lỗi hoặc trùng bất thường.

---

## 3. Timeline (Tuần 4 đến Tuần 8)

| Tuần | Công việc | Đầu ra cụ thể |
|---|---|---|
| Tuần 4 | Xác định nguồn dữ liệu và cách lưu trữ corpus | Cấu trúc dữ liệu và quy tắc đặt tên |
| Tuần 5 | Crawl/tổng hợp và làm sạch văn bản | Kho dữ liệu mẫu đã chuẩn hóa |
| Tuần 6 | Tạo bộ test đạo văn có chủ đích | Bộ file test hoàn chỉnh |
| Tuần 7 | Viết script đo thời gian và tỷ lệ trùng lặp | Script benchmark + file kết quả |
| Tuần 8 | Kiểm tra lại toàn bộ dataset và benchmark | Bộ dữ liệu sẵn sàng cho báo cáo |

---

## 4. Phối Hợp

- Phối hợp với Lê Thiên Lộc để test chức năng upload và highlight trong UI.
- Phối hợp với Đỗ Đình Chiến, Nguyễn Văn Vũ và Hoàng Văn Hưng để có bộ test dùng chung cho 4 thuật toán.
- Phối hợp với Nguyễn Thái Lộc để cung cấp số liệu thực nghiệm phục vụ biểu đồ và báo cáo.
