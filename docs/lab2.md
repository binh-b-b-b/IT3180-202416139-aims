Trả lời lab 2

Câu 1: Vì sao phải đồng bộ với master trước khi tạo PR?

Ngăn chặn xung đột từ gốc: Chủ động giải quyết các điểm tranh chấp mã nguồn ngay tại nhánh cá nhân, tuyệt đối không để xung đột lọt vào nhánh chính.

Đảm bảo tính toàn vẹn khi tích hợp

Tối ưu hóa quy trình Review: Giúp tệp diff của Pull Request chỉ tập trung độc lập vào phần code mình viết, giúp người kiểm duyệt dễ dàng nắm bắt logic 

Câu 2: Khi nào không được rebase?

Khi nhánh đã được chia sẻ và có người khác cùng tham gia: rebase sẽ làm thay đổi chuỗi mã băm của lịch sử, dẫn đến việc phải ép đẩy và làm lệch hướng nhánh làm việc chung của đồng đội.

Trên các nhánh nhánh cốt lõi, công khai (như master, main, release/*): Những nhánh này đóng vai trò là hồ sơ lịch sử chính thống, nghiêm cấm mọi hành vi viết lại lịch sử.

Khi PR đang trong giai đoạn chờ đánh giá : Việc thay đổi lịch sử commit giữa chừng sẽ làm mất đi sự đối ứng và ngữ cảnh của các đoạn bình luận từ người review.

Chỉ thực hiện rebase trên các nhánh nhánh riêng tư.

Câu 3: feature/* khác topic/* thế nào?

feature/* :

Dùng để xây dựng các chức năng cốt lõi hoặc tiện ích hướng tới người dùng cuối .

Trực tiếp tác động và làm thay đổi mã nguồn logic của ứng dụng, thường gắn liền với chuẩn thông điệp commit feat:.

topic/* :

Phục vụ cho các công việc bên lề không bổ sung tính năng mới .

Tập trung vào việc hoàn thiện tài liệu, cấu hình hệ thống, sơ đồ thiết kế hoặc chuẩn bị các nội dung hỗ trợ cho đợt phát hành.
