# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.1] - 2026-11-09
### Fixed
- Sửa lỗi tìm kiếm tiêu đề phân biệt chữ hoa chữ thường (Refs #20).

## [1.0.0] - 2026-11-08
### Added
- Cart.print_cart(): Hiển thị chi tiết các sản phẩm trong giỏ hàng.
- search_by_title(): Hỗ trợ tìm kiếm đĩa DVD theo tiêu đề.
- total_cost_with_discount(): Hỗ trợ tính tổng tiền giỏ hàng có áp dụng phần trăm giảm giá.

### Fixed
- Giới hạn giỏ hàng (Issue #6): Ngăn nhận đĩa thứ 21 vượt quá MAX_NUMBERS_ORDERED (20 đĩa).
- Xử lý kiểm tra tham số phần trăm giảm giá hợp lệ từ 0 đến 100.
