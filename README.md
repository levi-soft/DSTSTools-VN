# DSTSTool GUI

[![Version](https://img.shields.io/badge/version-1.0-blue.svg)](https://github.com)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Ứng dụng GUI hiện đại và mạnh mẽ để xử lý file .mvgl và .mbe với giao diện thân thiện và dễ sử dụng.

## ✨ Tính năng chính

### 📁 File .mvgl
- **Extract**: Chuyển đổi file .mvgl thành cấu trúc thư mục chứa data files
- **Repack**: Tạo lại file .mvgl từ thư mục chứa data files

### 📊 File .mbe
- **Extract**: Chuyển đổi file .mbe thành các file CSV có cấu trúc
- **Repack**: Tạo lại file .mbe từ nhiều file CSV
- **Batch Processing**: Xử lý nhiều file cùng lúc
- **Error Recovery**: Bỏ qua file lỗi và tiếp tục xử lý

### 🔧 Text Tools
- **Merge CSV → TSV**: Gộp nhiều file CSV thành 1 file TSV chuẩn
  - Tự động tạo metadata column (relative_path)
  - Giữ nguyên tên cột gốc từ CSV
  - Xử lý đúng xuống dòng và ký tự đặc biệt
- **Split TSV → CSV**: Tách file TSV thành cấu trúc thư mục CSV gốc
  - Khôi phục cấu trúc thư mục đầy đủ
  - Xử lý file trùng tên trong thư mục khác nhau

## 🚀 Cài đặt và sử dụng

### Yêu cầu hệ thống
- **OS**: Windows 10+
- **Python**: 3.7 hoặc cao hơn
- **RAM**: 512MB+
- **Disk**: 100MB dung lượng trống

## 📖 Hướng dẫn sử dụng

### Giao diện chính
Ứng dụng có 3 tab chính:
- **.mvgl Files**: Xử lý file .mvgl
- **.mbe Files**: Xử lý file .mbe
- **Text Tools**: Công cụ xử lý text

### Extract .mvgl
1. Chọn tab ".mvgl Files"
2. Chú ý phần "Extract File .mvgl"
3. Chọn file .mvgl nguồn
4. Chọn thư mục đích
5. Nhấn "Extract"

### Repack .mvgl
1. Chọn tab ".mvgl Files"
2. Chú ý phần "Repack thành File .mvgl"
3. Chọn thư mục chứa Data files
4. Chọn vị trí lưu file .mvgl
5. Nhấn "Repack"

### Extract .mbe
1. Chọn tab ".mbe Files"
2. Chú ý phần "Extract File .mbe"
3. Chọn file .mbe hoặc nhiều file .mbe
4. Chọn thư mục đích
5. Nhấn "Extract"

### Repack .mbe
1. Chọn tab ".mbe Files"
2. Chú ý phần "Repack thành File .mbe"
3. Chọn thư mục chứa CSV files
4. Chọn thư mục lưu file .mbe
5. Nhấn "Repack"

## 🔧 Công nghệ sử dụng

- **Python 3.7+**: Ngôn ngữ lập trình chính
- **PyQt6**: Framework GUI hiện đại
- **PyInstaller**: Công cụ đóng gói executable
- **Struct**: Xử lý dữ liệu nhị phân
- **CSV**: Xử lý file CSV/TSV

## 📋 Thông số kỹ thuật

### File .mbe Format
- **Magic Number**: 'EXPA'
- **Column Types**: Int, IntID, byte, float, String, StringID
- **Alignment**: 8-byte cho String/StringID, 4-byte cho các loại khác
- **Padding**: 0xCC bytes giữa các rows

### File .mvgl Format
- Hỗ trợ extract thành data files
- Hỗ trợ repack từ data files

## 📝 License

Dự án này được phân phối dưới giấy phép MIT. Xem file [`LICENSE`](LICENSE) để biết thêm chi tiết.

### Điều khoản chính của MIT License:
- ✅ **Sử dụng miễn phí** cho mục đích cá nhân và thương mại
- ✅ **Chỉnh sửa** và phân phối lại code
- ✅ **Bao gồm thông báo bản quyền** trong tất cả bản sao
- ⚠️ **Không có bảo đảm** về chất lượng hoặc tính năng
- ⚠️ **Không chịu trách nhiệm** về thiệt hại hoặc vấn đề phát sinh

## 👨‍💻 Tác giả

**Levi** - *Developer & Maintainer*

- Email: nguyenthaitrunghieu@gmail.com
- GitHub: [@levi-soft](https://github.com/levi-soft)

## 🙏 Lời cảm ơn

- Cảm ơn cộng đồng open source
- Cảm ơn người dùng đã sử dụng và góp ý

## 📞 Liên hệ

Nếu bạn có câu hỏi hoặc cần hỗ trợ:

- Tạo Issue trên GitHub
- Gửi email đến tác giả
- Tham gia cộng đồng Discord/Slack (nếu có)

---

**⭐ Nếu bạn thấy dự án hữu ích, hãy cho chúng tôi một ngôi sao!**