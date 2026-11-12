# Checklist QC

- **Người kiểm:** QC Reviewer. **Không** được kiểm shot do chính mình tạo.
- **Khi nào:**
  - Phần **A–C**: từng shot, trước khi vào `04_shots/selects/` (Bước 5).
  - Phần **D–F**: bản dựng và từng file giao (Bước 7, 9).
- Một mục **Lỗi** ở A, B hoặc E = **loại**, không có ngoại lệ. Mục khác: ghi chú, Producer quyết.
- Ghi kết quả vào cột `qc_status` / `qc_by` của Shot log (shot) hoặc sheet `QC` của workbook (bản dựng).
- Xem từng shot ở **tốc độ thật**, rồi **từng khung** ở đoạn có chuyển động mạnh (tay, mặt, cánh, bánh xe).

## A. Kỹ thuật hàng không — *lỗi = loại*
- [ ] Đúng **dòng máy bay** trong brief (hình dáng mũi, thân dài/ngắn)
- [ ] Đúng **số động cơ**, vị trí động cơ
- [ ] Cửa sổ: hàng thẳng, khoảng cách đều, không biến dạng/thay đổi số lượng giữa các khung
- [ ] Winglet/sharklet, càng đáp, cánh tà đúng kiểu và không biến dạng
- [ ] Livery giữ nguyên như ảnh thật (không méo, không đổi màu, không chữ lạ)
- [ ] Hướng bay/lăn hợp lý: cất cánh hướng mũi lên, không bay lùi, bánh xe thu/thả đúng pha
- [ ] Cabin đúng cấu hình hạng ghế (số ghế/hàng, màu ghế, màn hình) của hãng
- [ ] Không có tàu bay/logo hãng khác lọt vào khung

## B. An toàn bay & hành vi — *lỗi = loại*
- [ ] Hành khách thắt dây an toàn khi cất cánh, hạ cánh, đèn thắt dây sáng
- [ ] Không có hành lý ở lối đi, cửa thoát hiểm bị chắn
- [ ] Bàn ăn, lưng ghế, rèm cửa sổ đúng vị trí theo pha bay
- [ ] Không dùng thiết bị điện tử sai quy định của hãng
- [ ] Không đứng/đi lại trong khoang khi không được phép
- [ ] Tiếp viên AI chỉ ở góc xa/từ phía sau; không cận mặt
- [ ] Đồng phục (nếu thấy) không sai chi tiết dễ nhận ra
- [ ] Không có hành vi nguy hiểm hoặc trái quy định trong sân bay (đi vào khu bay, chụp ảnh nơi cấm…)

## C. Lỗi đặc thù AI
- [ ] Tay, ngón tay đúng số lượng, không dính, không biến dạng khi cử động
- [ ] Mặt nhân vật không "trôi" (giống character sheet từ đầu đến cuối shot)
- [ ] Nhân vật giống chính họ ở các shot khác (so với Bible)
- [ ] Không có chữ "rác", ký tự lạ, logo giả trên biển hiệu, quần áo, màn hình
- [ ] Vật lý hợp lý: nước, tóc, vải, đồ uống, mây chuyển động tự nhiên
- [ ] Không có vật xuất hiện/biến mất giữa chừng; số lượng người/vật không đổi
- [ ] Không nhấp nháy, rung ảnh, đổi màu đột ngột
- [ ] Ánh sáng & màu khớp style frame và shot liền kề
- [ ] Không có watermark nhìn thấy được (dấu hiệu render nhầm từ Flow)
- [ ] Nhân vật không giống người nổi tiếng/người thật cụ thể

## D. Thương hiệu
- [ ] Logo đúng file gốc, đúng tỉ lệ, vùng an toàn, màu
- [ ] Font, màu chữ, đồ hoạ theo guideline
- [ ] Tone lời VO và chữ đúng Brand Kit; không có từ cấm
- [ ] Sonic logo/jingle đúng file, đúng vị trí
- [ ] Phụ đề khớp lời VO, không lỗi chính tả (VI có dấu đầy đủ)
- [ ] End card: logo + CTA + **nhãn AI**

## E. Pháp lý & claim — *lỗi = loại*
- [ ] Giá, khuyến mãi khớp brief và điều kiện đã được Legal duyệt
- [ ] Có dòng điều kiện áp dụng, đủ lâu và đủ lớn để đọc được
- [ ] Mọi claim so sánh/tuyệt đối có căn cứ đã lưu
- [ ] Dòng máy bay và đường bay thể hiện đúng với thực tế khai thác
- [ ] Nhãn AI có trên **mọi** phiên bản
- [ ] Mọi tư liệu thật, nhạc, SFX có quyền sử dụng
- [ ] Người thật xuất hiện (tiếp viên, phi công…) có model release

## F. Kỹ thuật file & âm thanh
- [ ] Đúng độ phân giải, tỉ lệ, fps theo SOP mục 2
- [ ] Loudness: −14 LUFS (online) / −23 LUFS (TV), true peak ≤ −1 dBTP
- [ ] VO nghe rõ trên nhạc; không méo, không clip
- [ ] 9:16: chữ, logo, CTA nằm trong vùng an toàn của Reels/TikTok/Shorts
- [ ] Bản EN: không sót chữ tiếng Việt trên màn hình; VO và phụ đề khớp
- [ ] Đúng tên file theo quy ước; đủ 6 file giao
- [ ] Metadata SynthID/C2PA còn nguyên (kiểm bằng công cụ đọc C2PA)
- [ ] Xem lại toàn bộ file xuất trên điện thoại (9:16) và màn hình lớn (16:9)
