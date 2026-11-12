# Cấu trúc prompt chuẩn

Áp dụng cho Bước 3–6. **Prompt hình ảnh, video và nhạc viết bằng tiếng Anh** (model hiểu tốt nhất). Mọi prompt dùng xong đều dán đầy đủ vào Shot log.

Quy tắc chung:
- Một prompt = **một chủ thể chính + một hành động chính**.
- Mô tả cái **muốn thấy**, cụ thể và nhìn được (ánh sáng, chất liệu, ống kính) — tránh tính từ chung chung như "beautiful", "amazing".
- **Không bao giờ yêu cầu chữ, logo, biển hiệu** trong hình.
- Nhân vật luôn gọi bằng mã trong Bible (`CH01`, `CH02`…) và đính kèm ảnh tham chiếu tương ứng.
- Prompt tốt (đạt QC ngay lần 1–2) → copy vào mục **Thư viện prompt** cuối file này.

---

## 1. Ảnh — Character sheet (Nano Banana Pro)

```text
[CHARACTER] Character reference sheet of {age} {gender} {ethnicity/look}, {build}, {hair}, {distinguishing features}.
[WARDROBE] Wearing {outfit, colors, materials}.
[LAYOUT] Same person shown in 5 views on a plain light-grey studio background: front, three-quarter left, profile left, three-quarter right, full body standing.
[LIGHT] Soft even studio lighting, neutral color balance.
[STYLE] Photorealistic, natural skin texture, 85mm lens look.
[EXCLUDE] No text, no labels, no logos, no jewelry with letters. Does not resemble any real or famous person.
```

## 2. Ảnh — Style frame / Khung đầu (Nano Banana Pro)

Đính kèm: ảnh nhân vật (`CH##`), ảnh tàu bay/cabin thật, style frame đã duyệt.

```text
[SHOT] {shot type: wide / medium / close-up}, {camera angle}, {aspect ratio 16:9 or 9:16}.
[SUBJECT] {CH01 from reference image} {pose / expression}.
[SETTING] {location, using reference image of real cabin / destination}.
[TIME & LIGHT] {time of day}, {light quality and direction}, {color temperature}.
[STYLE] Match the attached style frame: {grade description}, {lens: e.g. 35mm, shallow depth of field}.
[COMPOSITION] {subject placement}. Keep main subject centered (center-safe for 9:16 crop).
[EXCLUDE] No text, no logos, no signage, no letters anywhere in frame.
```

**Shot có tàu bay (HYBRID):** dùng **ảnh thật** của hãng làm nền/khung đầu; chỉ cho model **thêm/chỉnh** yếu tố khác (bầu trời, ánh sáng, người). Thêm dòng:
```text
[PRESERVE] Keep the aircraft exactly as in the reference photo: same livery, same proportions, same number of engines and windows. Do not redraw or alter the aircraft.
```

## 3. Video — Veo 3.1 (image-to-video)

**Đầu vào bắt buộc:** khung đầu đã duyệt (+ khung cuối nếu cần khống chế chuyển động), ảnh tham chiếu nhân vật.

**Tham số mặc định:**

| Tham số | Nháp | Bản cuối |
|---|---|---|
| Model | `veo-3.1-fast-generate-001` | `veo-3.1-generate-001` |
| Độ phân giải | 720p | 1080p (4K nếu master TV) |
| Thời lượng | đúng thời lượng shot list (4/6/8s) | như nháp |
| Tỉ lệ | 16:9 (hero shot: thêm 9:16) | như nháp |
| Tạo âm thanh | **Tắt** | **Tắt** (trừ khi shot list ghi cần) |
| Seed | ghi lại | dùng seed của bản nháp tốt nhất |

**Prompt:**

```text
[CAMERA] {movement: slow dolly in / static / gentle pan left / crane up}, {lens feel}, {speed: slow, smooth}.
[SUBJECT] {CH01} {single main action, described physically: "turns her head toward the window and smiles softly"}.
[SETTING] {where — must match first frame}.
[LIGHT] {must match first frame}, {any change: "sunlight sweeps across her face"}.
[MOTION DETAILS] {secondary motion: clouds drift, hair moves slightly}.
[STYLE] Cinematic commercial, photorealistic, {grade}, 24fps natural motion blur.
[AUDIO] none
```

**Negative prompt** (trường `negativePrompt` — liệt kê thứ cần tránh, **không** viết dạng "no …"):
```text
text, letters, logos, watermark, signage, distorted hands, extra fingers, warped face, morphing, flickering, sudden camera cuts, unbuckled seatbelt during takeoff, luggage in aisle
```

**Shot tàu bay (HYBRID) — giữ chuyển động tối thiểu:**
```text
[CAMERA] Locked-off tripod shot, no camera movement.
[SUBJECT] The aircraft from the first frame rolls slowly forward along the runway centerline. The aircraft shape, livery and proportions stay exactly as in the first frame.
[SETTING] {airport, time}.
[MOTION DETAILS] Heat haze behind engines, subtle shimmer.
[STYLE] Photorealistic, matches first frame exactly.
[AUDIO] none
```
→ Nếu 3+3 lần vẫn méo tàu bay → **dùng footage thật** (SOP 8.2).

## 4. Nhạc — Lyria

```text
[GENRE] {e.g. cinematic ambient pop}
[MOOD] {e.g. hopeful, warm, light anticipation building to uplift}
[INSTRUMENTS] {e.g. soft piano, airy synth pads, light percussion entering at 0:10}
[TEMPO] {e.g. 100 BPM}
[STRUCTURE] {e.g. gentle intro 0–8s, build 8–22s, resolve and soft ending 22–30s}
[CONSTRAINTS] Instrumental only, no vocals, no lyrics. Leave space for voice-over (mid frequencies not too busy).
```

## 5. Giọng đọc — Gemini TTS

- Chọn **1 giọng VI + 1 giọng EN** cố định cho thương hiệu, ghi vào Brand Kit. Không đổi giữa các chiến dịch nếu không có lý do.
- Chỉ dẫn phong cách (đặt trước lời đọc):
```text
Đọc bằng giọng ấm áp, tự tin, tốc độ vừa phải, nhấn nhẹ vào tên điểm đến, nghỉ ngắn trước câu kêu gọi hành động.
```
- Tên riêng/mã sân bay dễ đọc sai → viết theo cách đọc (VD: "Đà Nẵng", không viết "DAD").
- Đo thời lượng file VO so với khung thời gian VO của kịch bản ngay ở animatic.

---

## Thư viện prompt (bổ sung dần)

| Ngày | Chiến dịch | Loại shot | Model | Prompt (rút gọn) / Link Shot log | Ghi chú vì sao hiệu quả |
|---|---|---|---|---|---|
| | | | | | |
