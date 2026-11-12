# SOP — Sản xuất video quảng cáo hàng không bằng AI của Google

| | |
|---|---|
| **Phiên bản** | 1.0.1 (đã review góc nhìn làm phim, chưa qua pilot) |
| **Ngày** | 2026-11-12 |
| **Áp dụng cho** | `[HÃNG]` — mọi chiến dịch video quảng cáo |
| **Chủ sở hữu tài liệu** | Producer |
| **Rà soát** | Model Registry (mục 11): hằng tháng · Toàn bộ SOP: sau pilot, sau đó mỗi quý |

> Tài liệu viết dạng chung với placeholder `[HÃNG]`. Mọi đặc thù thương hiệu (tone, đội tàu bay, slogan, quy tắc giá…) nằm trong **Brand Kit** — xem [templates/02-brand-kit-gem.md](templates/02-brand-kit-gem.md).

---

## 1. Mục đích & phạm vi

Quy trình **lặp lại được** để một team creative sản xuất một **bộ video quảng cáo** cho mỗi chiến dịch trong **5 ngày làm việc + 1 ngày dự phòng** (để sửa theo góp ý ở cổng cuối), với chi phí AI **≤ 500 USD/bộ** (chưa tính nhân sự).

- **Tạo nội dung** (kịch bản, ảnh, video, nhạc, giọng đọc): dùng AI của Google.
- **Hậu kỳ** (dựng, màu, đồ hoạ, mix, xuất file): Premiere Pro + After Effects.
- **Tự động hoá bằng API**: ngoài phạm vi phiên bản này — sẽ làm sau khi chạy tay 1–2 chiến dịch.

## 2. Bộ sản phẩm chuẩn mỗi chiến dịch

| Mã | Phiên bản | Tỉ lệ | Độ dài | Ngôn ngữ | Kênh |
|---|---|---|---|---|---|
| M30-VI / M30-EN | Master | 16:9 | 30s | VI / EN | YouTube, TV online, màn hình sân bay |
| C15-VI / C15-EN | Social 15s (**kịch bản riêng**, không chỉ là bản cắt ngắn) | 9:16 | 15s | VI / EN | Reels, TikTok, Shorts |
| C06-VI / C06-EN | Bumper (kịch bản riêng) | 9:16 | 6s | VI / EN | Reels, TikTok, Shorts, YouTube bumper (16:9 nếu cần) |

> Trên social, bản 15s 9:16 thường là bản có nhiều lượt xem nhất. Vì vậy C15 và C06 được **viết và duyệt cùng lúc với kịch bản 30s** (Bước 2, Cổng 1), dùng chung bộ shot nhưng có lời VO, nhịp và câu mở đầu riêng.

**Thông số giao file**

| Hạng mục | Master | Social |
|---|---|---|
| File | ProRes 422 HQ (.mov) + H.264 (.mp4) | H.264 High (.mp4) |
| Độ phân giải | 1920×1080 (3840×2160 nếu mọi shot render 4K) | 1080×1920 (9:16) |
| Khung hình | **Chốt ở brief.** Không lên TV: 24 fps xuyên suốt (Veo xuất 24 fps). Có lên TV (VN thường 25 fps): dựng trên **timeline 25 fps ngay từ đầu**, cho clip 24 fps chạy ở 25 fps (interpret footage — hình nhanh ~4%, mắt khó nhận ra; VO/nhạc làm riêng nên không đổi cao độ). **Không** đổi tốc độ cả bản dựng ở bước cuối (spot 30s sẽ còn ~28,8s) và không nội suy khung (giật hình). Spot TV phải đúng khung thời lượng; slate/clock, mức tín hiệu theo yêu cầu đài (V9) | 24 fps (hoặc theo timeline master nếu master là 25 fps) |
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
| Producer | **P** | Giao việc hằng ngày theo lịch và báo hạn mới nếu trễ; tổ chức 4 cổng duyệt (hẹn người duyệt, gửi đúng thứ cần duyệt, gom góp ý thành một danh sách sửa, ghi lại ai đồng ý lúc nào); book người đọc VO nếu dùng giọng thật; quản lý ngân sách, Shot log, giao file; sở hữu SOP và Model Registry |
| Director / Creative Lead | **DIR** | Chịu trách nhiệm **chất lượng sáng tạo** của phim: viết treatment, duyệt style frame và khung đầu, chọn take, quyết nhịp dựng và hướng màu. Có mặt ở cả 4 cổng. Có thể do CW hoặc AI Artist kiêm, nhưng phải là **một người cụ thể** — Gem chỉ là trợ lý, không phải người quyết |
| Creative / Copywriter | **CW** | Ý tưởng, kịch bản 30s/15s/6s, lời VO, chữ trên màn hình (VI + EN) |
| AI Artist | **AI** | Storyboard, Production Bible, khung đầu, tạo shot video |
| Editor | **ED** | Âm thanh (nhạc Lyria, VO nháp/TTS, SFX), animatic, rough cut, màu, đồ hoạ, mix, phiên bản, xuất file |
| QC Reviewer | **QC** | Chạy checklist QC từng shot và bản dựng |
| Brand Approver (phía hãng) | **BR** | Duyệt ở 4 cổng |
| Legal | **LG** | Xem trước chữ giá/claim ở cổng 3; duyệt cổng 4: claim, giá, khuyến mãi, ghi nhãn AI, quyền sử dụng tư liệu |

> **Vì sao âm thanh chuyển sang Editor:** AI Artist đã gánh Bible, khung đầu và toàn bộ shot video — là điểm nghẽn của Ngày 3–4. Nhạc quyết định nhịp dựng, nên người dựng nắm luôn nhạc và VO. Team có người làm âm thanh riêng thì giao cho người đó.

R = làm · A = chịu trách nhiệm cuối · C = được hỏi ý kiến · I = được thông báo

| Bước | P | DIR | CW | AI | ED | QC | BR | LG |
|---|---|---|---|---|---|---|---|---|
| 1. Brief | A | C | C | I | I | | C | C |
| 2. Ý tưởng & kịch bản | A | C | R | C | | | C | |
| 3. Storyboard + Treatment | A | R | C | R | | | | |
| **Cổng 1** | R | C | C | | | | A | |
| 4. Production Bible + Nhạc + Animatic | A | C | C | R | R | | | |
| **Cổng 2** | R | C | C | | C | | A | |
| 5. Tạo shot video | A | C (chọn take) | | R | C | R | | |
| 6. Âm thanh hoàn thiện | A | C | C | | R | | | |
| 7a. Rough cut | A | C | C | C | R | | | |
| **Cổng 3** | R | C | | | C | | A | C |
| 7b. Hoàn thiện master | A | C | | | R | R | | |
| 8. Phiên bản | A | C | R (chữ EN) | | R | R | | |
| 9. QC & giao | A | | | | R | R | | |
| **Cổng 4** | R | C | | | C | C | A | A |

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
- **Hai quyết định kỹ thuật phải chốt ngay ở brief** (đổi về sau rất tốn kém):
  1. **Giọng đọc bản master:** TTS hay người đọc thật. Nếu người thật → Producer book người đọc + phòng thu cho **Ngày 3** (sau khi lời VO được khoá ở Cổng 2). Với bản master của hãng bay, khuyến nghị dùng giọng thật; TTS dùng cho nháp, social và bản EN nếu BR đồng ý.
  2. **Có phát TV không** → quyết định fps của timeline (24 hay 25 fps, xem mục 2) và hỏi đài thông số (V9).
- **Output:** Brief được Brand Approver ký xác nhận.
- **Lưu ý:** Nếu brief nhắc tới giá/khuyến mãi → gửi Legal xem trước điều kiện ngay từ bước này, đừng đợi cổng cuối.

### Bước 2 — Ý tưởng & kịch bản
- **Công cụ:** Gem Brand Kit.
- **Việc làm:**
  1. Đưa brief vào Gem, yêu cầu **3–5 hướng ý tưởng** (mỗi hướng: tên, insight, tóm tắt 3 câu, cảnh chủ đạo, rủi ro sản xuất bằng AI).
  2. Producer + CW + Director chọn 1 hướng (có thể gửi BR chọn).
  3. Gem viết **kịch bản 30s + shot list**: mỗi shot có thời lượng, mô tả hình, góc máy, lời VO, chữ trên màn hình, nguồn hình (AI / Thật / Hybrid), có phải hero shot không.
  4. Gem viết **kịch bản 15s và 6s riêng** (không phải gợi ý cắt): mỗi bản có thứ tự shot (cột `used_in` của Shot list), lời VO riêng và chữ trên màn hình riêng. Yêu cầu cho bản social:
     - **Câu mở đầu (hook) trong 1–2 giây đầu**: hình mạnh nhất hoặc câu hỏi/khẳng định gây tò mò, không mở bằng logo.
     - **Hiểu được khi tắt tiếng**: thông điệp chính nằm ở chữ trên màn hình và hình, VO chỉ bổ trợ.
     - C15: VO tối đa ~11s, end card 2–3s. C06: một ý duy nhất, có thể không VO, end card ~2s.
  5. CW chỉnh tay lời VO tiếng Việt cho tự nhiên. Lời VO 30s chiếm tối đa ~24s; độ dài thực đo lại ở animatic.
- **Output:** Kịch bản 30s / 15s / 6s + Shot list (sheet `Shot list` trong workbook, cột `used_in` ghi shot nằm ở bản nào).
- **Quy tắc shot list:**
  - Đánh dấu **hero shot** (3–5 shot đắt giá nhất, gồm các shot dùng làm hook của C15/C06) → sẽ được tạo riêng ở cả 16:9 và 9:16.
  - Shot còn lại dàn cảnh **center-safe** (chủ thể ở giữa khung) để crop sang 9:16.
  - Shot có tàu bay/logo → nguồn **Thật** hoặc **Hybrid** (ảnh thật làm khung đầu).
  - Shot có tiếp viên → chỉ góc xa/từ phía sau, hoặc nguồn **Thật**.
  - Cột thời lượng là **thời lượng dùng trong phim**. Clip tạo bằng Veo phải dài hơn để có **phần dư (handles)** — xem Bước 5.

### Bước 3 — Storyboard + Treatment
- **Storyboard** (AI Artist, Nano Banana 2.1 — nhanh, rẻ): mỗi shot 1 khung 16:9; **hero shot thêm khung 9:16**. Ghép thành bảng storyboard (Google Slides hoặc PDF) kèm lời VO dưới mỗi khung, và một trang thứ tự shot cho C15/C06.
- **Treatment 1 trang** (Director): cách kể bằng hình của phim, gồm:
  - Moodboard 6–10 ảnh tham chiếu (phim, quảng cáo, ảnh chụp) + điều muốn lấy ở mỗi ảnh.
  - Ống kính & chuyển động máy (VD: 35–50mm, máy chậm, nhiều locked-off).
  - Bảng màu và ánh sáng (giờ trong ngày, nhiệt độ màu).
  - Nhịp dựng và hướng nhạc (tempo gợi ý, cảm xúc từng đoạn).
  - Hình mẫu nhân vật (casting AI): tuổi, phong cách, đa dạng phù hợp khán giả mục tiêu.
- **2–3 style frame sơ bộ** (AI Artist + Director, Nano Banana Pro): để phía hãng thấy **chất lượng hình thật sự** của phim. Storyboard nháp chỉ thể hiện bố cục; nếu chỉ gửi storyboard, người duyệt dễ đánh giá sai hướng.
- **Output:** Storyboard PDF + Treatment + style frame sơ bộ.

> ### 🚦 Cổng duyệt 1 — Kịch bản + Storyboard + Treatment (cuối Ngày 1)
> **Người duyệt:** Brand Approver. **Duyệt:** ý tưởng, thông điệp, kịch bản **30s, 15s và 6s**, lời VO, trình tự cảnh, treatment và style frame sơ bộ, hướng giọng đọc (TTS/người thật). Tối đa **1 vòng sửa trong ngày**; quá → lịch lùi.

### Bước 4 — Production Bible + Nhạc + Animatic

**4a. Production Bible** — bộ tham chiếu được duyệt **trước khi tạo bất kỳ shot video nào**. Lưu ở `02_bible/`. Director duyệt từng mục trước khi gửi Cổng 2.

| Mục | Nội dung | Nguồn |
|---|---|---|
| Tàu bay | Ảnh thật đúng **dòng máy bay** xuất hiện trong phim: ngoại thất nhiều góc, cabin từng hạng ghế | Thư viện ảnh của hãng |
| Nhân vật | Character sheet 2–4 hành khách AI: mặt, trang phục, 4–6 góc (chính diện, 3/4, nghiêng, toàn thân) | Nano Banana Pro |
| Điểm đến | Ảnh tham chiếu từng địa điểm (cảnh, giờ trong ngày) | Ảnh thật có quyền sử dụng + Nano Banana Pro |
| Style frame | 3–5 khung chuẩn về màu, ánh sáng, ống kính, độ tương phản — đây là **đích màu cuối cùng** Editor chỉnh màu theo | Nano Banana Pro |
| Khung đầu | Khung hình đầu của **từng shot** (và khung cuối nếu cần), 16:9 và 9:16 với hero shot. Tạo với **màu trung tính, tương phản mềm** (xem "Chừa chỗ chỉnh màu" ở Bước 5) | Nano Banana Pro, dùng ảnh Bible làm tham chiếu |

Quy tắc Bible:
- Nhân vật AI **không được giống người nổi tiếng hay người thật** cụ thể.
- Ảnh thật có người (tiếp viên, phi công) dùng làm tham chiếu → phải có **sự đồng ý của người trong ảnh** (xem mục 12).
- Mỗi lần dùng tham chiếu ghi vào cột `refs` của Shot log.

**4b. Nhạc — chốt trước khi dựng animatic**
- Nhạc quyết định nhịp dựng, nên được chọn **trước** animatic, không ghép vào sau.
- Editor tạo 3–5 bản nhạc **không lời** bằng Lyria theo treatment: ghi rõ **tempo (BPM)**, cấu trúc theo giây khớp kịch bản 30s, và **điểm kết rõ ràng** trùng thời điểm vào end card, chừa chỗ cho sonic logo (xem [templates/03-prompt-structure.md](templates/03-prompt-structure.md)).
- Director + Producer chọn 1 bản. Bản này đi vào animatic và Cổng 2; sau Cổng 2 chỉ chỉnh độ dài/mix, không đổi bài (trừ khi BR yêu cầu).

**4c. Animatic**
- **Việc làm:** Editor dựng các khung đầu **theo nhịp của bản nhạc đã chọn** (điểm cắt rơi vào phách), đúng thời lượng shot list, kèm VO nháp Gemini TTS. Có thể dùng vài clip Veo Fast/Omni giá rẻ cho shot có chuyển động phức tạp.
- Làm animatic cho cả **30s và 15s** (15s dùng thứ tự shot đã duyệt ở Cổng 1, khung 9:16).
- **Mục đích:** bắt lỗi nhịp, thời lượng VO, logic câu chuyện **trước khi** tiêu tiền render bản cuối.
- **Output:** Animatic 30s + 15s (MP4).

> ### 🚦 Cổng duyệt 2 — Animatic (cuối Ngày 2)
> **Người duyệt:** Brand Approver + quản lý marketing. **Duyệt:** nhịp, thời lượng, nhạc, Production Bible (nhân vật, style). Sau cổng này **khoá shot list và khoá lời VO** (để thu giọng thật ở Ngày 3) — thêm shot hay đổi lời phải qua Producer và tính lại ngân sách, thời gian.

### Bước 5 — Tạo shot video
- **Công cụ:** Veo 3.1 Fast (thử prompt) → Veo 3.1 Standard (bản cuối), qua Agent Platform.
- **Việc làm:**
  1. Viết prompt theo cấu trúc chuẩn [templates/03-prompt-structure.md](templates/03-prompt-structure.md) — **prompt viết bằng tiếng Anh**.
  2. Luôn dùng **image-to-video**: khung đầu từ Bible (+ khung cuối nếu cần kiểm soát chuyển động) và ảnh tham chiếu nhân vật.
  3. **Tắt tạo âm thanh** của Veo theo mặc định (âm thanh làm riêng ở bước 6) — giảm ~50% chi phí. Chỉ bật khi cần âm thanh môi trường đặc thù.
  4. **Tạo dư thời lượng (handles):** nửa giây đầu và cuối của clip AI thường lỗi hoặc chuyển động chưa ổn định. Shot dùng ≤ 4s → tạo clip 6s; dùng 5–6s → tạo 8s; shot cần dùng > 6s → tách thành 2 shot.
  5. **Chừa chỗ chỉnh màu:** file Veo là 8-bit, màu gần như "nướng" vào hình — đẩy màu mạnh ở hậu kỳ sẽ vỡ. Khung đầu và prompt yêu cầu **màu trung tính, tương phản mềm, giữ chi tiết vùng sáng và vùng tối**; look cuối cùng làm ở hậu kỳ theo style frame.
  6. **Fast chỉ để thử prompt, không phải bản xem trước chính xác.** Fast và Standard là hai model khác nhau: cùng prompt, khung đầu và seed vẫn có thể cho bố cục, chuyển động khác nhau. Dùng Fast để chốt prompt và khung đầu/cuối; 3 lần Standard mới là vòng chọn thật. Seed vẫn ghi lại để tạo lại **trong cùng một model** (kiểm chứng ở pilot — V11).
  7. Theo **giới hạn số lần tạo** (mục 8.2).
  8. Ghi mọi lần tạo vào Shot log.
  9. Director chọn take → QC Reviewer chạy checklist phần A–C ([templates/06-qc-checklist.md](templates/06-qc-checklist.md)) → đạt mới chuyển vào `04_shots/selects/`.
- **Output:** Các shot đã qua QC, đủ cho bản master và hero shot 9:16.

### Bước 6 — Âm thanh hoàn thiện
Nhạc đã chọn ở Bước 4b. Bước này do **Editor** làm, song song với Bước 5 trong Ngày 3.

| Thành phần | Công cụ | Ghi chú |
|---|---|---|
| Nhạc nền | Bài Lyria đã chọn ở 4b | Chỉnh độ dài cho bản 30s/15s/6s (cắt theo phách, giữ điểm kết). **Chỉ nhạc không lời.** |
| Giọng đọc master | Người đọc thật **hoặc** Gemini TTS — theo quyết định ở brief | Người thật: thu ở Ngày 3 theo lời VO đã khoá ở Cổng 2, thu cả VO 15s/6s trong cùng buổi |
| Giọng đọc khác | Gemini TTS | Bản EN (nếu BR đồng ý dùng TTS), nháp |
| Sonic logo / jingle | File thật của hãng | Luôn ở cuối, không tạo bằng AI |
| SFX | Thư viện SFX có bản quyền (hoặc audio Veo nếu đã bật) | Tiếng động cơ, thông báo cabin… phải đúng ngữ cảnh |

### Bước 7 — Dựng (Rough cut → Hoàn thiện)

**7a. Rough cut** (Ngày 3–4) — Editor bắt đầu dựng ngay khi shot đầu tiên vào `selects/`.
- Dựng **30s và 15s** theo animatic đã duyệt, bằng các shot đã đạt QC, nhạc đã chọn và VO bản cuối (hoặc VO nháp nếu chưa thu xong).
- Chưa chỉnh màu, chưa mix kỹ. Chữ giá/claim/CTA đặt dạng **chữ tạm** để Legal xem trước.
- Mục đích: phía hãng thấy **chuyển động AI thật** lần đầu — ảnh tĩnh ở animatic không lộ được cảm giác "là lạ" của chuyển động AI.

> ### 🚦 Cổng duyệt 3 — Rough cut / Khoá hình (cuối Ngày 4)
> **Người duyệt:** Brand Approver (A) + Director; Legal xem trước chữ giá, điều kiện, claim. **Duyệt:** shot đã chọn, chuyển động, nhịp, thời lượng 30s và 15s. Tối đa **1 vòng sửa trong ngày**.
> Sau cổng này là **khoá hình (picture lock)**: chỉ còn chỉnh màu, đồ hoạ, mix. Đổi shot sau khoá hình = yêu cầu thay đổi — Producer tính lại chi phí và thời gian, BR đồng ý mới làm.

**7b. Hoàn thiện master** (Ngày 5 sáng)
- **Công cụ:** Premiere Pro + After Effects. Timeline đúng fps đã chốt ở brief (mục 2).
- **Việc làm:** chỉnh màu đồng nhất theo style frame → làm khớp footage thật với shot AI (grain, độ nét, motion blur) → chèn đồ hoạ từ **template MOGRT** (logo, khung giá, CTA, phụ đề, end card có sẵn **nhãn AI**) → mix (nhạc, VO, SFX, sonic logo) → xuất bản master.
- **Template MOGRT bắt buộc có:** end card (logo + CTA + nhãn AI), khung giá & điều kiện, tên điểm đến, phụ đề VI/EN, lower third.
- QC Reviewer chạy checklist phần D–F trên bản dựng.

### Bước 8 — Phiên bản
1. **15s và 6s 9:16:** hoàn thiện theo **kịch bản và rough cut đã duyệt** (không quyết lại nội dung ở bước này) — hero shot 9:16 + crop các shot center-safe. Kiểm tra vùng an toàn.
2. **Bản tiếng Anh:** giữ nguyên hình; thay VO (TTS hoặc người đọc), phụ đề, chữ trên màn hình. CW chịu trách nhiệm bản chuyển thể — **không dịch máy nguyên văn** lời VO. Nên viết bản EN ngay sau Cổng 2 để kịp thu cùng buổi với VO tiếng Việt.
3. Xuất đủ 6 file theo bảng mục 2.

### Bước 9 — QC & giao file
- QC Reviewer chạy **toàn bộ** checklist trên cả 6 file.
- Producer đóng gói `07_deliverables/` + Shot log + báo cáo chi phí.

> ### 🚦 Cổng duyệt 4 — Bản cuối (cuối Ngày 5)
> **Người duyệt:** Brand Approver **và** Legal (bắt buộc cả hai).
> **Legal kiểm:** giá vé & điều kiện khuyến mãi, claim ("rẻ nhất", "đúng giờ nhất"… phải có căn cứ), dòng máy bay/đường bay thể hiện đúng thực tế, nhãn AI, quyền sử dụng tư liệu và nhạc.
> Sửa theo góp ý và giao file ở **Ngày 6 (dự phòng)**. Không cần sửa → giao ngay cuối Ngày 5.

## 7. Lịch 5 ngày + 1 ngày dự phòng

| Ngày | Việc | Kết thúc bằng |
|---|---|---|
| **1** | Brief (chốt giọng đọc, fps) → Ý tưởng → Kịch bản 30s/15s/6s + Shot list → Storyboard + Treatment + style frame sơ bộ | 🚦 Cổng 1 |
| **2** | Production Bible (nhân vật, style, khung đầu) · Nhạc Lyria (chốt) → Animatic 30s + 15s theo nhạc | 🚦 Cổng 2 → khoá shot list, khoá lời VO |
| **3** | Tạo shot (Fast thử prompt → Standard) → QC từng shot · Thu VO / TTS bản cuối, SFX · Editor dựng thô dần | |
| **4** | Tạo nốt shot + hero shot 9:16 → Rough cut 30s + 15s | 🚦 Cổng 3 → khoá hình |
| **5** | Màu → Đồ hoạ → Mix master → Hoàn thiện 15s/6s → Bản EN → QC toàn bộ | 🚦 Cổng 4 |
| **6** *(dự phòng)* | Sửa theo góp ý Cổng 4 → Giao | |

Mỗi cổng: tối đa **1 vòng sửa trong ngày**. Vượt → lịch lùi theo, Producer báo lại hạn cho BR. Cam kết với hãng là **5 ngày + 1 ngày dự phòng**, không hứa 5 ngày tròn.

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
  ├─ Tối đa 3 lần Veo 3.1 Fast   → chốt prompt & khung đầu/cuối? ┐
  │                                                             ▼
  ├─ Tối đa 3 lần Veo 3.1 Standard (cùng prompt/khung đầu đã chốt — đây là vòng chọn thật)
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

Thời lượng trong bảng là **thời lượng tạo** (đã gồm handles, Bước 5), không phải thời lượng dùng trong phim. Trần **$500** gồm cả dự phòng cho shot khó. Vượt **$400** → Producer báo BR trước khi tiếp tục.

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
| V4 | Luật Quảng cáo 75/2025 + NĐ 342/2025: có yêu cầu riêng cho quảng cáo dùng AI / quảng cáo hàng không không | LG | Đối chiếu văn bản gốc | Cổng 4 |
| V5 | Quyền dùng ảnh/footage thật của hãng làm đầu vào AI; sự đồng ý của tiếp viên/phi công có trong ảnh | LG + BR | Kiểm tra hợp đồng chụp ảnh, model release | Production Bible |
| V6 | Veo 3.1 Fast có xuất 4K không (tài liệu và bảng giá mâu thuẫn) | AI | Chạy thử 1 lần | Không chặn (mặc định dùng 1080p) |
| V7 | Flow có hỗ trợ 9:16 không | AI | Thử trên Flow | Không chặn |
| V8 | Nano Banana hiển thị dấu tiếng Việt (chỉ ảnh hưởng chú thích storyboard) | AI | Chạy thử | Không chặn |
| V9 | Thông số phát sóng của đài (fps, loudness, định dạng) nếu có kế hoạch lên TV | P | Hỏi đài | Bản master TV |
| V10 | Gemini TTS bản GA có chưa (hiện là Preview) | P | Rà soát Model Registry | Dùng TTS cho master |
| V11 | Cùng prompt + khung đầu + seed, Veo Fast và Veo Standard có cho bố cục/chuyển động giống nhau không; seed có tạo lại đúng clip trong cùng model không | AI | Chạy thử 2–3 shot ở pilot | Không chặn (SOP đã giả định là **không** giống) |

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
| 1.0.1 | 2026-11-12 | Review góc nhìn làm phim: thêm vai Director/Creative Lead + treatment; thêm **Cổng 3 rough cut / khoá hình** (cổng bản cuối thành Cổng 4); chốt giọng đọc và fps ngay ở brief; chọn nhạc trước animatic, dựng animatic theo nhạc; kịch bản 15s/6s viết và duyệt ở Cổng 1; tạo clip có handles, màu trung tính để chỉnh màu, Fast chỉ để thử prompt (V11); âm thanh chuyển sang Editor; lịch 5 ngày + 1 ngày dự phòng |
