# Kế Hoạch Thực Hiện — Hoàng Văn Hưng

**Vai trò:** Nghiên cứu, cài đặt code và viết doc báo cáo cho thuật toán Boyer-Moore, thiết kế nửa đầu slide thuyết trình

---

## 1. Tổng Quan Nhiệm Vụ

Hoàng Văn Hưng phụ trách 2 phần chính của dự án:

1. Cài đặt thuật toán Boyer-Moore.
2. Thiết kế nửa đầu bộ slide thuyết trình của nhóm.

---

## 2. Nội Dung Công Việc Chi Tiết

### 2.1 Cài đặt thuật toán Boyer-Moore

**Mục tiêu code:** tận dụng chiến lược so khớp từ phải sang trái để tăng tốc tìm kiếm trong văn bản dài.

**Việc cần làm cụ thể:**

- Xây dựng bảng bad character.
- Xây dựng bảng good suffix.
- Cài đặt cơ chế dịch chuyển sau mismatch.
- Trả về vị trí match, số lần match và thời gian chạy.

**Yêu cầu kỹ thuật:**

- Có xử lý so sánh nhiều vị trí trong corpus.
- Có test case cho pattern ngắn, pattern dài, mismatch đầu và mismatch cuối.

### 2.2 Viết tài liệu báo cáo cho Boyer-Moore

**Nội dung cần viết:**

- Giới thiệu nguyên lý so sánh từ phải sang trái.
- Giải thích bad character heuristic.
- Giải thích good suffix heuristic.
- Phân tích ưu điểm thực tế và giới hạn của thuật toán.
- So sánh Boyer-Moore với Brute-Force, KMP và Rabin-Karp.

### 2.3 Thiết kế nửa đầu slide thuyết trình

**Slide 1-12 đề xuất:**

1. Slide 1: Trang bìa.
2. Slide 2: Mục tiêu đề tài.
3. Slide 3: Bài toán phát hiện đạo văn.
4. Slide 4: Ánh xạ String Matching vào bài toán.
5. Slide 5: Kiến trúc hệ thống tổng quan.
6. Slide 6: Thuật toán Brute-Force.
7. Slide 7: Thuật toán KMP.
8. Slide 8: Thuật toán Boyer-Moore.
9. Slide 9: Minh họa bad character và good suffix.
10. Slide 10: Dữ liệu test và cách đánh giá.
11. Slide 11: Kết quả minh họa ban đầu.
12. Slide 12: Chuyển tiếp sang phần Rabin-Karp và benchmark.

**Quy tắc trình bày:**

- Mỗi slide chỉ tập trung một ý chính.
- Ưu tiên sơ đồ, biểu tượng, hình minh họa thay vì nhiều chữ.
- Thống nhất template với slide phần sau do Nguyễn Văn Vũ phụ trách.

---

## 3. Timeline (Tuần 4 đến Tuần 8)

| Tuần | Công việc | Đầu ra cụ thể |
|---|---|---|
| Tuần 4 | Nghiên cứu Boyer-Moore và chốt outline slide | Dàn ý code và dàn ý trình bày |
| Tuần 5 | Cài đặt Boyer-Moore bản đầu tiên | File code chạy được trên test cơ bản |
| Tuần 6 | Viết doc thuật toán và hoàn thiện test | Mục Boyer-Moore trong báo cáo |
| Tuần 7 | Thiết kế slide 1-12 | Bộ slide nửa đầu hoàn chỉnh |
| Tuần 8 | Rà soát và sửa nội dung slide, code, tài liệu | Bản hoàn thiện để nộp và thuyết trình |

---

## 4. Phối Hợp

- Phối hợp với Đỗ Đình Chiến để thống nhất cách trình bày Naive và KMP trên slide.
- Phối hợp với Nguyễn Văn Vũ để bàn giao phần chuyển tiếp sang slide 13-24.
- Phối hợp với Lê Thiên Lộc để đồng bộ giao diện demo và luồng trình bày hệ thống.
- Phối hợp với Huỳnh Gia Huy và Nguyễn Thái Lộc để chèn test case và số liệu thực nghiệm vào slide.
