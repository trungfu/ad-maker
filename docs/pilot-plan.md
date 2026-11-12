# Kế hoạch pilot SOP v1.0

## 1. Mục tiêu
1. Chạy thử **toàn bộ 9 bước và 3 cổng duyệt** trên một chiến dịch thật, rủi ro thấp.
2. Đo **thời gian và chi phí thực tế** của từng bước để chỉnh SOP và lịch 5 ngày.
3. Giải quyết các mục **chặn** trong danh sách cần xác minh (SOP mục 12).
4. Bắt đầu **thư viện prompt** từ những shot đạt QC.

## 2. Phạm vi

| Hạng mục | Pilot | Ghi chú |
|---|---|---|
| Chiến dịch | Quảng bá **một đường bay** (nội địa, đang khai thác) | Không gắn giá khuyến mãi để giảm tải pháp lý — nếu bắt buộc có giá, Legal duyệt điều kiện ngay Ngày 1 |
| Sản phẩm | **C15-VI**, **C15-EN**, **C06-VI** (9:16) | Chưa làm master 30s 16:9 |
| Lịch | 4 ngày làm việc (+ Ngày 0 chuẩn bị) | |
| Trần chi phí AI | **$200** | |
| Phát hành | Có thể chạy thật với ngân sách media nhỏ, hoặc chỉ nội bộ | BR quyết |

**Chưa kiểm chứng được trong pilot** (sẽ kiểm ở chiến dịch đầy đủ đầu tiên): chiến lược hero shot 16:9 + 9:16, crop center-safe, master ProRes/TV, giọng đọc người thật cho master.

## 3. Ngày 0 — Chuẩn bị một lần (dùng cho mọi chiến dịch sau)

| # | Việc | Ai | Xong? |
|---|---|---|---|
| 0.1 | Project GCP + bật Agent Platform, **bật thanh toán** (điều kiện để được bồi hoàn), kiểm tra hạn mức Veo | P | ☐ |
| 0.2 | Tạo Shared Drive theo cấu trúc SOP 9.1; tải `campaign-workbook.xlsx` lên làm Google Sheet mẫu | P | ☐ |
| 0.3 | Điền Brand Kit, tạo Gem, tải Knowledge (guideline, đội tàu bay, kịch bản cũ, `03-prompt-structure.md`) | P + CW | ☐ |
| 0.4 | Thu thập ảnh/footage thật đúng dòng máy bay của đường bay pilot; xác nhận quyền sử dụng (V5) | P + BR | ☐ |
| 0.5 | Dựng template MOGRT: end card (logo + CTA + **nhãn AI**), phụ đề VI/EN, lower third, khung 9:16 có vạch vùng an toàn | ED | ☐ |
| 0.6 | Chọn 1 giọng TTS tiếng Việt + 1 giọng tiếng Anh cho thương hiệu, ghi vào Brand Kit | AI + BR | ☐ |
| 0.7 | Gửi câu hỏi bồi hoàn cho Google account rep (V1) | P | ☐ |
| 0.8 | Legal xác nhận hình thức nhãn AI theo NĐ 142/2026 (V3) → chốt mẫu end card | LG | ☐ |
| 0.9 | Chạy thử nhanh V6, V7, V8 (Veo Fast 4K, Flow 9:16, dấu tiếng Việt) | AI | ☐ |
| 0.10 | Phân vai: ai là P, CW, AI, ED, QC, BR, LG cho pilot | P | ☐ |

**Điều kiện bắt đầu Ngày 1:** 0.1–0.5, 0.8 và 0.10 đã xong. V1 không chặn pilot (pilot chỉ dùng Veo 3.1 Standard cho bản cuối).

## 4. Lịch pilot

| Ngày | Việc | Kết thúc bằng |
|---|---|---|
| 1 | Brief → Ý tưởng (Gem) → Kịch bản 15s + Shot list → Storyboard 9:16 | 🚦 Cổng 1 |
| 2 | Production Bible → Animatic 15s + TTS nháp | 🚦 Cổng 2 |
| 3 | Tạo shot (Fast → Standard) + QC từng shot · Nhạc Lyria · Dựng C15-VI | |
| 4 | C06-VI + C15-EN → QC toàn bộ → Giao | 🚦 Cổng 3 |

## 5. Đo lường

Producer ghi trong suốt pilot (thêm một sheet `Pilot` vào workbook nếu cần):

| Chỉ số | Cách đo | Mục tiêu pilot |
|---|---|---|
| Giờ công từng bước | Mỗi người ghi giờ bắt đầu/kết thúc theo bước | Làm cơ sở cho lịch chuẩn |
| Chi phí AI theo nhóm | Sheet `Ngân sách` | ≤ $200 |
| Số lần tạo / shot được chọn | Shot log: tổng dòng ÷ số shot `select` | ≤ 4 với video |
| Shot chạm giới hạn 3+3 | Đếm | Ghi lại lý do từng shot |
| Tỉ lệ QC fail theo phần A–F | Shot log `qc_status` + sheet QC | Tìm lỗi AI hay gặp nhất |
| Số vòng sửa ở mỗi cổng | Đếm | ≤ 1 / cổng |
| Thời gian chờ render | Ghi tay khi chờ > 5 phút | Biết có cần chạy song song không |
| Tổng thời gian | Ngày 1 → giao | ≤ 4 ngày |
| Lỗi A/B/E ở bản giao | Sheet QC | **0** |

## 6. Họp rút kinh nghiệm (trong 2 ngày sau khi giao)

**Người tham dự:** cả team + BR.

1. Bước nào tốn thời gian nhất so với dự kiến? Tại sao?
2. Lỗi AI nào lặp lại nhiều nhất? Cần thêm gì vào prompt chuẩn / negative prompt / checklist QC?
3. Production Bible có đủ giữ nhân vật và tàu bay nhất quán không?
4. Gem viết kịch bản có đúng tone không? Cần sửa Instructions ở đâu?
5. Giới hạn 3+3 lần có hợp lý không?
6. Cổng duyệt nào bị kẹt? Vì sao?
7. Kết quả các mục cần xác minh V1–V10?
8. Bước nào lặp lại nhiều, đáng **tự động hoá bằng API** trước tiên?

**Đầu ra:**

| # | Thay đổi SOP | Mục trong SOP | Người sửa |
|---|---|---|---|
| | | | |

→ Cập nhật **SOP v1.1**, ghi vào lịch sử phiên bản. Sau đó áp dụng cho chiến dịch đầy đủ đầu tiên (M30 + C15 + C06, VI + EN).
