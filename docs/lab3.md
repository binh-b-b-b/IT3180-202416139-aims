trả lời lab3

1. Merge base là gì?

Là nút tổ tiên trực hệ gần nhất giữa hai nhánh, đánh dấu thời điểm chúng phân rẽ (kiểm tra qua lệnh git merge-base A B).

Git sử dụng mốc này làm điểm chiếu giữa nhánh nguồn và nhánh đích nhằm phát hiện chính xác ai đã chỉnh sửa những gì so với điểm gốc.

Nếu chỉ một nhánh thay đổi nội dung, Git tự động cập nhật; ngược lại, cả hai cùng tác động vào một vị trí sẽ kích hoạt trạng thái xung đột .

Merge base quyết định trực tiếp phạm vi mã nguồn hiển thị trong mục diff; chọn nhầm mốc cơ sở sẽ khiến PR bị lẫn lộn các mã nguồn không liên quan.

2. Vì sao master/release/* phải dùng revert?

Các nhánh cốt lõi như master hay release/* đã được đồng đội chia sẻ và phụ thuộc. Thao tác reset sẽ bóp méo lịch sử, gây phân kỳ và bị cơ chế branch protection từ chối thẳng thừng.

Thay vì xóa bỏ quá khứ, lệnh này sinh ra một commit bù đắp mới giúp tiến trình lịch sử luôn tịnh tiến, dễ dàng kiểm toán nguyên nhân hoàn tác thông qua PR.

Bắt buộc phải kết hợp cờ -m 1 nhằm xác định nhánh cha gốc (như master) làm hệ quy chiếu, giúp giữ nguyên vẹn mạch chính và gỡ bỏ phần tính năng không mong muốn.

Lệnh reset chỉ dành riêng cho các thao tác cục bộ trên những commit chưa từng được đẩy lên kho lưu trữ chung.