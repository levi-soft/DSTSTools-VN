# DSTSTool GUI v2

DSTSTool GUI là một ứng dụng giao diện đồ họa (GUI) được xây dựng bằng Python và PyQt6, cung cấp các công cụ để xử lý và chuyển đổi các định dạng file game phổ biến. Ứng dụng hỗ trợ xử lý hàng loạt với thanh tiến trình và xử lý lỗi.

## 📋 Mục lục

- [Tính năng chính](#-tính-năng-chính)
- [Cài đặt](#-cài-đặt)
- [Cách sử dụng](#-cách-sử-dụng)
- [Công cụ bên trong](#-công-cụ-bên-trong)
- [Nguồn gốc](#-nguồn-gốc)
- [Yêu cầu hệ thống](#-yêu-cầu-hệ-thống)
- [Đóng góp](#-đóng-góp)
- [Giấy phép](#-giấy-phép)

## 🚀 Tính năng chính

### 1. **CPK Tools** 📦
- **Giải nén Files**: Giải nén file CPK thành các file riêng lẻ
- **Đóng gói Files**: Đóng gói các file riêng lẻ thành file CPK
- **Xử lý hàng loạt**: Xử lý nhiều file cùng lúc
- **Theo dõi tiến trình**: Giám sát tiến trình xử lý theo thời gian thực

### 2. **MVGL Tools** 🎮
- **Giải nén MVGL**: Giải nén file MVGL thành các file riêng lẻ
- **Đóng gói MVGL**: Đóng gói file thành định dạng MVGL
- **Hỗ trợ DSCS**: Hỗ trợ định dạng DSCS
- **Tiến trình thời gian thực**: Theo dõi tiến trình chi tiết

### 3. **IMG Tools** 🖼️
- **IMG sang PNG**: Chuyển đổi file IMG sang PNG (Xử lý hàng loạt)
- **PNG sang IMG**: Chuyển đổi PNG sang IMG với nén BC7
- **Tích hợp Compressonator**: Sử dụng Compressonator CLI
- **Quản lý DDS**: Quản lý tự động file DDS

### 4. **MBE Tools** 📊
- **Giải nén MBE sang CSV**: Chuyển đổi MBE sang CSV (Xử lý hàng loạt)
- **Đóng gói CSV sang MBE**: Đóng gói CSV thành MBE (Xử lý hàng loạt)
- **Hiển thị số lượng file**: Hiển thị số lượng file đã xử lý
- **Xử lý metadata**: Xử lý metadata tự động

### 5. **TEXT Tools** 📝
- **Gộp CSV sang TSV**: Gộp nhiều CSV thành một TSV
- **Chia TSV sang CSV**: Chia TSV thành nhiều CSV
- **Escape ký tự xuống dòng**: Xử lý ký tự xuống dòng
- **Xử lý thư mục hàng loạt**: Xử lý thư mục hàng loạt

## 📦 Cài đặt

### Yêu cầu
- Python 3.8+
- PyQt6
- Các công cụ bên trong (đã được bao gồm)

### Cài đặt dependencies
```bash
pip install PyQt6
```

### Chạy ứng dụng
```bash
python DSTSToolGUIV2.py
```

## 📖 Cách sử dụng

### CPK Tools
1. **Giải nén Files**:
   - Chọn file CPK bằng nút "📄 Browse"
   - Chọn thư mục đích bằng nút "📂 Browse"
   - Nhấn "🚀 Extract Files"
   - Theo dõi thanh tiến trình

2. **Đóng gói Files**:
   - Chọn thư mục chứa files bằng nút "📂 Browse"
   - Chọn đường dẫn file CPK đầu ra bằng nút "💾 Browse"
   - Nhấn "🔧 Repack Files"
   - Theo dõi thanh tiến trình

### MVGL Tools
1. **Giải nén**:
   - Chọn file MVGL nguồn
   - Chọn thư mục đích
   - Nhấn "🚀 Extract Files"

2. **Đóng gói**:
   - Chọn thư mục chứa files
   - Chọn đường dẫn file MVGL đầu ra
   - Nhấn "🔧 Repack Files"

### IMG Tools
1. **IMG sang PNG**:
   - Chọn thư mục chứa file IMG
   - Chọn thư mục đích cho PNG
   - Nhấn "🔄 Convert to PNG"

2. **PNG sang IMG**:
   - Chọn thư mục chứa file PNG
   - Chọn thư mục đích cho IMG
   - Nhấn "🔄 Convert to IMG"

### MBE Tools
1. **Giải nén MBE sang CSV**:
   - Chọn thư mục chứa file .MBE
   - Chọn thư mục đích cho CSV
   - Nhấn "🚀 Extract Files"

2. **Đóng gói CSV sang MBE**:
   - Chọn thư mục chứa thư mục CSV
   - Chọn thư mục đích cho MBE
   - Nhấn "🔧 Repack Files"

### TEXT Tools
1. **Gộp CSV sang TSV**:
   - Chọn thư mục chứa CSV subdirectories
   - Chọn đường dẫn file TSV đầu ra
   - Nhấn "🔗 Merge CSV to TSV"

2. **Chia TSV sang CSV**:
   - Chọn file TSV nguồn
   - Chọn thư mục đích cho CSV
   - Nhấn "✂️ Split TSV to CSV"

## 🔧 Công cụ bên trong

DSTSTool GUI sử dụng các công cụ bên ngoài sau:

### Cấu trúc thư mục Tools
```
Tools/
├── compressonator/          # IMG Tools
├── DSCSTools/              # MVGL Tools
├── THL-MBE-Parser/         # MBE Tools
└── YACpkTool/              # CPK Tools
```

### File Dependencies
- **Compressonator CLI**: `compressonatorcli.exe`
- **DSCS Tools**: `DSCSToolsCLI.exe`
- **MBE Parser**: `MBE_Parser.py`, `MBE_Repacker.py`
- **YACpk Tool**: `YACpkTool.exe`, `CpkMaker.dll`

## 🔗 Nguồn gốc

DSTSTool GUI sử dụng các công cụ mã nguồn mở sau:

### 1. Compressonator
- **Nguồn**: https://github.com/GPUOpen-Tools/compressonator
- **Sử dụng**: IMG Tools - Chuyển đổi texture với nén BC7
- **Giấy phép**: MIT License

### 2. THL-MBE-Parser
- **Nguồn**: https://github.com/Ahtheerr/THL-MBE-Parser
- **Sử dụng**: MBE Tools - Parse và repack file MBE
- **Giấy phép**: MIT License

### 3. DSCSTools
- **Nguồn**: https://github.com/SydMontague/DSCSTools
- **Sử dụng**: MVGL Tools - Xử lý file MVGL/DSCS
- **Giấy phép**: MIT License

### 4. YACpkTool
- **Nguồn**: https://github.com/Brolijah/YACpkTool
- **Sử dụng**: CPK Tools - Extract và repack file CPK
- **Giấy phép**: MIT License

## 💻 Yêu cầu hệ thống

- **Hệ điều hành**: Windows 10/11
- **Python**: 3.8 trở lên
- **RAM**: 4GB tối thiểu, 8GB khuyến nghị
- **Lưu trữ**: 500MB cho ứng dụng và tools
- **Màn hình**: Độ phân giải tối thiểu 1280x720

## ⚠️ Lưu ý quan trọng

1. **Sao lưu Files**: Luôn sao lưu file gốc trước khi xử lý
2. **Quyền truy cập File**: Đảm bảo quyền đọc/ghi cho thư mục đích
3. **File lớn**: Một số file có thể mất nhiều thời gian xử lý
4. **Xử lý lỗi**: Ứng dụng sẽ hiển thị lỗi nếu có vấn đề
5. **Theo dõi tiến trình**: Theo dõi thanh tiến trình để biết tiến trình

## 🤝 Đóng góp

Chúng tôi hoan nghênh mọi đóng góp! Vui lòng:

1. Fork repository
2. Tạo feature branch (`git checkout -b feature/TinhNangTuyetVoi`)
3. Commit changes (`git commit -m 'Thêm tính năng tuyệt vời'`)
4. Push to branch (`git push origin feature/TinhNangTuyetVoi`)
5. Tạo Pull Request

## 📄 Giấy phép

DSTSTool GUI được phân phối dưới giấy phép MIT. Xem file `LICENSE` để biết thêm chi tiết.

---

**Tạo bởi**: Levi
**Phiên bản**: v2.0
**Ngày cập nhật**: 2025-01-19

*Ứng dụng này được phát triển để hỗ trợ cộng đồng modding game và xử lý file game một cách dễ dàng và hiệu quả.*