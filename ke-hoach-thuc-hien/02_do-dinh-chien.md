# Kế Hoạch Thực Hiện — Đỗ Đình Chiến

**Vai trò:** Nghiên cứu, cài đặt code và viết tài liệu báo cáo cho 2 thuật toán: Brute-Force (Naive) và KMP

---

## 1. Tổng Quan Nhiệm Vụ

Đỗ Đình Chiến phụ trách hai thuật toán nền tảng của dự án:

1. Thuật toán Vét cạn (Brute-Force / Naive).
2. Thuật toán KMP (Knuth-Morris-Pratt).

Ngoài phần code, Chiến còn phải viết tài liệu giải thích nguyên lý, minh họa cách chạy và phân tích độ phức tạp của hai thuật toán này.

---

## 2. Nội Dung Công Việc Chi Tiết

### 2.1 Cài đặt thuật toán Brute-Force

**Mục tiêu:** tạo một baseline đơn giản để so sánh với các thuật toán còn lại.

**Việc cần làm cụ thể:**

- Viết hàm so khớp chuỗi theo kiểu duyệt từng vị trí của text.
- Ở mỗi vị trí, so sánh lần lượt các ký tự của pattern.
- Trả về danh sách vị trí match.
- Hỗ trợ trường hợp nhiều match trong cùng một văn bản.

**Kết quả mong đợi:**

- Code dễ đọc, dễ kiểm tra, phù hợp làm thuật toán tham chiếu.
- Có thể tính thời gian chạy và số phép so sánh để phục vụ báo cáo.

### 2.2 Cài đặt thuật toán KMP

**Mục tiêu:** giảm số lần so sánh dư thừa bằng bảng tiền xử lý prefix.

**Việc cần làm cụ thể:**

- Xây dựng bảng prefix function / LPS.
- Viết vòng lặp so khớp chính với cơ chế quay lui bằng LPS.
- Trả về tất cả vị trí pattern xuất hiện trong text.
- Đảm bảo thuật toán chạy đúng với nhiều kiểu dữ liệu: đoạn ngắn, đoạn dài, văn bản lặp lại nhiều.

**Yêu cầu kỹ thuật:**

- Tách rõ phần tiền xử lý và phần tìm kiếm.
- Có test case riêng cho LPS và cho search.

### 2.3 Viết tài liệu báo cáo cho Brute-Force và KMP

**Nội dung báo cáo cần có:**

- Mô tả ý tưởng của Brute-Force và KMP.
- So sánh vì sao KMP hiệu quả hơn Naive trên văn bản dài.
- Phân tích độ phức tạp thời gian và không gian.
- Có ví dụ minh họa từng bước để người đọc dễ hiểu.
- Nêu hạn chế và tình huống phù hợp của mỗi thuật toán.

**Đầu ra tài liệu:**

- 1 chương hoặc 2 mục riêng biệt trong báo cáo chính.
- Có bảng so sánh, có hình minh họa nếu cần.

### 2.4 Kiểm thử

**Các test cần chuẩn bị:**

- Pattern xuất hiện ở đầu, giữa, cuối text.
- Pattern không xuất hiện.
- Pattern lặp nhiều lần.
- Text ngắn hơn pattern.

---

## 3. Timeline (Tuần 4 đến Tuần 8)

| Tuần | Công việc | Đầu ra cụ thể |
|---|---|---|
| Tuần 4 | Nghiên cứu lý thuyết Naive và KMP | Dàn ý code và dàn ý báo cáo |
| Tuần 5 | Cài đặt Brute-Force hoàn chỉnh | File code Naive chạy được |
| Tuần 6 | Cài đặt KMP và bảng LPS | File code KMP chạy đúng |
| Tuần 7 | Viết tài liệu báo cáo và test case | Chương báo cáo Naive + KMP |
| Tuần 8 | Rà soát, sửa lỗi, chốt nội dung | Bộ code và tài liệu sẵn sàng nộp |

---

## 4. Phối Hợp

- Phối hợp với Lê Thiên Lộc để thống nhất API trả về kết quả match.
- Phối hợp với Nguyễn Văn Vũ để so sánh Brute-Force/KMP với Rabin-Karp trên cùng bộ test.
- Phối hợp với Huỳnh Gia Huy để lấy dữ liệu văn bản và test case đa dạng.
- Phối hợp với Nguyễn Thái Lộc để thống nhất phần đánh giá độ phức tạp trong báo cáo.
