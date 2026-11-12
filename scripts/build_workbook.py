"""Build campaign workbook (xlsx) + CSV templates for the ad-maker SOP.

Usage: python build_workbook.py <docs/templates dir>
QC items are parsed from 06-qc-checklist.md so the checklist has one source.
"""
import csv
import re
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

OUT = Path(sys.argv[1])
N_ROWS = 500  # pre-filled formula rows in Shot log

HEAD_FONT = Font(bold=True, color="FFFFFF")
HEAD_FILL = PatternFill("solid", fgColor="1F3A5F")
EX_FILL = PatternFill("solid", fgColor="FFF4CC")
SEC_FILL = PatternFill("solid", fgColor="DCE6F1")
WRAP = Alignment(wrap_text=True, vertical="top")

# ---------------------------------------------------------------- data
PRICES = [
    # key, name, model_id, resolution, audio, unit, price_usd, category
    ("veo31std_1080_noaudio", "Veo 3.1 Standard", "veo-3.1-generate-001", "1080p", "N", "giây", 0.20, "Video bản cuối"),
    ("veo31std_1080_audio", "Veo 3.1 Standard", "veo-3.1-generate-001", "1080p", "Y", "giây", 0.40, "Video bản cuối"),
    ("veo31std_4k_noaudio", "Veo 3.1 Standard", "veo-3.1-generate-001", "4K", "N", "giây", 0.40, "Video bản cuối"),
    ("veo31std_4k_audio", "Veo 3.1 Standard", "veo-3.1-generate-001", "4K", "Y", "giây", 0.60, "Video bản cuối"),
    ("veo31fast_720_noaudio", "Veo 3.1 Fast", "veo-3.1-fast-generate-001", "720p", "N", "giây", 0.08, "Video nháp"),
    ("veo31fast_720_audio", "Veo 3.1 Fast", "veo-3.1-fast-generate-001", "720p", "Y", "giây", 0.10, "Video nháp"),
    ("veo31fast_1080_noaudio", "Veo 3.1 Fast", "veo-3.1-fast-generate-001", "1080p", "N", "giây", 0.10, "Video nháp"),
    ("veo31fast_1080_audio", "Veo 3.1 Fast", "veo-3.1-fast-generate-001", "1080p", "Y", "giây", 0.12, "Video nháp"),
    ("omni12flash_720", "Gemini Omni 1.2 Flash (ước tính)", "gemini-omni-1.2-flash", "720p", "Y", "giây", 0.07, "Video nháp"),
    ("nb21_1k", "Nano Banana 2.1", "gemini-nano-banana-2.1", "1K", "-", "ảnh", 0.034, "Ảnh"),
    ("nb21_2k", "Nano Banana 2.1", "gemini-nano-banana-2.1", "2K", "-", "ảnh", 0.05, "Ảnh"),
    ("nbpro_2k", "Nano Banana Pro", "gemini-3-pro-image", "1K/2K", "-", "ảnh", 0.134, "Ảnh"),
    ("nbpro_4k", "Nano Banana Pro", "gemini-3-pro-image", "4K", "-", "ảnh", 0.24, "Ảnh"),
    ("lyria3pro", "Lyria 3 Pro", "(điền khi rà soát)", "-", "Y", "bài", 0.08, "Nhạc"),
    ("tts_flash", "Gemini TTS Flash (giá KM tới 31/12/2026)", "gemini-3.8-flash-tts", "-", "Y", "giây audio", 0.000225, "Giọng đọc"),
    ("real_footage", "Footage/ảnh thật của hãng", "-", "-", "-", "clip", 0.0, "Tư liệu thật"),
]
CATEGORIES = ["Video nháp", "Video bản cuối", "Ảnh", "Nhạc", "Giọng đọc", "Tư liệu thật"]

SHOT_LIST_COLS = [
    ("shot_id", "Mã shot: S01, S02…", 9),
    ("duration_s", "Thời lượng (giây): 4/6/8", 10),
    ("description", "Mô tả hình (tiếng Việt)", 40),
    ("camera", "Góc máy & chuyển động", 28),
    ("source", "AI / THẬT / HYBRID (ảnh thật làm khung đầu)", 11),
    ("hero", "Y = hero shot, tạo riêng cả 16:9 và 9:16", 7),
    ("ratios", "16:9 hoặc 16:9+9:16", 11),
    ("used_in", "Dùng trong: M30, C15, C06 (ngăn bởi dấu phẩy)", 13),
    ("vo_vi", "Lời VO tiếng Việt", 34),
    ("vo_en", "Lời VO tiếng Anh", 34),
    ("onscreen_vi", "Chữ trên màn hình VI (lớp đồ hoạ)", 24),
    ("onscreen_en", "Chữ trên màn hình EN (lớp đồ hoạ)", 24),
    ("sfx", "SFX cần có", 18),
    ("bible_refs", "Mã tham chiếu Bible: CH01, AC01, LOC02, STY01", 20),
    ("first_frame", "Tên file khung đầu đã duyệt", 28),
    ("status", "todo / draft / selected / locked", 10),
    ("notes", "Ghi chú", 30),
]
SHOT_LIST_EXAMPLES = [
    ["S01", 6, "Tàu bay A321neo của hãng lăn ra đường băng lúc bình minh", "Locked-off, góc thấp ngang càng đáp",
     "HYBRID", "Y", "16:9+9:16", "M30,C15,C06", "Mỗi chuyến bay là một khởi đầu.", "Every flight is a new beginning.",
     "", "", "Tiếng động cơ tăng dần", "AC01, STY01", "DAD25_S01_FF_169_nbpro_v02.png", "todo",
     "VÍ DỤ — xoá trước khi dùng. Nếu 3+3 lần méo tàu bay → footage thật"],
    ["S02", 4, "CH01 nhìn ra cửa sổ, nắng sớm chiếu lên mặt, mỉm cười", "Slow dolly in, 50mm",
     "AI", "N", "16:9", "M30,C15", "", "", "Đà Nẵng — chỉ từ 499.000đ*", "Da Nang — from 499,000 VND*",
     "Tiếng cabin nhẹ", "CH01, CAB01, STY01", "DAD25_S02_FF_169_nbpro_v01.png", "todo",
     "VÍ DỤ — center-safe để crop 9:16. Giá chờ Legal xác nhận"],
]

SHOT_LOG_COLS = [
    ("date", "Ngày tạo (YYYY-MM-DD)", 11),
    ("campaign", "Mã chiến dịch", 9),
    ("shot_id", "Mã shot (S01) hoặc mã Bible (CH01)", 9),
    ("take", "Lần thử thứ mấy", 6),
    ("ratio", "16:9 / 9:16", 7),
    ("model_key", "Chọn từ danh sách (sheet Giá model) — quyết định giá", 22),
    ("model_id", "Tự điền", 24),
    ("resolution", "Tự điền", 9),
    ("audio", "Tự điền", 6),
    ("qty", "Số lượng: giây (video, TTS) / số ảnh / số bài", 8),
    ("prompt", "Prompt ĐẦY ĐỦ (dán nguyên văn)", 50),
    ("negative_prompt", "Negative prompt", 30),
    ("refs", "Ảnh tham chiếu / khung đầu đã dùng", 28),
    ("seed", "Seed", 10),
    ("cost_usd", "Tự tính = qty × đơn giá", 9),
    ("category", "Tự điền", 13),
    ("file_name", "Tên file theo quy ước SOP 9.2", 34),
    ("status", "draft / select / reject", 9),
    ("reject_reason", "Lý do loại (để rút kinh nghiệm)", 26),
    ("qc_by", "Người kiểm QC (khác người tạo)", 12),
    ("qc_status", "pending / pass / fail", 9),
    ("notes", "Ghi chú", 26),
]
LOG_IDX = {name: i for i, (name, _, _) in enumerate(SHOT_LOG_COLS)}
SHOT_LOG_EXAMPLES = [
    ["2026-11-20", "DAD25", "CH01", 1, "", "nbpro_2k", None, None, None, 4,
     "Character reference sheet of a Vietnamese woman in her early 30s…", "", "", "", None, None,
     "DAD25_CH01_sheet_nbpro_v01.png", "select", "", "Lan", "pass", "VÍ DỤ — xoá trước khi dùng"],
    ["2026-11-21", "DAD25", "S02", 1, "16:9", "veo31fast_720_noaudio", None, None, None, 4,
     "[CAMERA] Slow dolly in… [SUBJECT] CH01 turns toward the window…", "text, logos, distorted hands…",
     "DAD25_S02_FF_169_nbpro_v01.png; CH01", "123456", None, None,
     "DAD25_S02_169_veo31fast_t01.mp4", "reject", "Ngón tay biến dạng ở giây 3", "Minh", "fail", "VÍ DỤ"],
    ["2026-11-21", "DAD25", "S02", 4, "16:9", "veo31std_1080_noaudio", None, None, None, 4,
     "(cùng prompt lần 1, sửa mô tả tay)", "text, logos, distorted hands…",
     "DAD25_S02_FF_169_nbpro_v01.png; CH01", "123456", None, None,
     "DAD25_S02_169_veo31std_t04.mp4", "select", "", "Minh", "pass", "VÍ DỤ"],
]
DELIVERABLES = ["M30-VI", "M30-EN", "C15-VI", "C15-EN", "C06-VI", "C06-EN"]


# ---------------------------------------------------------------- helpers
def style_header(ws, widths):
    for c, w in enumerate(widths, start=1):
        cell = ws.cell(row=1, column=c)
        cell.font, cell.fill, cell.alignment = HEAD_FONT, HEAD_FILL, WRAP
        ws.column_dimensions[get_column_letter(c)].width = w
    ws.freeze_panes = "B2"


def add_list_validation(ws, col_letter, formula, last_row):
    dv = DataValidation(type="list", formula1=formula, allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f"{col_letter}2:{col_letter}{last_row}")


def col(name):
    return get_column_letter(LOG_IDX[name] + 1)


def parse_qc(md_path):
    sections, current = [], None
    for line in md_path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^## ([A-F])\. (.+)$", line)
        if m:
            current = (m.group(1), m.group(2), [])
            sections.append(current)
            continue
        m = re.match(r"^- \[ \] (.+)$", line)
        if m and current:
            current[2].append(m.group(1).replace("**", ""))
    return sections


# ---------------------------------------------------------------- workbook
wb = Workbook()

# Hướng dẫn
ws = wb.active
ws.title = "Hướng dẫn"
guide = [
    ["Workbook chiến dịch — SOP sản xuất video quảng cáo [HÃNG]"],
    [""],
    ["1. Tải file lên Shared Drive → mở bằng Google Sheets → đổi tên thành {CAMPAIGN}_workbook."],
    ["2. Xoá các dòng VÍ DỤ (tô vàng) ở sheet Shot list và Shot log."],
    ["3. Shot list: điền ở Bước 2, khoá sau Cổng duyệt 2."],
    ["4. Shot log: MỖI lần gọi model = 1 dòng, kể cả lần hỏng. Chọn model_key từ danh sách; model_id, cost_usd… tự tính."],
    ["5. QC: chạy cho từng file giao ở Bước 9 (Đạt / Lỗi / N/A). Mục A, B, E Lỗi = loại."],
    ["6. Ngân sách: tự cộng từ Shot log. Vượt $400 → Producer báo Brand Approver."],
    ["7. Giá model: cập nhật khi rà soát Model Registry hằng tháng (SOP mục 11)."],
    [""],
    ["Giá theo tra cứu ngày 2026-11-12 — xác minh lại trước khi dùng cho báo giá."],
]
for r in guide:
    ws.append(r)
ws["A1"].font = Font(bold=True, size=14)
ws.column_dimensions["A"].width = 110

# Giá model
wp = wb.create_sheet("Giá model")
wp.append(["model_key", "Model", "model_id", "Độ phân giải", "Có tiếng", "Đơn vị", "Đơn giá (USD)", "Nhóm"])
for row in PRICES:
    wp.append(list(row))
style_header(wp, [24, 34, 26, 12, 9, 11, 13, 16])
for r in range(2, len(PRICES) + 2):
    wp.cell(row=r, column=7).number_format = "0.000###"
price_last = len(PRICES) + 1
price_rng = f"'Giá model'!$A$2:$H${price_last}"

# Shot list
wsl = wb.create_sheet("Shot list")
wsl.append([c[0] for c in SHOT_LIST_COLS])
for ex in SHOT_LIST_EXAMPLES:
    wsl.append(ex)
    for c in range(1, len(SHOT_LIST_COLS) + 1):
        wsl.cell(row=wsl.max_row, column=c).fill = EX_FILL
style_header(wsl, [c[2] for c in SHOT_LIST_COLS])
for c, (_, tip, _) in enumerate(SHOT_LIST_COLS, start=1):
    wsl.cell(row=1, column=c).comment = None
names = [c[0] for c in SHOT_LIST_COLS]
add_list_validation(wsl, get_column_letter(names.index("source") + 1), '"AI,THẬT,HYBRID"', 200)
add_list_validation(wsl, get_column_letter(names.index("hero") + 1), '"Y,N"', 200)
add_list_validation(wsl, get_column_letter(names.index("ratios") + 1), '"16:9,16:9+9:16"', 200)
add_list_validation(wsl, get_column_letter(names.index("status") + 1), '"todo,draft,selected,locked"', 200)
for row in wsl.iter_rows(min_row=2):
    for cell in row:
        cell.alignment = WRAP

# Shot log
wlog = wb.create_sheet("Shot log")
wlog.append([c[0] for c in SHOT_LOG_COLS])
last = N_ROWS + 1
for i in range(N_ROWS):
    r = i + 2
    row = SHOT_LOG_EXAMPLES[i] if i < len(SHOT_LOG_EXAMPLES) else [None] * len(SHOT_LOG_COLS)
    for c, v in enumerate(row, start=1):
        if v is not None:
            wlog.cell(row=r, column=c, value=v)
    mk, q = f"{col('model_key')}{r}", f"{col('qty')}{r}"
    look = lambda n: f'=IF({mk}="","",VLOOKUP({mk},{price_rng},{n},FALSE))'
    wlog[f"{col('model_id')}{r}"] = look(3)
    wlog[f"{col('resolution')}{r}"] = look(4)
    wlog[f"{col('audio')}{r}"] = look(5)
    wlog[f"{col('category')}{r}"] = look(8)
    wlog[f"{col('cost_usd')}{r}"] = f'=IF(OR({mk}="",{q}=""),"",{q}*VLOOKUP({mk},{price_rng},7,FALSE))'
    wlog[f"{col('cost_usd')}{r}"].number_format = "0.00"
    if i < len(SHOT_LOG_EXAMPLES):
        for c in range(1, len(SHOT_LOG_COLS) + 1):
            wlog.cell(row=r, column=c).fill = EX_FILL
style_header(wlog, [c[2] for c in SHOT_LOG_COLS])
add_list_validation(wlog, col("model_key"), f"='Giá model'!$A$2:$A${price_last}", last)
add_list_validation(wlog, col("ratio"), '"16:9,9:16"', last)
add_list_validation(wlog, col("status"), '"draft,select,reject"', last)
add_list_validation(wlog, col("qc_status"), '"pending,pass,fail"', last)

# QC (bản dựng / file giao)
wq = wb.create_sheet("QC")
wq.append(["Mục", "Hạng mục kiểm"] + DELIVERABLES + ["Ghi chú"])
sections = parse_qc(OUT / "06-qc-checklist.md")
assert sections, "Không đọc được mục nào từ 06-qc-checklist.md"
for letter, title, items in sections:
    wq.append([letter, title])
    for c in range(1, len(DELIVERABLES) + 4):
        wq.cell(row=wq.max_row, column=c).fill = SEC_FILL
        wq.cell(row=wq.max_row, column=c).font = Font(bold=True)
    for n, item in enumerate(items, start=1):
        wq.append([f"{letter}{n}", item] + ["" for _ in DELIVERABLES])
style_header(wq, [6, 70] + [9] * len(DELIVERABLES) + [30])
first_d, last_d = get_column_letter(3), get_column_letter(2 + len(DELIVERABLES))
dv = DataValidation(type="list", formula1='"Đạt,Lỗi,N/A"', allow_blank=True)
wq.add_data_validation(dv)
dv.add(f"{first_d}2:{last_d}{wq.max_row}")
for row in wq.iter_rows(min_row=2, max_col=2):
    for cell in row:
        cell.alignment = WRAP
qc_last = wq.max_row
wq.append([])
wq.append(["", "Người kiểm / Ngày"])
wq.append(["", "Số mục Lỗi"] + [f'=COUNTIF({get_column_letter(3 + i)}2:{get_column_letter(3 + i)}{qc_last},"Lỗi")'
                                  for i in range(len(DELIVERABLES))])

# Ngân sách
wb_ = wb.create_sheet("Ngân sách")
cost_rng = f"'Shot log'!${col('cost_usd')}$2:${col('cost_usd')}${last}"
cat_rng = f"'Shot log'!${col('category')}$2:${col('category')}${last}"
wb_.append(["Hạng mục", "USD"])
wb_.append(["Trần ngân sách AI", 500])
wb_.append(["Ngưỡng cảnh báo", 400])
wb_.append([])
wb_.append(["Chi theo nhóm", ""])
start = wb_.max_row + 1
for cat in CATEGORIES:
    wb_.append([cat, f'=SUMIF({cat_rng},"{cat}",{cost_rng})'])
end = wb_.max_row
wb_.append(["Tổng đã chi", f"=SUM(B{start}:B{end})"])
total_row = wb_.max_row
wb_.append(["Còn lại", f"=B2-B{total_row}"])
wb_.append(["Trạng thái", f'=IF(B{total_row}>=B2,"VƯỢT TRẦN — dừng",IF(B{total_row}>=B3,"Cảnh báo — báo Brand Approver","Trong ngân sách"))'])
wb_.append([])
wb_.append(["Số lần tạo bị loại", f"=COUNTIF('Shot log'!${col('status')}$2:${col('status')}${last},\"reject\")"])
wb_.append(["Số lần tạo được chọn", f"=COUNTIF('Shot log'!${col('status')}$2:${col('status')}${last},\"select\")"])
style_header(wb_, [36, 16])
for r in range(2, wb_.max_row + 1):
    wb_.cell(row=r, column=2).number_format = "0.00"
for r in (5,):
    wb_.cell(row=r, column=1).font = Font(bold=True)
wb_.cell(row=total_row, column=1).font = Font(bold=True)
wb_.freeze_panes = None

wb.move_sheet("Ngân sách", offset=-(len(wb.sheetnames) - 2))
wb.save(OUT / "campaign-workbook.xlsx")

# ---------------------------------------------------------------- CSVs
with open(OUT / "04-shot-list.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow([c[0] for c in SHOT_LIST_COLS])
    w.writerows(SHOT_LIST_EXAMPLES)

price_map = {p[0]: p for p in PRICES}
with open(OUT / "05-shot-log.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow([c[0] for c in SHOT_LOG_COLS])
    for ex in SHOT_LOG_EXAMPLES:
        row = list(ex)
        p = price_map[row[LOG_IDX["model_key"]]]
        row[LOG_IDX["model_id"]], row[LOG_IDX["resolution"]], row[LOG_IDX["audio"]] = p[2], p[3], p[4]
        row[LOG_IDX["cost_usd"]] = round(row[LOG_IDX["qty"]] * p[6], 4)
        row[LOG_IDX["category"]] = p[7]
        w.writerow(row)

print("sheets:", wb.sheetnames)
print("qc sections:", [(s[0], len(s[2])) for s in sections])
