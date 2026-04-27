# Kế Hoạch Thực Hiện — Lê Thiên Lộc

**Vai trò:** Thiết kế kiến trúc tổng thể, Quản lý Git, Thiết kế UI/UX bằng Tkinter/PyQt, tích hợp highlight đoạn text nghi vấn đạo văn

---

## 1. Tổng Quan Nhiệm Vụ

Lê Thiên Lộc là người phụ trách nền tảng kỹ thuật và trải nghiệm người dùng của dự án. Công việc chính gồm:

1. Thiết kế kiến trúc tổng thể của hệ thống phát hiện đạo văn.
2. Chuẩn hóa cấu trúc module và luồng dữ liệu giữa giao diện, thuật toán và dữ liệu.
3. Thiết kế giao diện upload file, hiển thị kết quả, và highlight đoạn text bị trùng.
4. Quản lý Git, nhánh phát triển và quy trình merge của nhóm.

---

## 2. Nội Dung Công Việc Chi Tiết

### 2.1 Thiết kế kiến trúc phần mềm

**Mục tiêu:** tạo ra một cấu trúc dự án rõ ràng, dễ mở rộng và dễ tích hợp 4 thuật toán string matching.

**Việc cần làm cụ thể:**

- Chốt cấu trúc thư mục: `algorithms`, `ui`, `utils`, `data`, `reports`.
- Định nghĩa chuẩn đầu vào/đầu ra cho các thuật toán:
  - input: `pattern`, `text`, hoặc danh sách file trong corpus
  - output: vị trí match, số lần match, tỷ lệ trùng lặp, thời gian chạy
- Tạo luồng xử lý thống nhất:
  - upload file
  - tiền xử lý text
  - chạy thuật toán
  - tổng hợp kết quả
  - highlight đoạn khớp
- Xác định các hàm dùng chung như normalize text, đọc file, đo thời gian, xuất báo cáo.

### 2.2 Thiết kế UI/UX

**Mục tiêu:** giao diện phải trực quan, dễ dùng, có thể nạp dữ liệu và hiển thị kết quả đạo văn rõ ràng.

**Các màn hình cần thiết kế:**

- Cửa sổ chính để chọn file văn bản và kho dữ liệu.
- Khu vực preview văn bản gốc.
- Khu vực hiển thị đoạn match được highlight.
- Panel thống kê: số lần match, phần trăm trùng lặp, thời gian chạy.
- Khu vực chọn thuật toán để so sánh.

**Đầu việc kỹ thuật:**

- Thiết kế layout bằng Tkinter hoặc PyQt.
- Làm nút `Upload File`, `Run Analysis`, `Compare Algorithms`, `Export Result`.
- Bổ sung scrollbar, khung preview dài, và hiển thị màu cho các đoạn khớp.
- Đảm bảo giao diện không bị rối khi văn bản dài.

### 2.3 Quản lý Git và quy trình phát triển

**Mục tiêu:** đảm bảo các thành viên code song song nhưng vẫn merge ổn định.

**Việc cần làm:**

- Tạo nhánh chính và nhánh feature cho từng module.
- Quy định commit message rõ ràng theo module.
- Review PR trước khi merge.
- Kiểm tra xung đột giữa UI, thuật toán và dữ liệu test.

### 2.4 Tích hợp và kiểm thử giao diện

**Mục tiêu:** bảo đảm UI gọi được đúng các thuật toán và hiển thị đúng kết quả.

**Phối hợp tích hợp:**

- Gọi module Naive/KMP/Rabin-Karp/Boyer-Moore theo API thống nhất.
- Nhận dữ liệu vị trí match từ các thuật toán để highlight trên màn hình.
- Hiển thị đúng từng file văn bản và thống kê tương đồng.
- Kiểm tra độ ổn định khi nạp nhiều file lớn.

---

## 3. Timeline (Tuần 4 đến Tuần 8)

| Tuần | Công việc | Đầu ra cụ thể |
|---|---|---|
| Tuần 4 | Chốt kiến trúc hệ thống và chuẩn API | Sơ đồ module, danh sách hàm chung |
| Tuần 5 | Thiết kế layout UI/UX và prototype màn hình chính | Bản thiết kế giao diện đầu tiên |
| Tuần 6 | Cài đặt khung giao diện, upload file, preview text | UI có thể nạp file và hiển thị nội dung |
| Tuần 7 | Tích hợp highlight kết quả và khung so sánh thuật toán | Màn hình kết quả rõ ràng, dễ quan sát |
| Tuần 8 | Review code, sửa lỗi giao diện, chuẩn bị demo | UI ổn định và sẵn sàng trình bày |

---

## 4. Phối Hợp

- Phối hợp với Đỗ Đình Chiến và Nguyễn Văn Vũ để thống nhất dạng output của từng thuật toán.
- Phối hợp với Huỳnh Gia Huy để kiểm thử giao diện bằng dữ liệu thật.
- Phối hợp với Nguyễn Thái Lộc để đảm bảo UI hiển thị đúng số liệu thực nghiệm và biểu đồ.
- Phối hợp với Hoàng Văn Hưng để thống nhất phần trình bày slide đầu và ngữ cảnh thuật toán.

---

## 5. Cập Nhật Trạng Thái Thực Tế (Đối Chiếu Repo)

**Ngày cập nhật:** 27/04/2026

### 5.1 Tổng kết nhanh

- Trạng thái chung: **Đã hoàn thành bộ chức năng chính theo phạm vi giao việc**.
- Đã có khung hệ thống, UI hoàn chỉnh cho demo, compare, export và xếp hạng corpus.
- Việc còn lại chủ yếu là tăng độ ổn định và bổ sung kiểm thử tích hợp.

### 5.2 Checklist theo đầu việc của Lê Thiên Lộc

| Hạng mục | Trạng thái | Ghi chú |
|---|---|---|
| Chốt cấu trúc thư mục dự án | Đã hoàn thành | Có `algorithms`, `ui`, `utils`, `data`, `report` |
| Luồng xử lý cơ bản (upload -> normalize -> search -> highlight) | Đã hoàn thành một phần | Đã có trong `ui/main_window.py` |
| Chuẩn hóa API thuật toán thống nhất | Đã hoàn thành | `algorithms/kmp.py` đã có `search(pattern, text)` và alias tương thích ngược |
| Hàm dùng chung (đọc file, normalize, timer) | Đã hoàn thành | Có trong `utils/file_loader.py`, `utils/text_normalizer.py`, `utils/timer.py` |
| UI upload + preview text | Đã hoàn thành | Có nút upload và vùng hiển thị text |
| UI highlight đoạn trùng | Đã hoàn thành | Dùng tag `match` trong Text widget |
| Panel thống kê kết quả | Đã hoàn thành cơ bản | Có số match, thời gian, similarity ước lượng |
| Chọn thuật toán để chạy | Đã hoàn thành | Combobox 4 thuật toán |
| Nút `Compare Algorithms` | Đã hoàn thành | Đã chạy so sánh 4 thuật toán trong UI |
| Nút `Export Result` | Đã hoàn thành | Đã hỗ trợ xuất CSV/JSON từ kết quả chạy |
| Scrollbar cho vùng văn bản dài | Đã hoàn thành | Đã thêm thanh cuộn dọc/ngang cho vùng văn bản |
| Tích hợp so sánh theo nhiều file corpus trong UI | Đã hoàn thành | Hỗ trợ chọn nhiều file, chọn thư mục corpus, gộp dữ liệu và loại trùng |
| Quản lý Git/PR theo quy trình nhóm | Chưa đủ bằng chứng | Cần đối chiếu lịch sử nhánh/PR trên GitHub |

### 5.3 Việc Cần Làm Tiếp (Ưu tiên)

1. Viết test tích hợp UI-Algorithm với dữ liệu lớn để xác nhận tính ổn định.
2. Bổ sung bộ test hồi quy cho các luồng compare/rank/export để tránh lỗi khi demo.

### 5.4 Kết luận tiến độ vai trò Lê Thiên Lộc

- Mức hoàn thành hiện tại: **khoảng 95%** so với phạm vi công việc đã mô tả.
- Đã hoàn thiện bộ chức năng chính: upload, chạy thuật toán, compare, highlight, export, xếp hạng top corpus.
- Phần còn lại chủ yếu là củng cố kiểm thử tích hợp và chuẩn hóa quy trình review/PR.
