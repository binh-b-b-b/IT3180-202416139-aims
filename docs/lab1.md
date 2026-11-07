Câu hỏi nhanh: cấu hình --global được lưu ở đâu? Khác gì so với --local?
--global lưu tại tệp ~/.gitconfig và có hiệu lực cho toàn bộ repository của người dùng. --local lưu tại .git/config nằm bên trong thư mục dự án, chỉ có tác dụng riêng cho repository đó và sẽ ưu tiên ghi đè lên các thiết lập --global
1. Vì sao dùng git mv?
báo rõ cho Git đây là đổi tên, giữ được lịch sử (--follow) và PR hiện renamed thay vì xóa + thêm.
2. release/lab01 có phải baseline không?
có, vì là phiên bản đã thống nhất, đóng băng, và là bản nộp.
3. Vì sao không commit thẳng master dù làm một mình?
đảm bảo branch master luôn trong trạng thái ổn định và sẵn sàng sản xuất, tạo thói quen tuân thủ quy trình chuẩn giúp kiểm tra, truy vết nguồn gốc thay đổi và khôi phục