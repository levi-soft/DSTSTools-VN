# DSTSTool GUI v2

[![Phiên bản](https://img.shields.io/badge/phiên%20bản-2.0-blue.svg)](https://github.com/levi-soft/DSTSTools-VN)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Giấy phép](https://img.shields.io/badge/giấy%20phép-MIT-green.svg)](LICENSE)
[![Nền tảng](https://img.shields.io/badge/nền%20tảng-Windows-lightgrey.svg)](https://www.microsoft.com/windows)

**DSTSTool GUI v2** là một ứng dụng giao diện đồ họa (GUI) toàn diện được xây dựng bằng Python và PyQt6, chuyên dành cho việc modding game Digimon Story: Time Stranger. Ứng dụng cung cấp bộ công cụ mạnh mẽ để xử lý và chuyển đổi các định dạng file game phổ biến, hỗ trợ xử lý hàng loạt với giám sát tiến trình thời gian thực và xử lý lỗi thông minh.

## 🌐 Language Support / Hỗ trợ Ngôn ngữ

📖 **For English users** / **Dành cho người dùng tiếng Anh**: [Click here to read in English](README.md)

Tài liệu này có sẵn bằng cả tiếng Việt và tiếng Anh. Chọn ngôn ngữ bạn muốn ở trên.

## 🎯 Mục đích và Lợi ích

DSTSTool GUI v2 được thiết kế đặc biệt để:
- **Đơn giản hóa quá trình modding**: Giao diện trực quan giúp người dùng dễ dàng thao tác với file game
- **Tăng hiệu suất**: Xử lý hàng loạt và đa luồng giúp tiết kiệm thời gian đáng kể
- **Đảm bảo an toàn**: Sao lưu tự động và kiểm tra tính toàn vẹn file
- **Hỗ trợ cộng đồng**: Công cụ mã nguồn mở phục vụ cộng đồng modding game

## 📋 Mục lục

- [Tính năng chính](#-tính-năng-chính)
- [Kiến trúc & Quy trình](#-kiến-trúc--quy-trình)
- [Định dạng file được hỗ trợ](#-định-dạng-file-được-hỗ-trợ)
- [Cài đặt](#-cài-đặt)
- [Cách sử dụng](#-cách-sử-dụng)
- [Công cụ bên trong](#-công-cụ-bên-trong)
- [Nguồn gốc & Lời cảm ơn](#-nguồn-gốc--lời-cảm-ơn)
- [Yêu cầu hệ thống](#-yêu-cầu-hệ-thống)
- [Khắc phục sự cố](#-khắc-phục-sự-cố)
- [Đóng góp](#-đóng-góp)
- [Nhật ký thay đổi](#-nhật-ký-thay-đổi)
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

## 🏗️ Kiến trúc & Quy trình

### Kiến trúc ứng dụng
```
DSTSTool GUI v2/
├── DSTSToolGUIV2.py          # Ứng dụng chính & framework GUI
├── CPKTool.py               # Module xử lý archive CPK
├── MVGLTool.py              # Module xử lý file MVGL/DSCS
├── IMGTool.py               # Module chuyển đổi hình ảnh
├── MBETool.py               # Module xử lý dữ liệu MBE
├── TEXTTool.py              # Module xử lý text/CSV
├── Tools/                   # Thư mục công cụ bên thứ ba
│   ├── compressonator/      # Nén texture GPU
│   ├── DSCSTools/          # Xử lý archive MVGL/DSCS
│   ├── THL-MBE-Parser/     # Parser file MBE
│   └── YACpkTool/          # Công cụ xử lý CPK
└── icon.ico                 # Biểu tượng ứng dụng
```

### Quy trình xử lý
1. **Giao diện người dùng**: GUI PyQt6 với hệ thống tab
2. **Xử lý đa luồng**: Worker threads cho tác vụ nặng
3. **Tích hợp công cụ**: Gọi executable bên thứ ba qua subprocess
4. **Giám sát tiến trình**: Theo dõi tiến trình thời gian thực và xử lý lỗi
5. **Quản lý file**: Sao lưu tự động và validation

### Cơ chế an toàn
- **Cách ly tiến trình**: Mỗi tác vụ chạy trong thread riêng
- **Dọn dẹp tài nguyên**: Tự động dọn dẹp process khi thoát
- **Khôi phục lỗi**: Xử lý lỗi graceful với thông báo chi tiết
- **Kiểm tra file**: Validation tính toàn vẹn trước/sau xử lý

## 📁 Định dạng file được hỗ trợ

### Định dạng Archive
| Định dạng | Phần mở rộng | Mô tả | Công cụ sử dụng |
|-----------|---------------|--------|----------------|
| **CPK Archive** | `.cpk` | Định dạng archive game | YACpkTool |
| **MVGL Archive** | `.mvgl` | Archive model/texture | DSCSTools |
| **DSCS Archive** | `.dscs` | Định dạng archive thay thế | DSCSTools |

### Định dạng Hình ảnh
| Định dạng | Phần mở rộng | Mô tả | Nén |
|-----------|---------------|--------|-----|
| **IMG Texture** | `.img` | Định dạng texture game | BC7 (qua DDS) |
| **PNG Image** | `.png` | Định dạng hình ảnh chuẩn | Lossless |
| **DDS Texture** | `.dds` | DirectDraw Surface | BC7/BC1/BC3 |

### Định dạng Dữ liệu
| Định dạng | Phần mở rộng | Mô tả | Công cụ sử dụng |
|-----------|---------------|--------|----------------|
| **MBE Data** | `.mbe` | Định dạng dữ liệu game | THL-MBE-Parser |
| **CSV Data** | `.csv` | Comma-separated values | Built-in |
| **TSV Data** | `.tsv` | Tab-separated values | Built-in |

### Hỗ trợ Xử lý Hàng loạt
- ✅ **Quét thư mục**: Tự động tìm file trong thư mục
- ✅ **Xử lý đệ quy**: Xử lý thư mục con
- ✅ **Pattern matching**: Lọc file theo pattern
- ✅ **Theo dõi tiến trình**: Theo dõi tiến trình từng file
- ✅ **Cách ly lỗi**: Lỗi của một file không ảnh hưởng file khác

## 📦 Cài đặt

### Yêu cầu hệ thống tối thiểu
| Thành phần | Yêu cầu | Ghi chú |
|------------|---------|---------|
| **Hệ điều hành** | Windows 10 (64-bit) | Windows 11 khuyến nghị |
| **Python** | 3.8.0+ | 3.9+ khuyến nghị cho hiệu suất tốt hơn |
| **RAM** | 4GB | 8GB+ cho file lớn |
| **Ổ cứng** | 500MB | SSD khuyến nghị |
| **Màn hình** | 1280x720 | 1920x1080+ cho trải nghiệm tốt |
| **CPU** | Dual-core 2.5GHz+ | Quad-core khuyến nghị |

### Bước 1: Cài đặt Python
1. Tải Python từ [python.org](https://python.org)
2. Chạy installer và **đảm bảo tích vào "Add Python to PATH"**
3. Kiểm tra cài đặt:
```bash
python --version
pip --version
```

### Bước 2: Cài đặt Dependencies
```bash
# Cập nhật pip trước
python -m pip install --upgrade pip

# Cài đặt PyQt6
pip install PyQt6

# (Tùy chọn) Cài đặt thêm các package hỗ trợ
pip install pyqt6-tools
```

### Bước 3: Tải và cấu hình DSTSTool GUI
```bash
# Clone repository hoặc tải release
# Giải nén file vào thư mục mong muốn

# Di chuyển vào thư mục ứng dụng
cd path/to/DSTSTool-GUI

# Chạy ứng dụng
python DSTSToolGUIV2.py
```

### Bước 4: Xác minh cài đặt
- Ứng dụng sẽ hiển thị cửa sổ GUI với 5 tab công cụ
- Kiểm tra menu Help > README để xem tài liệu
- Test với file mẫu để đảm bảo hoạt động

### Cài đặt nâng cao

#### Sử dụng Virtual Environment (Khuyến nghị)
```bash
# Tạo virtual environment
python -m venv dststool_env

# Kích hoạt virtual environment
dststool_env\Scripts\activate

# Cài đặt dependencies trong virtual environment
pip install PyQt6

# Chạy ứng dụng
python DSTSToolGUIV2.py
```

#### Cấu hình cho Development
```bash
# Cài đặt thêm các package development
pip install pyqt6-tools black flake8 pytest

# Chạy linter
flake8 *.py

# Format code
black *.py
```

### Yêu cầu khuyến nghị (cho hiệu suất tối ưu)
| Thành phần | Khuyến nghị | Lợi ích |
|------------|-------------|---------|
| **Hệ điều hành** | Windows 11 Pro | Tương thích tốt nhất |
| **Python** | 3.11.x | Hiệu suất cao, hỗ trợ mới nhất |
| **RAM** | 16GB+ | Xử lý file lớn mượt mà |
| **Ổ cứng** | NVMe SSD 1TB+ | Tốc độ I/O cao |
| **GPU** | DirectX 11+ | Hỗ trợ nén texture |
| **Màn hình** | 2560x1440+ | Giao diện sắc nét |

### Kiểm tra tương thích hệ thống

#### Kiểm tra Python
```bash
# Kiểm tra phiên bản Python
python --version

# Kiểm tra pip
pip --version

# Kiểm tra PyQt6 compatibility
python -c "import sys; print(f'Python: {sys.version}')"
```

#### Kiểm tra Windows Features
- ✅ .NET Framework 4.8+
- ✅ Visual C++ Redistributables
- ✅ DirectX 11+ (cho GPU acceleration)

### Cấu hình nâng cao

#### Cho file lớn (>2GB)
```json
{
  "max_file_size": "4GB",
  "buffer_size": "256MB",
  "thread_count": 4,
  "temp_dir": "D:\\Temp"
}
```

#### Cho batch processing
- **Memory allocation**: Tối đa 75% RAM có sẵn
- **Thread pool**: Tự động điều chỉnh theo CPU cores
- **I/O optimization**: Sử dụng async operations

### Các vấn đề đã biết và giải pháp

#### Windows Defender
- **Vấn đề**: Có thể chặn các executable bên thứ ba
- **Giải pháp**: Thêm thư mục Tools vào exclusion list

#### Virtual Machine
- **Hỗ trợ**: VMware, VirtualBox, Hyper-V
- **Lưu ý**: Cần enable GPU acceleration cho texture compression

#### Remote Desktop
- **Hỗ trợ**: RDP, TeamViewer, AnyDesk
- **Lưu ý**: Có thể chậm hơn khi xử lý file lớn

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

## 🔗 Nguồn gốc & Lời cảm ơn

DSTSTool GUI v2 được xây dựng trên nền tảng của các công cụ mã nguồn mở tuyệt vời từ cộng đồng. Chúng tôi xin gửi lời cảm ơn sâu sắc đến tất cả các nhà phát triển đã đóng góp vào các dự án này.

### 🖼️ Compressonator (Nén Texture GPU)
- **Tác giả**: GPUOpen Tools Team (AMD)
- **Repository**: https://github.com/GPUOpen-Tools/compressonator
- **Sử dụng trong**: IMG Tools - Chuyển đổi texture với nén BC7
- **Giấy phép**: MIT License
- **Đóng góp**: Công cụ nén texture chuyên nghiệp với hỗ trợ GPU acceleration
- **Phiên bản**: v4.3.0 (tích hợp trong DSTSTool)

### 📊 THL-MBE-Parser (Parser Dữ liệu)
- **Tác giả**: Ahtheerr
- **Repository**: https://github.com/Ahtheerr/THL-MBE-Parser
- **Sử dụng trong**: MBE Tools - Parse và repack file MBE
- **Giấy phép**: MIT License
- **Đóng góp**: Parser chuyên biệt cho định dạng MBE của game Digimon
- **Phiên bản**: Latest (tích hợp Python scripts)

### 🎮 DSCSTools (Bộ xử lý Archive)
- **Tác giả**: SydMontague
- **Repository**: https://github.com/SydMontague/DSCSTools
- **Sử dụng trong**: MVGL Tools - Xử lý file MVGL/DSCS
- **Giấy phép**: MIT License
- **Đóng góp**: Bộ công cụ toàn diện cho xử lý archive game
- **Phiên bản**: CLI v1.0 (tích hợp executable)

### 📦 YACpkTool (Công cụ Archive)
- **Tác giả**: Brolijah
- **Repository**: https://github.com/Brolijah/YACpkTool
- **Sử dụng trong**: CPK Tools - Extract và repack file CPK
- **Giấy phép**: MIT License
- **Đóng góp**: Công cụ xử lý archive CPK hiệu quả và đáng tin cậy
- **Phiên bản**: v1.0 (tích hợp với CpkMaker.dll)

### 🙏 Lời cảm ơn đặc biệt

Chúng tôi xin gửi lời cảm ơn chân thành đến:

- **Cộng đồng modding Digimon**: Cung cấp kiến thức và động lực phát triển
- **Các nhà phát triển công cụ**: Đã tạo ra các công cụ mạnh mẽ và chia sẻ mã nguồn
- **Người dùng và tester**: Đóng góp phản hồi quý báu để cải thiện ứng dụng
- **AMD GPUOpen**: Hỗ trợ công nghệ nén texture tiên tiến

### 📜 Giấy phép và Quyền sử dụng

Tất cả các công cụ bên thứ ba đều tuân thủ giấy phép MIT hoặc tương đương, cho phép:
- ✅ Sử dụng thương mại và phi thương mại
- ✅ Sửa đổi và phân phối
- ✅ Bảo lưu thông tin bản quyền
- ✅ Không có warranty

### 🤝 Đóng góp ngược

DSTSTool GUI v2 là dự án mã nguồn mở và chúng tôi khuyến khích:
- Báo cáo bug và đề xuất tính năng
- Đóng góp code cải thiện
- Chia sẻ kinh nghiệm sử dụng
- Hỗ trợ người dùng khác trong cộng đồng

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

## 🔧 Khắc phục sự cố

### Vấn đề thường gặp và giải pháp

#### 1. Lỗi "Python not found" hoặc "pip not found"
```
Error: 'python' is not recognized as an internal or external command
```
**Giải pháp:**
- Kiểm tra PATH: `echo %PATH%`
- Thêm Python vào PATH trong cài đặt Windows
- Sử dụng `py` thay vì `python`: `py --version`

#### 2. Lỗi import PyQt6
```
ModuleNotFoundError: No module named 'PyQt6'
```
**Giải pháp:**
```bash
# Cài đặt PyQt6
pip install PyQt6

# Hoặc với quyền admin
pip install --user PyQt6

# Kiểm tra cài đặt
python -c "import PyQt6; print('PyQt6 installed successfully')"
```

#### 3. Lỗi "Tool not found" (Compressonator, DSCSTools, etc.)
```
Error: compressonatorcli.exe not found at path/to/Tools/compressonator/
```
**Giải pháp:**
- Kiểm tra thư mục Tools có đầy đủ không
- Đảm bảo các file executable không bị antivirus chặn
- Thêm thư mục Tools vào Windows Defender exclusion
- Kiểm tra quyền truy cập file

#### 4. Ứng dụng không khởi động
```
Application crashed on startup
```
**Giải pháp:**
- Kiểm tra log file trong thư mục ứng dụng
- Chạy từ command line: `python DSTSToolGUIV2.py`
- Kiểm tra Python và PyQt6 version compatibility
- Thử chạy với virtual environment

#### 5. Lỗi xử lý file lớn
```
Out of memory error hoặc Processing timeout
```
**Giải pháp:**
- Tăng RAM hệ thống (khuyến nghị 16GB+)
- Xử lý file theo batch nhỏ hơn
- Đóng các ứng dụng khác để giải phóng RAM
- Sử dụng SSD thay vì HDD

### FAQ (Câu hỏi thường gặp)

#### Q: DSTSTool GUI có miễn phí không?
**A:** Có, hoàn toàn miễn phí và mã nguồn mở dưới giấy phép MIT.

#### Q: Tôi có thể sử dụng DSTSTool cho game khác không?
**A:** Ứng dụng được thiết kế đặc biệt cho Digimon Story: Time Stranger, nhưng một số công cụ có thể hoạt động với game khác có định dạng tương tự.

#### Q: Làm sao để khôi phục file đã bị ghi đè?
**A:** Luôn backup file gốc trước khi xử lý. Nếu không có backup, file gốc có thể không khôi phục được.

#### Q: Tại sao xử lý file rất chậm?
**A:** Nguyên nhân có thể do:
- File quá lớn so với RAM
- Ổ cứng chậm (HDD thay vì SSD)
- Antivirus quét file
- Hệ thống thiếu tài nguyên

#### Q: Có thể xử lý nhiều file cùng lúc không?
**A:** Có, ứng dụng hỗ trợ batch processing. Tuy nhiên, quá nhiều file cùng lúc có thể gây quá tải hệ thống.

#### Q: Làm sao để đóng góp code?
**A:** Xem phần Contributing bên dưới để biết chi tiết quy trình.

#### Q: Ứng dụng có hỗ trợ Linux/Mac không?
**A:** Hiện tại chỉ hỗ trợ Windows. Các công cụ bên thứ ba chủ yếu dành cho Windows.

#### Q: File sau khi xử lý có khác với file gốc không?
**A:** Một số định dạng (như IMG với nén BC7) sẽ có chất lượng tương đương nhưng kích thước nhỏ hơn. Các định dạng khác giữ nguyên chất lượng.

### Debug Mode

Để chạy ứng dụng ở chế độ debug:
```bash
# Chạy với debug logging
python DSTSToolGUIV2.py --debug

# Hoặc set environment variable
set DSTSTOOL_DEBUG=1
python DSTSToolGUIV2.py
```

### Liên hệ hỗ trợ

Nếu gặp vấn đề không giải quyết được:
1. Kiểm tra [Issues](https://github.com/your-repo/DSTSTool-GUI/issues) trên GitHub
2. Tạo issue mới với thông tin chi tiết:
   - Phiên bản ứng dụng
   - Hệ điều hành và Python version
   - Mô tả lỗi và steps để reproduce
   - Log files nếu có

## 🤝 Đóng góp

Chúng tôi rất hoan nghênh mọi đóng góp từ cộng đồng! DSTSTool GUI là dự án mã nguồn mở và chúng tôi tin rằng sự hợp tác sẽ làm cho công cụ này ngày càng hoàn thiện hơn.

### Cách đóng góp

#### 1. Phát triển Code
```bash
# Fork repository trên GitHub
# Clone repository của bạn
git clone https://github.com/your-username/DSTSTool-GUI.git
cd DSTSTool-GUI

# Tạo branch cho tính năng mới
git checkout -b feature/your-feature-name

# Cài đặt development dependencies
pip install -r requirements-dev.txt

# Chạy tests
python -m pytest

# Format code
black *.py
flake8 *.py

# Commit changes
git commit -m "feat: Add your feature description"

# Push to your branch
git push origin feature/your-feature-name
```

#### 2. Quy trình Pull Request
1. **Fork** repository trên GitHub
2. **Tạo feature branch** với tên mô tả (`feature/add-new-tool`, `fix/bug-fix`, `docs/update-readme`)
3. **Implement** tính năng hoặc sửa lỗi
4. **Test** kỹ lưỡng trên môi trường của bạn
5. **Update documentation** nếu cần
6. **Commit** với message rõ ràng (theo conventional commits)
7. **Push** lên branch của bạn
8. **Tạo Pull Request** với mô tả chi tiết

#### 3. Coding Standards
```python
# Sử dụng type hints
def process_file(file_path: str) -> bool:
    pass

# Comment functions in English
def extract_archive(source: str, target: str) -> bool:
    """
    Extract archive file to target directory.

    Args:
        source: Path to archive file
        target: Target directory for extraction

    Returns:
        True if successful, False otherwise
    """
    pass

# Error handling
try:
    # Your code here
    pass
except Exception as e:
    logger.error(f"Error processing file: {e}")
    return False
```

#### 4. Các loại đóng góp được chào đón
- ✅ **Bug fixes**: Sửa lỗi và cải thiện stability
- ✅ **New features**: Thêm công cụ hoặc tính năng mới
- ✅ **Documentation**: Cải thiện docs, tutorials, examples
- ✅ **Performance**: Tối ưu hóa tốc độ xử lý
- ✅ **UI/UX**: Cải thiện giao diện người dùng
- ✅ **Testing**: Thêm unit tests và integration tests
- ✅ **Localization**: Hỗ trợ thêm ngôn ngữ

#### 5. Báo cáo Issues
Khi báo cáo bug hoặc đề xuất tính năng:
- Sử dụng issue templates có sẵn
- Cung cấp thông tin chi tiết:
  - Phiên bản ứng dụng
  - Hệ điều hành và Python version
  - Steps để reproduce
  - Expected vs actual behavior
  - Screenshots nếu có thể

#### 6. Development Setup
```bash
# Clone repository
git clone https://github.com/your-repo/DSTSTool-GUI.git
cd DSTSTool-GUI

# Setup virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run application
python DSTSToolGUIV2.py
```

### Quy tắc cộng đồng
- **Tôn trọng**: Tôn trọng ý kiến của người khác
- **Chất lượng**: Đảm bảo code chất lượng cao
- **Testing**: Test kỹ trước khi submit
- **Documentation**: Update docs cho mọi thay đổi
- **Communication**: Thảo luận trước khi implement tính năng lớn

### Liên hệ
- **GitHub Issues**: Cho bug reports và feature requests
- **GitHub Discussions**: Cho questions và discussions
- **Discord**: [DSTSTool Community](https://discord.gg/dststool) (optional)

Cảm ơn bạn đã đóng góp cho DSTSTool GUI! 🎉

## 📝 Nhật ký thay đổi

### [v2.0] - 2025-09-19
#### ✨ Tính năng mới
- **Giao diện hoàn toàn mới**: Redesign UI với PyQt6, hệ thống tab hiện đại
- **Hỗ trợ đa định dạng**: CPK, MVGL, IMG, MBE, TEXT tools tích hợp
- **Batch processing**: Xử lý hàng loạt với theo dõi tiến trình
- **Error handling**: Xử lý lỗi thông minh với thông báo chi tiết
- **Process management**: Quản lý tiến trình an toàn, tự động dọn dẹp

#### 🔧 Cải thiện
- **Performance**: Tối ưu hóa tốc độ xử lý file
- **Stability**: Cải thiện độ ổn định và xử lý lỗi
- **User Experience**: Giao diện trực quan, dễ sử dụng
- **Resource management**: Quản lý bộ nhớ và CPU hiệu quả

#### 📚 Tài liệu
- **README bilingual**: Hỗ trợ tiếng Anh và tiếng Việt
- **Installation guide**: Hướng dẫn cài đặt chi tiết
- **Troubleshooting**: Hướng dẫn khắc phục sự cố
- **API documentation**: Tài liệu cho developers

### [v1.5.0] - 2024-08-15
#### ✨ Tính năng mới
- Thêm hỗ trợ IMG tools với Compressonator
- Tích hợp THL-MBE-Parser cho MBE processing
- Cải thiện TEXT tools với CSV/TSV support

#### 🔧 Cải thiện
- Cập nhật DSCSTools CLI
- Tối ưu hóa memory usage
- Thêm progress bars cho tất cả operations

### [v1.0.0] - 2024-01-01
#### 🚀 Phát hành đầu tiên
- CPK tools với YACpkTool integration
- MVGL tools với DSCSTools
- Basic GUI với PyQt5
- Core functionality cho Digimon Story: Time Stranger

### Phát triển tương lai
#### [v2.1.0] - Q2 2025 (Planned)
- **Cross-platform support**: Linux và macOS compatibility
- **Plugin system**: Kiến trúc plugin mở rộng
- **Advanced batch processing**: Parallel processing với GPU acceleration
- **Cloud integration**: Hỗ trợ xử lý file trên cloud
- **API endpoints**: REST API cho automation

#### [v2.2.0] - Q4 2025 (Planned)
- **Machine Learning**: AI-powered file analysis
- **Advanced compression**: Lossless compression algorithms
- **Real-time collaboration**: Multi-user editing support
- **Mobile companion**: Mobile app cho monitoring

### Cách theo dõi phiên bản
```bash
# Kiểm tra phiên bản hiện tại
python DSTSToolGUIV2.py --version

# Cập nhật từ GitHub releases
# Download latest release từ GitHub
```

### Release Notes Template
```
## [vX.Y.Z] - YYYY-MM-DD

### Added
- Mô tả tính năng mới

### Changed
- Thay đổi trong chức năng hiện tại

### Deprecated
- Tính năng sắp bị loại bỏ

### Removed
- Tính năng đã loại bỏ

### Fixed
- Sửa lỗi

### Security
- Thay đổi liên quan đến bảo mật
```

## 📄 Giấy phép

DSTSTool GUI được phân phối dưới giấy phép MIT. Xem file `LICENSE` để biết thêm chi tiết.

---

## 📦 Downloads & Releases

### Latest Release: v2.0
[![Download](https://img.shields.io/badge/Download-v2.0-blue.svg)](https://github.com/levi-soft/DSTSTools-VN/releases/latest)
[![All Releases](https://img.shields.io/badge/All%20Releases-View-green.svg)](https://github.com/levi-soft/DSTSTools-VN/releases)

### System Requirements Summary
- **OS**: Windows 10/11 (64-bit)
- **Python**: 3.8+
- **RAM**: 4GB minimum
- **Storage**: 500MB

### Quick Start
```bash
# 1. Install Python 3.8+
# 2. Install PyQt6
pip install PyQt6

# 3. Download DSTSTool GUI
# 4. Run application
python DSTSToolGUIV2.py
```

## 🌟 Features Overview

| Tool | Input | Output | Features |
|------|-------|--------|----------|
| **CPK** | `.cpk` | Files | Extract/Repack, Batch processing |
| **MVGL** | `.mvgl` | Files | Extract/Repack, DSCS support |
| **IMG** | `.img` | `.png` | BC7 compression, DDS handling |
| **MBE** | `.mbe` | `.csv` | Parse/Repack, Metadata |
| **TEXT** | `.csv` | `.tsv` | Merge/Split, Line breaks |

## 📞 Support & Community

- **GitHub Repository**: [Xem trên GitHub](https://github.com/levi-soft/DSTSTools-VN)
- **GitHub Issues**: [Báo cáo bug & đề xuất tính năng](https://github.com/levi-soft/DSTSTools-VN/issues)
- **GitHub Discussions**: [Q&A và thảo luận chung](https://github.com/levi-soft/DSTSTools-VN/discussions)
- **Documentation**: [Tài liệu đầy đủ](https://levi-soft.github.io/DSTSTools-VN/)
- **README**: [English](README.md) | [Tiếng Việt](README_VI.md)

## 🙏 Acknowledgments

DSTSTool GUI v2 được phát triển bởi **Levi** với sự hỗ trợ từ cộng đồng modding Digimon Story: Time Stranger.

**Cảm ơn đặc biệt:**
- Cộng đồng modding đã truyền cảm hứng
- Các nhà phát triển công cụ mã nguồn mở
- Người dùng đã đóng góp phản hồi quý báu

---

**Tác giả**: Levi
**Phiên bản**: v2.0
**Cập nhật cuối**: 2025-09-19
**Repository**: [GitHub](https://github.com/levi-soft/DSTSTools-VN)

*DSTSTool GUI được phát triển để hỗ trợ cộng đồng modding game, giúp xử lý file game một cách dễ dàng và hiệu quả. Mã nguồn mở dưới giấy phép MIT.*