trả lời lab4

1. Vì sao release/* không merge ngược vào master?

Nhánh release/* là một mốc đóng băng độc lập, trong khi master vẫn liên tục tiến hóa. Việc merge ngược sẽ mang theo các điều chỉnh riêng của bản phát hành vào nhánh chính, gây nhiễu phiên bản.

Mọi luồng phát triển đều xuất phát từ master. Khi cần khắc phục sự cố trên bản release, thay vì merge toàn bộ, ta chỉ chọn lọc và đưa bản vá sang thông qua lệnh cherry-pick -x.

Việc duy trì định hướng lịch sử độc lập một chiều giúp câu lệnh git log A..B phản ánh chính xác nội dung thực tế của từng phiên bản phát hành mà không bị chéo nhánh.

Câu 2: So sánh với GitFlow

GitFlow sử dụng song song hai nhánh chủ lực với cơ chế merge hai chiều phức tạp từ release/hotfix vào cả hai nhánh; trong khi mô hình này chỉ dùng duy nhất master làm gốc, nhánh release cắt ra và xử lý vá lỗi độc lập qua cherry-pick.

Release Flow loại bỏ sự rườm rà của GitFlow, mang lại sự đơn giản tối đa và khả năng kiểm soát linh hoạt khi duy trì đồng thời nhiều phiên bản phát hành song song.

GitFlow phù hợp với các chu kỳ phát hành định kỳ phức tạp, còn mô hình học phần này tối ưu cho việc bảo trì nhiều phiên bản hoặc triển khai các cột mốc theo tiến độ tuần.

Câu 3: Vì sao lên 1.0.0 mà không phải 0.4.0?

Các phiên bản dạng 0.y.z biểu thị giai đoạn thử nghiệm với API chưa ổn định. Cột mốc 1.0.0 đánh dấu sản phẩm chính thức đạt độ hoàn thiện và cam kết tương thích với người dùng.

Sau chuỗi Lab 01–03, hệ thống đã hoàn thiện toàn diện các chức năng cốt lõi (giỏ hàng, tìm kiếm, chính sách ưu đãi) kèm theo bộ kiểm thử và kiểm soát lỗi vững chắc.

Tăng PATCH khi vá lỗi (1.0.1) hoặc tăng MINOR khi bổ sung tính năng mới (1.1.0).