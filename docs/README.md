# Tài liệu quy trình sản xuất video quảng cáo `[HÃNG]` bằng AI của Google

Bắt đầu từ **[guide.html](guide.html)** (mở bằng trình duyệt) — hướng dẫn sử dụng kit theo vai trò, checklist thiết lập lần đầu, prompt mẫu có nút sao chép, máy tính chi phí. Quy định chi tiết nằm trong **[SOP.md](SOP.md)**.

| File | Nội dung | Ai dùng |
|---|---|---|
| [SOP.md](SOP.md) | Quy trình 9 bước, 4 cổng duyệt, vai trò, lịch 5 ngày + 1 dự phòng, chi phí, pháp lý, Model Registry | Cả team |
| [pilot-plan.md](pilot-plan.md) | Chuẩn bị một lần + chạy thử SOP trên bộ social 15s | Producer |
| [templates/01-brief.md](templates/01-brief.md) | Mẫu brief chiến dịch | Producer + Brand Approver |
| [templates/02-brand-kit-gem.md](templates/02-brand-kit-gem.md) | Brand Kit + Instructions cho Gem viết ý tưởng/kịch bản/prompt | Producer, Copywriter |
| [templates/03-prompt-structure.md](templates/03-prompt-structure.md) | Cấu trúc prompt ảnh, video (Veo), nhạc (Lyria), giọng đọc (TTS) + thư viện prompt | AI Artist |
| [templates/06-qc-checklist.md](templates/06-qc-checklist.md) | Checklist QC: hàng không, an toàn bay, lỗi AI, thương hiệu, pháp lý, kỹ thuật | QC Reviewer |
| [templates/campaign-workbook.xlsx](templates/campaign-workbook.xlsx) | Workbook mỗi chiến dịch: Ngân sách, Giá model, Shot list, Shot log (tự tính chi phí), QC | Producer, AI Artist, Editor, QC |
| `templates/04-shot-list.csv`, `templates/05-shot-log.csv` | Bản CSV của Shot list / Shot log (cùng cột với workbook, dùng cho tự động hoá sau này) | — |

## Cập nhật workbook

Workbook được sinh từ [`../scripts/build_workbook.py`](../scripts/build_workbook.py). Bảng giá model nằm ở `PRICES` trong script; sheet QC đọc trực tiếp từ `06-qc-checklist.md`. Khi đổi giá hoặc checklist:

```bash
python3 -m venv .venv && .venv/bin/pip install openpyxl
.venv/bin/python scripts/build_workbook.py docs/templates
```

Sau đó tải lại workbook lên Drive làm mẫu mới (không ghi đè workbook của chiến dịch đang chạy).
