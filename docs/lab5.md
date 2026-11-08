1. Ưu, nhược điểm của upstream first so với release first?

upstream first (Khắc phục triệt để trên nhánh chính trước, sau đó cherry-pick ngược xuống bản phát hành):

Ưu điểm: Triệt tiêu hoàn toàn nguy cơ tái phát sinh lỗi trong các vòng đời sản phẩm tương lai nhờ mã nguồn luôn được kiểm định trên nền tảng mới nhất. Lý tưởng cho các hệ thống quy mô lớn vận hành theo sprint.

Nhược điểm: Do nhánh chính đã tiến xa, việc đưa bản vá xuống bản release dễ phát sinh xung đột hoặc vướng vào các phụ thuộc chưa có sẵn, làm chậm trễ thời gian phản hồi cho khách hàng.

release first (Xử lý trực tiếp trên nhánh phát hành, sau đó lan truyền ngược về master và các nhánh liên quan):

Ưu điểm: Cung cấp bản vá nhanh chóng, an toàn và chuẩn xác trên chính phiên bản đang vận hành thực tế mà không làm ảnh hưởng đến các tính năng đang phát triển dang dở.

Nhược điểm: Tiềm ẩn rủi ro bỏ sót quá trình đồng bộ sang các nhánh khác, đồng thời đòi hỏi nhiều thao tác cherry-pick thủ công dễ phát sinh xung đột (như trường hợp xử lý tại aims/search.py).

2. Nếu quên lan truyền bản sửa sang release/lab05, lệnh nào ở Phần F phát hiện?

Sử dụng bộ lọc thông điệp git log --all --oneline --grep "cherry picked from commit <FIX_SHA>" để kiểm tra; nếu chỉ trả về 1 kết quả duy nhất đồng nghĩa với việc nhánh release/lab05 chưa được cập nhật .

Đối chiếu trực tiếp qua git cherry: Lệnh git cherry -v origin/release/lab05 origin/release/lab04 sẽ hiển thị dấu cộng (+) trước commit sửa lỗi, chứng minh rằng bản tương đương vẫn vắng bóng trên nhánh đích.

Kiểm tra thông qua kiểm thử hành vi thực tế: Thực thi truy vấn tìm kiếm với từ khóa "lion" qua search_by_title nhưng kết quả trả về 0 thay vì 1 (vẫn dính lỗi ở phiên bản v1.1.0).

Điểm lưu ý kỹ thuật: Lệnh git tag --contains <FIX_SHA> không áp dụng được trong trường hợp này do cherry-pick sinh ra mã băm (SHA) mới hoàn toàn, khiến tag v1.1.0 không thể nhận diện được commit gốc mà chỉ ghi nhận ở mốc v1.0.1.