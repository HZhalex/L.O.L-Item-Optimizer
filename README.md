# Hệ Thống Phát Hiện Đạo Văn bằng String Matching

## 1. Giới thiệu dự án

Dự án xây dựng một hệ thống phát hiện đạo văn dựa trên bài toán **String Matching** trong Python. Chương trình cho phép người dùng tải lên văn bản nguồn hoặc một kho tài liệu tham chiếu, sau đó so khớp nội dung để phát hiện các đoạn trùng lặp, đánh dấu vị trí khớp, và thống kê tỷ lệ tương đồng giữa các văn bản.

Mục tiêu của dự án là tạo ra một công cụ có thể:

- phát hiện nhanh các đoạn text có dấu hiệu sao chép;
- so sánh hiệu năng của nhiều thuật toán string matching;
- hiển thị rõ các đoạn nghi vấn bằng highlight trực quan;
- tổng hợp kết quả thực nghiệm để phục vụ báo cáo môn học **Phân tích Thiết kế Giải thuật**.

---

## 2. Bài toán trong ngữ cảnh phát hiện đạo văn

Trong hệ thống này, bài toán được ánh xạ như sau:

- **Pattern**: đoạn văn hoặc câu cần kiểm tra.
- **Text**: văn bản nguồn hoặc văn bản nghi vấn.
- **Corpus**: tập hợp nhiều file tài liệu dùng làm kho so sánh.
- **Match position**: vị trí xuất hiện của chuỗi khớp trong văn bản.
- **Similarity rate**: tỷ lệ trùng lặp giữa tài liệu nghi vấn và kho dữ liệu.

**Mục tiêu:** xác định chính xác đoạn nội dung bị trùng, làm nổi bật phần khớp, và cung cấp số liệu đo lường để đánh giá mức độ tương đồng.

---

## 3. Bốn thuật toán áp dụng

### 3.1 Brute-Force (Naive)

Thuật toán duyệt lần lượt từng vị trí trong văn bản và so sánh từng ký tự của pattern với text.

**Ưu điểm:** dễ cài đặt, dễ kiểm tra đúng sai, phù hợp làm baseline.

**Nhược điểm:** chậm khi dữ liệu lớn vì có nhiều phép so sánh lặp lại.

**Độ phức tạp:** worst-case $O(nm)$ với $n$ là độ dài text và $m$ là độ dài pattern.

### 3.2 KMP (Knuth-Morris-Pratt)

KMP xây dựng bảng tiền tố/hậu tố để tránh quay lại so sánh từ đầu khi xảy ra mismatch.

**Ưu điểm:** chạy tuyến tính, ổn định với dữ liệu lớn.

**Nhược điểm:** phần tiền xử lý phức tạp hơn Naive.

**Độ phức tạp:** $O(n + m)$.

### 3.3 Rabin-Karp

Rabin-Karp dùng hash trượt để so sánh cửa sổ văn bản với pattern.

**Ưu điểm:** phù hợp khi cần kiểm tra nhiều đoạn hoặc nhiều pattern; rất hiệu quả nếu hash tốt.

**Nhược điểm:** có thể gặp va chạm hash, cần xử lý xác minh lại bằng so sánh chuỗi thật.

**Độ phức tạp:** trung bình gần $O(n + m)$, xấu nhất có thể về $O(nm)$ nếu va chạm nhiều.

### 3.4 Boyer-Moore

Boyer-Moore so sánh từ phải sang trái và dùng hai heuristic chính: bad character và good suffix.

**Ưu điểm:** thường rất nhanh trong thực tế, đặc biệt với văn bản dài.

**Nhược điểm:** cài đặt phức tạp hơn các thuật toán còn lại.

**Độ phức tạp:** thực tế thường tốt hơn tuyến tính, worst-case vẫn có thể cao.

---

## 4. Tính năng của hệ thống

1. Upload file văn bản đầu vào và kho tài liệu tham chiếu.
2. Chọn một hoặc nhiều thuật toán để so sánh.
3. Tô sáng đoạn text bị trùng trong giao diện.
4. Hiển thị vị trí match, số lần match, tỷ lệ tương đồng và thời gian chạy.
5. Xuất báo cáo thực nghiệm và biểu đồ so sánh hiệu năng.

---

## 5. Công nghệ sử dụng

- **Ngôn ngữ:** Python 3.x
- **Giao diện:** Tkinter hoặc PyQt
- **Xử lý dữ liệu:** đọc file text, chuẩn hóa nội dung, so khớp chuỗi
- **Trực quan hóa:** matplotlib

---

## 6. Cấu trúc dự án hiện tại

```text
plagiarism-detection/
├── .gitignore                   # Loại trừ file tạm, cache, môi trường ảo
├── main.py
├── README.md                    # Tài liệu tổng quan dự án
├── requirements.txt             # Danh sách thư viện cần cài
├── algorithms/
│   ├── __init__.py              # Xuất API chung cho 4 thuật toán
│   ├── brute_force.py           # Thuật toán Brute-Force
│   ├── kmp.py                   # Thuật toán KMP
│   ├── rabin_karp.py            # Thuật toán Rabin-Karp
│   └── boyer_moore.py           # Thuật toán Boyer-Moore
├── ui/
│   ├── __init__.py              # Khởi tạo package giao diện
│   ├── main_window.py           # Cửa sổ chính: upload, compare, rank, export
│   └── result_view.py           # Định dạng chuỗi hiển thị kết quả
├── utils/
│   ├── __init__.py              # Khởi tạo package tiện ích
│   ├── file_loader.py           # Đọc file text, liệt kê file trong thư mục
│   ├── text_normalizer.py       # Chuẩn hóa chữ thường và khoảng trắng
│   └── timer.py                 # Đo thời gian thực thi
├── models/
│   ├── __init__.py              # Package mô hình dữ liệu
│   └── match_result.py          # Cấu trúc kết quả match
├── data/
│   ├── corpus/                  # Kho văn bản gốc tham chiếu
│   ├── corpus_grouped/          # Kho văn bản đã phân nhóm theo size
│   │   ├── small/
│   │   ├── medium/
│   │   └── large/
│   ├── test_cases/              # Bộ test đạo văn theo từng kịch bản
│   │   ├── exact/
│   │   ├── partial/
│   │   ├── noise/
│   │   ├── clean/
│   │   └── paraphrase/
│   ├── results/                 # Kết quả benchmark xuất ra CSV/JSON
│   └── metadata.json            # Metadata cho corpus
├── scripts/
│   ├── benchmark.py             # Chạy đo thời gian và tỷ lệ trùng lặp
│   ├── crawl_wiki.py            # Crawl dữ liệu Wikipedia về corpus
│   ├── generate_testcase.py     # Tạo test case đạo văn
│   └── phanloai_corpus.py       # Phân loại corpus theo kích thước
├── report/
│   ├── bao-cao-mau.md           # Khung báo cáo mẫu
│   └── outline-slide-nhom.md    # Dàn ý slide thuyết trình
└── ke-hoach-thuc-hien/          # File giao việc và tiến độ từng thành viên
	├── 01_le-thien-loc.md
	├── 02_do-dinh-chien.md
	├── 03_nguyen-van-vu.md
	├── 04_nguyen-thai-loc.md
	├── 05_huynh-gia-huy.md
	└── 06_hoang-van-hung.md
```

### 6.1 Overview nhanh

- `main.py` là điểm khởi chạy duy nhất của ứng dụng.
- `algorithms/` chứa 4 thuật toán string matching dùng để so sánh hiệu năng và phát hiện trùng lặp.
- `ui/` chứa toàn bộ giao diện Tkinter, bao gồm màn hình chính và phần hiển thị kết quả.
- `utils/` gom các hàm dùng chung như đọc file, chuẩn hóa text, đo thời gian.
- `models/` giữ các cấu trúc dữ liệu kết quả để thống nhất đầu ra giữa các module.
- `data/` là nơi đặt corpus, test case, kết quả thực nghiệm và metadata.
- `scripts/` là các script hỗ trợ crawl dữ liệu, tạo test, phân loại corpus, benchmark.
- `report/` chứa khung báo cáo và dàn ý slide.
- `ke-hoach-thuc-hien/` lưu kế hoạch và phân công từng thành viên trong nhóm.

---

## 7. Hướng dẫn cài đặt và chạy

1. Cài Python 3.x.
2. Cài các thư viện cần thiết:

```bash
pip install matplotlib
```

3. Chạy chương trình:

```bash
python main.py
```

4. Tải file văn bản và chọn thuật toán để phân tích.

---

## 8. Thành viên nhóm

| STT | Họ và tên | Nhiệm vụ chính |
|---|---|---|
| 1 | Lê Thiên Lộc | Thiết kế kiến trúc tổng thể, quản lý Git, thiết kế UI/UX bằng Tkinter/PyQt, tích hợp highlight đoạn đạo văn. Nghiên cứu, cài đặt và viết doc cho Brute-Force |
| 2 | Đỗ Đình Chiến | Nghiên cứu, cài đặt và viết doc cho KMP |
| 3 | Nguyễn Văn Vũ | Nghiên cứu, cài đặt và viết doc cho Rabin-Karp, phụ trách nửa sau slide thuyết trình |
| 4 | Nguyễn Thái Lộc | Viết báo cáo phân tích độ phức tạp, so sánh 4 thuật toán, vẽ biểu đồ thực nghiệm |
| 5 | Huỳnh Gia Huy | Xây dựng bộ dữ liệu test, crawl/tổng hợp kho text, viết script đo thời gian và tỷ lệ trùng lặp |
| 6 | Hoàng Văn Hưng | Nghiên cứu, cài đặt và viết doc cho Boyer-Moore, thiết kế nửa đầu slide thuyết trình |

---

## 9. Mục tiêu đầu ra

- Một hệ thống phát hiện đạo văn chạy được trên Python.
- 4 thuật toán string matching được cài đặt rõ ràng và so sánh được.
- Bộ dữ liệu test phong phú và có script đo lường.
- Báo cáo và slide thuyết trình đầy đủ, chuyên nghiệp.
