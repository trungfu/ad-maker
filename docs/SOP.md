# SOP — Sản xuất video quảng cáo hàng không bằng AI của Google

| | |
|---|---|
| **Phiên bản** | 1.0 (bản đầu, chưa qua pilot) |
| **Ngày** | 2026-11-12 |
| **Áp dụng cho** | `[HÃNG]` — mọi chiến dịch video quảng cáo |
| **Chủ sở hữu tài liệu** | Producer |
| **Rà soát** | Model Registry (mục 11): hằng tháng · Toàn bộ SOP: sau pilot, sau đó mỗi quý |

> Tài liệu viết dạng chung với placeholder `[HÃNG]`. Mọi đặc thù thương hiệu (tone, đội tàu bay, slogan, quy tắc giá…) nằm trong **Brand Kit** — xem [templates/02-brand-kit-gem.md](templates/02-brand-kit-gem.md).

---

## 1. Mục đích & phạm vi

Quy trình **lặp lại được** để một team creative sản xuất một **bộ video quảng cáo** cho mỗi chiến dịch trong **5 ngày làm việc**, với chi phí AI **≤ 500 USD/bộ** (chưa tính nhân sự).

- **Tạo nội dung** (kịch bản, ảnh, video, nhạc, giọng đọc): dùng AI của Google.
- **Hậu kỳ** (dựng, màu, đồ hoạ, mix, xuất file): Premiere Pro + After Effects.
- **Tự động hoá bằng API**: ngoài phạm vi phiên bản này — sẽ làm sau khi chạy tay 1–2 chiến dịch.

## 2. Bộ sản phẩm chuẩn mỗi chiến dịch

| Mã | Phiên bản | Tỉ lệ | Độ dài | Ngôn ngữ | Kênh |
|---|---|---|---|---|---|
| M30-VI / M30-EN | Master | 16:9 | 30s | VI / EN | YouTube, TV online, màn hình sân bay |
| C15-VI / C15-EN | Cutdown | 9:16 | 15s | VI / EN | Reels, TikTok, Shorts |
| C06-VI / C06-EN | Bumper | 9:16 | 6s | VI / EN | Reels, TikTok, Shorts, YouTube bumper (16:9 nếu cần) |

**Thông số giao file**

| Hạng mục | Master | Social |
|---|---|---|
| File | ProRes 422 HQ (.mov) + H.264 (.mp4) | H.264 High (.mp4) |
| Độ phân giải | 1920×1080 (3840×2160 nếu mọi shot render 4K) | 1080×1920 (9:16) |
| Khung hình | 24 fps xuyên suốt (Veo xuất 24 fps). Nếu phát truyền hình VN 25 fps → chuyển đổi ở bước cuối, kiểm tra với đài | 24 fps |
| Âm thanh | 48 kHz, stereo. **−23 LUFS** (EBU R128) cho TV, **−14 LUFS** cho online. True peak ≤ −1 dBTP | 48 kHz, −14 LUFS, ≤ −1 dBTP |
| Phụ đề | File SRT riêng + bản burn-in | Burn-in bắt buộc (đa số xem không tiếng) |
| Vùng an toàn 9:16 | — | Chữ/logo/CTA nằm trong vùng giữa: chừa ~250 px phía trên, ~400 px phía dưới, ~120 px bên phải (khung 1080×1920). Đối chiếu template safe zone chính thức của từng nền tảng |
| Metadata | **Không xoá** SynthID / C2PA khi xuất | như Master |

## 3. Nguyên tắc cứng (không ngoại lệ)

1. **Livery, logo, dòng máy bay là tài sản thật.** Không để AI tự vẽ logo hay livery. Cảnh tàu bay dùng footage/ảnh thật của hãng, hoặc dùng ảnh thật làm **khung đầu** cho Veo. Logo chèn ở hậu kỳ.
2. **AI không bao giờ vẽ chữ vào hình.** Mọi chữ trên màn hình (giá, CTA, tên điểm đến, phụ đề) nằm ở **lớp đồ hoạ** trong After Effects/Premiere. Nhờ vậy đổi sang bản tiếng Anh chỉ cần thay chữ.
3. **Tiếp viên không xuất hiện cận cảnh dưới dạng AI.** Hành khách AI được phép. Tiếp viên chỉ ở góc xa/từ phía sau, hoặc dùng footage thật.
4. **Flow chỉ để thăm dò ý tưởng.** Bản master render qua **Gemini Enterprise Agent Platform** (tên mới của Vertex AI) bằng tài khoản trả phí của công ty. Lý do: Flow tự gắn watermark nhìn thấy được với người dùng tại Việt Nam, và không nằm trong diện bồi hoàn bản quyền của Google Cloud.
5. **Mọi shot vào bản master dùng model có bồi hoàn bản quyền** — hiện là **Veo 3.1 Standard (bản GA)**. Model khác chỉ dùng cho nháp (xem mục 11).
6. **Có nhãn AI trên mọi phiên bản** và bật khai báo AI trên từng nền tảng (mục 10).
7. **Mọi lần tạo đều được ghi vào Shot log.** Không có trong Shot log = không được đưa vào timeline.
8. **Mọi shot qua QC trước khi vào timeline dựng**, do người không trực tiếp tạo shot đó kiểm.

## 4. Vai trò (RACI)

Một người có thể kiêm nhiều vai, **trừ QC Reviewer**: không được tự kiểm shot do chính mình tạo.

| Vai trò | Ký hiệu | Trách nhiệm chính |
|---|---|---|
| Producer | **P** | Điều phối lịch, ngân sách, Shot log, giao file; sở hữu SOP và Model Registry |
| Creative / Copywriter | **CW** | Ý tưởng, kịch bản, lời VO, chữ trên màn hình (VI + EN) |
| AI Artist | **AI** | Production Bible, storyboard, tạo shot video, nhạc, giọng đọc AI |
| Editor | **ED** | Animatic, dựng, màu, đồ hoạ, mix, phiên bản, xuất file |
| QC Reviewer | **QC** | Chạy checklist QC từng shot và bản dựng |
| Brand Approver (phía hãng) | **BR** | Duyệt ở 3 cổng |
| Legal | **LG** | Duyệt cổng 3: claim, giá, khuyến mãi, ghi nhãn AI, quyền sử dụng tư liệu |

R = làm · A = chịu trách nhiệm cuối · C = được hỏi ý kiến · I = được thông báo

| Bước | P | CW | AI | ED | QC | BR | LG |
|---|---|---|---|---|---|---|---|
| 1. Brief | A | C | I | I | | C | C |
| 2. Ý tưởng & kịch bản | A | R | C | | | C | |
| 3. Storyboard | A | C | R | | | | |
| **Cổng 1** | R | C | | | | A | |
| 4. Production Bible + Animatic | A | C | R | R | | | |
| **Cổng 2** | R | C | | C | | A | |
| 5. Tạo shot video | A | | R | C | R | | |
| 6. Âm thanh | A | C | R | R | | | |
| 7. Hậu kỳ | A | C | C | R | R | | |
| 8. Phiên bản | A | R (chữ EN) | | R | R | | |
| 9. QC & giao | A | | | R | R | | |
| **Cổng 3** | R | | | C | C | A | A |

## 5. Công cụ & tài khoản

| Công cụ | Dùng để | Tài khoản |
|---|---|---|
| **Gemini — Gem "Brand Kit `[HÃNG]`"** | Ý tưởng, kịch bản, copy VI/EN, viết prompt | Google Workspace của công ty |
| **Google AI Studio / Flow** | Thăm dò nhanh ảnh & chuyển động (**không** dùng cho bản cuối) | Google AI Pro/Ultra |
| **Gemini Enterprise Agent Platform** (Vertex AI cũ) | Render ảnh Bible, khung đầu, shot video bản cuối, nhạc, TTS | Project GCP công ty, **thanh toán trả phí** (điều kiện để được bồi hoàn bản quyền) |
| **Google Shared Drive** | Lưu toàn bộ tài sản chiến dịch | Workspace |
| **Google Sheets** | Shot list, Shot log, ngân sách, checklist QC | Workspace |
| **Premiere Pro + After Effects** | Dựng, màu, template đồ hoạ (MOGRT), mix, xuất | Adobe CC |

## 6. Quy trình 9 bước

### Bước 1 — Brief
- **Input:** yêu cầu từ hãng.
- **Việc làm:** Producer điền [templates/01-brief.md](templates/01-brief.md) cùng Brand Approver. Brief phải có: mục tiêu, thông điệp chính (1 câu), đường bay/ưu đãi, giá + điều kiện áp dụng, CTA, kênh, dòng máy bay sẽ xuất hiện, tư liệu thật có sẵn, hạn chót.
- **Output:** Brief được Brand Approver ký xác nhận.
- **Lưu ý:** Nếu brief nhắc tới giá/khuyến mãi → gửi Legal xem trước điều kiện ngay từ bước này, đừng đợi cổng 3.

### Bước 2 — Ý tưởng & kịch bản
- **Công cụ:** Gem Brand Kit.
- **Việc làm:**
  1. Đưa brief vào Gem, yêu cầu **3–5 hướng ý tưởng** (mỗi hướng: tên, insight, tóm tắt 3 câu, cảnh chủ đạo, rủi ro sản xuất bằng AI).
  2. Producer + CW chọn 1 hướng (có thể gửi BR chọn).
  3. Gem viết **kịch bản 30s + shot list**: mỗi shot có thời lượng, mô tả hình, góc máy, lời VO, chữ trên màn hình, nguồn hình (AI / Thật / Hybrid), có phải hero shot không.
  4. CW chỉnh tay lời VO tiếng Việt cho tự nhiên. Lời VO chiếm tối đa ~24s của 30s; độ dài thực đo lại bằng TTS ở bước animatic.
- **Output:** Kịch bản + Shot list (sheet `Shot list` trong workbook).
- **Quy tắc shot list:**
  - Đánh dấu **hero shot** (3–5 shot đắt giá nhất) → sẽ được tạo riêng ở cả 16:9 và 9:16.
  - Shot còn lại dàn cảnh **center-safe** (chủ thể ở giữa khung) để crop sang 9:16.
  - Shot có tàu bay/logo → nguồn **Thật** hoặc **Hybrid** (ảnh thật làm khung đầu).
  - Shot có tiếp viên → chỉ góc xa/từ phía sau, hoặc nguồn **Thật**.

### Bước 3 — Storyboard
- **Công cụ:** Nano Banana 2.1 (nhanh, rẻ).
- **Việc làm:** Mỗi shot 1 khung hình, 16:9. Ghép thành bảng storyboard (Google Slides hoặc PDF) kèm lời VO dưới mỗi khung.
- **Output:** Storyboard PDF.

> ### 🚦 Cổng duyệt 1 — Kịch bản + Storyboard (cuối Ngày 1)
> **Người duyệt:** Brand Approver. **Duyệt:** ý tưởng, thông điệp, lời VO, trình tự cảnh. Tối đa **1 vòng sửa trong ngày**; quá → lịch lùi.

### Bước 4 — Production Bible + Animatic

**4a. Production Bible** — bộ tham chiếu được duyệt **trước khi tạo bất kỳ shot video nào**. Lưu ở `02_bible/`.

| Mục | Nội dung | Nguồn |
|---|---|---|
| Tàu bay | Ảnh thật đúng **dòng máy bay** xuất hiện trong phim: ngoại thất nhiều góc, cabin từng hạng ghế | Thư viện ảnh của hãng |
| Nhân vật | Character sheet 2–4 hành khách AI: mặt, trang phục, 4–6 góc (chính diện, 3/4, nghiêng, toàn thân) | Nano Banana Pro |
| Điểm đến | Ảnh tham chiếu từng địa điểm (cảnh, giờ trong ngày) | Ảnh thật có quyền sử dụng + Nano Banana Pro |
| Style frame | 3–5 khung chuẩn về màu, ánh sáng, ống kính, độ tương phản | Nano Banana Pro |
| Khung đầu | Khung hình đầu của **từng shot** (và khung cuối nếu cần), 16:9 và 9:16 với hero shot | Nano Banana Pro, dùng ảnh Bible làm tham chiếu |

Quy tắc Bible:
- Nhân vật AI **không được giống người nổi tiếng hay người thật** cụ thể.
- Ảnh thật có người (tiếp viên, phi công) dùng làm tham chiếu → phải có **sự đồng ý của người trong ảnh** (xem mục 12).
- Mỗi lần dùng tham chiếu ghi vào cột `refs` của Shot log.

**4b. Animatic**
- **Việc làm:** Editor ghép các khung đầu theo đúng thời lượng shot list + giọng đọc nháp Gemini TTS + nhạc nháp. Có thể dùng vài clip Veo Fast/Omni giá rẻ cho shot có chuyển động phức tạp.
- **Mục đích:** bắt lỗi nhịp, thời lượng VO, logic câu chuyện **trước khi** tiêu tiền render bản cuối.
- **Output:** Animatic 30s (MP4).

> ### 🚦 Cổng duyệt 2 — Animatic (cuối Ngày 2)
> **Người duyệt:** Brand Approver + quản lý marketing. **Duyệt:** nhịp, thời lượng, Production Bible (nhân vật, style). Sau cổng này **khoá shot list** — thêm shot mới phải qua Producer và tính lại ngân sách.

### Bước 5 — Tạo shot video
- **Công cụ:** Veo 3.1 Fast (nháp) → Veo 3.1 Standard (bản cuối), qua Agent Platform.
- **Việc làm:**
  1. Viết prompt theo cấu trúc chuẩn [templates/03-prompt-structure.md](templates/03-prompt-structure.md) — **prompt viết bằng tiếng Anh**.
  2. Luôn dùng **image-to-video**: khung đầu từ Bible (+ khung cuối nếu cần kiểm soát chuyển động) và ảnh tham chiếu nhân vật.
  3. **Tắt tạo âm thanh** của Veo theo mặc định (âm thanh làm riêng ở bước 6) — giảm ~50% chi phí. Chỉ bật khi cần âm thanh môi trường đặc thù.
  4. Theo **giới hạn số lần tạo** (mục 8.2).
  5. Ghi mọi lần tạo vào Shot log.
  6. Shot chọn → QC Reviewer chạy checklist phần A–C ([templates/06-qc-checklist.md](templates/06-qc-checklist.md)) → đạt mới chuyển vào `04_shots/selects/`.
- **Output:** Các shot đã qua QC, đủ cho bản master và hero shot 9:16.

### Bước 6 — Âm thanh
| Thành phần | Công cụ | Ghi chú |
|---|---|---|
| Nhạc nền | Lyria (Agent Platform) | **Chỉ nhạc không lời.** Tạo 3–5 phương án, chọn 1. Lưu prompt vào Shot log |
| Giọng đọc | Gemini TTS | Dùng cho animatic, bản 15s/6s. Bản master 30s: dùng TTS **hoặc** giọng người thật nếu hãng có giọng đọc thương hiệu — Producer quyết với BR |
| Sonic logo / jingle | File thật của hãng | Luôn ở cuối, không tạo bằng AI |
| SFX | Thư viện SFX có bản quyền (hoặc audio Veo nếu đã bật) | Tiếng động cơ, thông báo cabin… phải đúng ngữ cảnh |

### Bước 7 — Hậu kỳ
- **Công cụ:** Premiere Pro + After Effects.
- **Việc làm:** dựng theo animatic đã duyệt → chỉnh màu đồng nhất theo style frame → chèn đồ hoạ từ **template MOGRT** (logo, khung giá, CTA, phụ đề, end card có sẵn **nhãn AI**) → mix (nhạc, VO, SFX, sonic logo) → xuất bản master.
- **Template MOGRT bắt buộc có:** end card (logo + CTA + nhãn AI), khung giá & điều kiện, tên điểm đến, phụ đề VI/EN, lower third.
- QC Reviewer chạy checklist phần D–F trên bản dựng.

### Bước 8 — Phiên bản
1. **15s và 6s 9:16:** dựng lại từ hero shot 9:16 + crop các shot center-safe. Kiểm tra vùng an toàn.
2. **Bản tiếng Anh:** giữ nguyên hình; thay VO (TTS hoặc người đọc), phụ đề, chữ trên màn hình. CW chịu trách nhiệm bản dịch — **không dịch máy nguyên văn** lời VO.
3. Xuất đủ 6 file theo bảng mục 2.

### Bước 9 — QC & giao file
- QC Reviewer chạy **toàn bộ** checklist trên cả 6 file.
- Producer đóng gói `07_deliverables/` + Shot log + báo cáo chi phí.

> ### 🚦 Cổng duyệt 3 — Bản cuối (Ngày 5)
> **Người duyệt:** Brand Approver **và** Legal (bắt buộc cả hai).
> **Legal kiểm:** giá vé & điều kiện khuyến mãi, claim ("rẻ nhất", "đúng giờ nhất"… phải có căn cứ), dòng máy bay/đường bay thể hiện đúng thực tế, nhãn AI, quyền sử dụng tư liệu và nhạc.

## 7. Lịch 5 ngày

| Ngày | Việc | Kết thúc bằng |
|---|---|---|
| **1** | Brief → Ý tưởng → Kịch bản + Shot list → Storyboard | 🚦 Cổng 1 |
| **2** | Production Bible (nhân vật, style, khung đầu) → Animatic + VO nháp | 🚦 Cổng 2 |
| **3** | Tạo shot video (nháp Fast → bản cuối Standard) → QC từng shot · Nhạc Lyria | |
| **4** | Tạo nốt shot + hero shot 9:16 → Dựng master → Màu → Đồ hoạ → Mix | Master 30s VI nội bộ |
| **5** | Bản 15s/6s 9:16 → Bản EN → QC toàn bộ → Giao | 🚦 Cổng 3 |

Mỗi cổng: tối đa **1 vòng sửa trong ngày**. Vượt → lịch lùi theo, Producer báo lại hạn cho BR.

## 8. Kiểm soát chi phí

### 8.1 Bảng giá tham chiếu
*(Theo tra cứu ngày 2026-11-12, giá trên Agent Platform, USD — xác minh lại khi rà soát Model Registry.)*

| Model | Đơn vị | Giá |
|---|---|---|
| Veo 3.1 Standard 1080p | /giây video | $0.20 không tiếng · $0.40 có tiếng |
| Veo 3.1 Standard 4K | /giây video | $0.40 không tiếng · $0.60 có tiếng |
| Veo 3.1 Fast 720p | /giây video | $0.08 không tiếng · $0.10 có tiếng |
| Veo 3.1 Fast 1080p | /giây video | $0.10 không tiếng · $0.12 có tiếng |
| Nano Banana 2.1 | /ảnh | $0.034 (1K) · $0.05 (2K) |
| Nano Banana Pro | /ảnh | $0.134 (1K/2K) · $0.24 (4K) |
| Lyria 3 Pro | /bài | $0.08 |
| Gemini TTS Flash | /1M token audio (25 token/giây) | $9 (khuyến mãi tới 31/12/2026), $18 từ 2027 |

### 8.2 Giới hạn số lần tạo mỗi shot

```
Shot mới
  ├─ Tối đa 3 lần Veo 3.1 Fast   → đạt bố cục & chuyển động? ──┐
  │                                                             ▼
  ├─ Tối đa 3 lần Veo 3.1 Standard (cùng prompt/khung đầu đã chốt)
  │
  └─ Vẫn hỏng → DỪNG, không thử tiếp. Chọn 1:
        (a) Thiết kế lại shot (đơn giản hoá chuyển động)
        (b) Đổi khung đầu/khung cuối
        (c) Dùng footage thật
```

Producer cập nhật cột `cost_usd` trong Shot log hằng ngày và so với ngân sách.

### 8.3 Ước tính một bộ chiến dịch (tham khảo)

| Hạng mục | Giả định | Chi phí |
|---|---|---|
| Nháp Veo Fast 720p | 10 shot × 8s × 3 lần, không tiếng | ~$19 |
| Bản cuối Veo Standard 1080p | 10 shot × 8s × 3 lần, không tiếng | ~$48 |
| Hero shot 9:16 | 4 shot × 8s × (3 Fast + 3 Standard) | ~$27 |
| Ảnh | ~200 ảnh NB 2.1 + ~100 ảnh NB Pro | ~$20 |
| Nhạc + TTS | 5 bài + ~20 lượt đọc VI/EN | ~$2 |
| **Tổng (1080p)** | | **~$115** |
| **Tổng (4K, bật âm thanh Veo)** | | **~$250** |

Trần **$500** gồm cả dự phòng cho shot khó. Vượt **$400** → Producer báo BR trước khi tiếp tục.

## 9. Quản lý file

### 9.1 Cấu trúc thư mục (Shared Drive)
```
[HÃNG] Ads/
└── {YYYY}-{CAMPAIGN}/
    ├── 00_brief/
    ├── 01_script_storyboard/
    ├── 02_bible/
    │   ├── aircraft/
    │   ├── characters/
    │   ├── locations/
    │   ├── style/
    │   └── first_frames/
    ├── 03_animatic/
    ├── 04_shots/
    │   ├── drafts/
    │   └── selects/
    ├── 05_audio/
    │   ├── music/
    │   ├── vo/
    │   └── sfx/
    ├── 06_edit/
    │   ├── project/
    │   └── exports/
    ├── 07_deliverables/
    └── {CAMPAIGN}_workbook (Google Sheet: Shot list, Shot log, QC, Ngân sách)
```

### 9.2 Quy ước đặt tên
```
{CAMPAIGN}_{SHOT}_{RATIO}_{MODEL}_t{TAKE}.{ext}
VD: DAD25_S03_169_veo31std_t02.mp4
    DAD25_S03_916_veo31fast_t01.mp4
    DAD25_CH01_front_nbpro_v03.png        (character sheet)
    DAD25_S03_FF_169_nbpro_v02.png        (khung đầu)
Deliverable: {CAMPAIGN}_{M30|C15|C06}_{VI|EN}_{169|916}_v{NN}.{mp4|mov}
```

### 9.3 Shot log
Mỗi lần gọi model (kể cả lần hỏng) = **1 dòng** trong sheet `Shot log`. Cột bắt buộc: ngày, shot, lần, tỉ lệ, model + mã model, độ phân giải, thời lượng, có tiếng không, **prompt đầy đủ**, ảnh tham chiếu, seed, chi phí, tên file, trạng thái, lý do loại. Mục đích: shot đẹp thì biết chính xác cách tạo lại; prompt tốt thì đưa vào thư viện prompt.

## 10. Ghi nhãn AI & pháp lý

1. **End card mọi phiên bản** có dòng: *"Video có sử dụng nội dung tạo bởi AI"* (bản EN: *"This video contains AI-generated content"*). Nằm sẵn trong template MOGRT.
2. **Bật khai báo AI trên nền tảng:**
   - Google Ads / YouTube: cài đặt nhãn AI ("How this ad was made").
   - Meta: khai báo AI khi đăng; Meta có thể tự gắn nhãn "AI info".
   - TikTok: bật "contains AI-generated content" — **bắt buộc**, không bật sẽ bị từ chối.
3. **Không xoá metadata SynthID/C2PA** khi xuất file và khi nén lại.
4. **Bối cảnh pháp lý Việt Nam** (cần Legal xác nhận với văn bản gốc — mục 12):
   - Luật Trí tuệ nhân tạo 134/2025/QH15 (hiệu lực 01/03/2026) + Nghị định 142/2026/NĐ-CP: nội dung AI mô phỏng ngoại hình/giọng người thật phải có **nhãn nhìn thấy được**.
   - Luật Quảng cáo sửa đổi 75/2025/QH15 (hiệu lực 01/01/2026) + Nghị định 342/2025.
5. **Bồi hoàn bản quyền của Google Cloud** chỉ áp dụng khi: dùng Agent Platform **trả phí**, model **GA** được liệt kê, không tắt bộ lọc an toàn. **Không** bảo vệ khiếu nại về **nhãn hiệu** trong thương mại → lý do của nguyên tắc 1.

## 11. Model Registry

*Rà soát hằng tháng. Lần rà soát gần nhất: **2026-11-12**.*

| Bước | Model | Mã model | Nền tảng | Trạng thái | Bồi hoàn | Dùng cho bản cuối? |
|---|---|---|---|---|---|---|
| Kịch bản, copy | Gemini (bản Pro mới nhất) | *điền khi rà soát* | Gemini app (Gem) | GA | Có (Gemini) | Có |
| Storyboard nháp | Nano Banana 2.1 | `gemini-nano-banana-2.1` | Agent Platform / AI Studio | *kiểm tra* | Chưa rõ | Không |
| Bible, khung đầu | Nano Banana Pro | `gemini-3-pro-image` | Agent Platform | *kiểm tra* | Chưa rõ | Có (là khung đầu, không xuất hiện trực tiếp) |
| Video nháp | Veo 3.1 Fast | `veo-3.1-fast-generate-001` | Agent Platform | GA | Có | Không (chỉ nháp) |
| **Video bản cuối** | **Veo 3.1 Standard** | `veo-3.1-generate-001` | Agent Platform | GA (tới ít nhất 04/05/2027) | **Có** | **Có** |
| Video thử nghiệm | Gemini Omni 1.2 Flash | `gemini-omni-1.2-flash` | Agent Platform (region `global`) | GA từ 05/11/2026 | **Chưa rõ** | **Không** — tới khi Google xác nhận bồi hoàn bằng văn bản |
| Nhạc | Lyria 3 Pro | *điền khi rà soát* | Agent Platform | *kiểm tra* | Chưa rõ | Có (nhạc nền) |
| Giọng đọc | Gemini TTS Flash | `gemini-3.8-flash-tts` | Agent Platform | **Preview** | Không (Preview) | Bản 15s/6s; master cân nhắc giọng người thật |
| Thăm dò | Flow | — | Web (gói AI Pro/Ultra) | — | **Không** | **Không** (watermark tại VN) |

**Thay đổi cần biết:** Veo 3.1 Fast/Quality trong Flow ngừng ngày **05/12/2026** (Flow chuyển sang Omni). Imagen đã ngừng trên Gemini API (vẫn còn trên Agent Platform).

## 12. Việc cần xác minh trước khi chạy thật

| # | Việc | Ai | Cách | Chặn việc gì |
|---|---|---|---|---|
| V1 | Nano Banana (2.1, Pro), Lyria, Omni có nằm trong diện bồi hoàn bản quyền không | P | Hỏi Google account rep, xin xác nhận bằng văn bản | Dùng Omni cho bản cuối |
| V2 | Điều kiện "output không bị chỉnh sửa" của bồi hoàn áp dụng ra sao khi shot Veo đã qua dựng/màu | LG | Đọc Service Specific Terms §20 + hỏi Google | Hiểu đúng phạm vi bảo vệ |
| V3 | Nghị định 142/2026: hình thức, vị trí, thời lượng nhãn AI bắt buộc trong video quảng cáo | LG | Đối chiếu văn bản gốc | Mẫu end card |
| V4 | Luật Quảng cáo 75/2025 + NĐ 342/2025: có yêu cầu riêng cho quảng cáo dùng AI / quảng cáo hàng không không | LG | Đối chiếu văn bản gốc | Cổng 3 |
| V5 | Quyền dùng ảnh/footage thật của hãng làm đầu vào AI; sự đồng ý của tiếp viên/phi công có trong ảnh | LG + BR | Kiểm tra hợp đồng chụp ảnh, model release | Production Bible |
| V6 | Veo 3.1 Fast có xuất 4K không (tài liệu và bảng giá mâu thuẫn) | AI | Chạy thử 1 lần | Không chặn (mặc định dùng 1080p) |
| V7 | Flow có hỗ trợ 9:16 không | AI | Thử trên Flow | Không chặn |
| V8 | Nano Banana hiển thị dấu tiếng Việt (chỉ ảnh hưởng chú thích storyboard) | AI | Chạy thử | Không chặn |
| V9 | Thông số phát sóng của đài (fps, loudness, định dạng) nếu có kế hoạch lên TV | P | Hỏi đài | Bản master TV |
| V10 | Gemini TTS bản GA có chưa (hiện là Preview) | P | Rà soát Model Registry | Dùng TTS cho master |

## 13. Template & tài liệu liên quan

| File | Dùng ở bước |
|---|---|
| [templates/01-brief.md](templates/01-brief.md) | 1 |
| [templates/02-brand-kit-gem.md](templates/02-brand-kit-gem.md) | 2, 4, 8 |
| [templates/03-prompt-structure.md](templates/03-prompt-structure.md) | 3, 4, 5, 6 |
| [templates/06-qc-checklist.md](templates/06-qc-checklist.md) | 5, 7, 9 |
| [templates/campaign-workbook.xlsx](templates/campaign-workbook.xlsx) — sheet Shot list, Shot log, QC, Ngân sách (bản CSV: `04-shot-list.csv`, `05-shot-log.csv`) | 2–9 |
| [pilot-plan.md](pilot-plan.md) | Trước khi áp dụng chính thức |

## 14. Lịch sử phiên bản

| Phiên bản | Ngày | Thay đổi |
|---|---|---|
| 1.0 | 2026-11-12 | Bản đầu tiên, trước pilot |
