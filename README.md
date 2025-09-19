# DSTSTool GUI v2

[![Version](https://img.shields.io/badge/version-2.0-blue.svg)](https://github.com/levi-soft/DSTSTools-VN)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)

**DSTSTool GUI v2** is a comprehensive graphical user interface (GUI) application built with Python and PyQt6, specialized for Digimon Story: Time Stranger game modding. The application provides powerful tools for processing and converting popular game file formats, supporting batch processing with real-time progress monitoring and intelligent error handling.

## 🌐 Language Support / Hỗ trợ Ngôn ngữ

📖 **For Vietnamese users** / **Dành cho người dùng Việt Nam**: [Nhấn vào đây để đọc bằng tiếng Việt](README_VI.md)

This documentation is available in both English and Vietnamese. Choose your preferred language above.

## 🎯 Purpose and Benefits

DSTSTool GUI v2 is specially designed to:
- **Simplify modding process**: Intuitive interface helps users easily manipulate game files
- **Increase efficiency**: Batch processing and multi-threading save significant time
- **Ensure safety**: Automatic backup and file integrity checking
- **Support community**: Open-source tool serving the modding community

## 📋 Table of Contents

- [Key Features](#-key-features)
- [Architecture & Workflow](#-architecture--workflow)
- [Supported File Formats](#-supported-file-formats)
- [Installation](#-installation)
- [Usage](#-usage)
- [Internal Tools](#-internal-tools)
- [Sources & Acknowledgments](#-sources--acknowledgments)
- [System Requirements](#-system-requirements)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [Changelog](#-changelog)
- [License](#-license)

## 🚀 Key Features

### 1. **CPK Tools** 📦
- **Extract Files**: Extract CPK files into individual files
- **Repack Files**: Pack individual files into CPK format
- **Batch Processing**: Process multiple files simultaneously
- **Progress Monitoring**: Real-time progress tracking

### 2. **MVGL Tools** 🎮
- **Extract MVGL**: Extract MVGL files into individual files
- **Repack MVGL**: Pack files into MVGL format
- **DSCS Support**: DSCS format support
- **Real-time Progress**: Detailed progress monitoring

### 3. **IMG Tools** 🖼️
- **IMG to PNG**: Convert IMG files to PNG (Batch)
- **PNG to IMG**: Convert PNG to IMG with BC7 compression
- **Compressonator Integration**: Uses Compressonator CLI
- **DDS Management**: Automatic DDS file management

### 4. **MBE Tools** 📊
- **Extract MBE to CSV**: Convert MBE to CSV (Batch)
- **Repack CSV to MBE**: Pack CSV into MBE (Batch)
- **File Count Display**: Shows number of processed files
- **Metadata Handling**: Automatic metadata processing

### 5. **TEXT Tools** 📝
- **Merge CSV to TSV**: Merge multiple CSV files into TSV
- **Split TSV to CSV**: Split TSV into multiple CSV files
- **Line Break Escaping**: Handle line break characters
- **Batch Directory Processing**: Batch directory processing

## 🏗️ Architecture & Workflow

### Application Architecture
```
DSTSTool GUI v2/
├── DSTSToolGUIV2.py          # Main application & GUI framework
├── CPKTool.py               # CPK archive processing module
├── MVGLTool.py              # MVGL/DSCS file processing module
├── IMGTool.py               # Image conversion module
├── MBETool.py               # MBE data processing module
├── TEXTTool.py              # Text/CSV processing module
├── Tools/                   # External tools directory
│   ├── compressonator/      # GPU texture compression
│   ├── DSCSTools/          # MVGL/DSCS processing
│   ├── THL-MBE-Parser/     # MBE file parser
│   └── YACpkTool/          # CPK archive tool
└── icon.ico                 # Application icon
```

### Processing Workflow
1. **User Interface**: PyQt6-based GUI with tab system
2. **Multi-threading**: Worker threads for heavy tasks
3. **Tool Integration**: Call third-party executables via subprocess
4. **Progress Monitoring**: Real-time progress tracking and error handling
5. **File Management**: Automatic backup and validation

### Safety Mechanisms
- **Process isolation**: Each task runs in separate thread
- **Resource cleanup**: Automatic process cleanup on exit
- **Error recovery**: Graceful error handling with detailed messages
- **File validation**: Integrity checking before/after processing

## 📁 Supported File Formats

### Archive Formats
| Format | Extension | Description | Tool Used |
|--------|-----------|-------------|-----------|
| **CPK Archive** | `.cpk` | Game archive format | YACpkTool |
| **MVGL Archive** | `.mvgl` | Model/texture archive | DSCSTools |

### Image Formats
| Format | Extension | Description | Compression |
|--------|-----------|-------------|-------------|
| **IMG Texture** | `.img` | Game texture format | BC7 (via DDS) |
| **PNG Image** | `.png` | Standard image format | Lossless |
| **DDS Texture** | `.dds` | DirectDraw Surface | BC7/BC1/BC3 |

### Data Formats
| Format | Extension | Description | Tool Used |
|--------|-----------|-------------|-----------|
| **MBE Data** | `.mbe` | Game data format | THL-MBE-Parser |
| **CSV Data** | `.csv` | Comma-separated values | Built-in |
| **TSV Data** | `.tsv` | Tab-separated values | Built-in |

### Batch Processing Support
- ✅ **Directory scanning**: Automatically find files in directories
- ✅ **Recursive processing**: Process subdirectories
- ✅ **Pattern matching**: Filter files by pattern
- ✅ **Progress tracking**: Track progress for each file
- ✅ **Error isolation**: One file error doesn't affect others

## 📦 Installation

### Minimum System Requirements
- **Operating System**: Windows 10/11 (64-bit)
- **Python**: 3.8.0 or higher
- **RAM**: 4GB (8GB recommended)
- **Storage**: 500MB free space
- **Display**: Minimum resolution 1280x720

### Step 1: Install Python
1. Download Python from [python.org](https://python.org)
2. Run installer and **make sure to check "Add Python to PATH"**
3. Verify installation:
```bash
python --version
pip --version
```

### Step 2: Install Dependencies
```bash
# Update pip first
python -m pip install --upgrade pip

# Install PyQt6
pip install PyQt6

# (Optional) Install additional supporting packages
pip install pyqt6-tools
```

### Step 3: Download and Configure DSTSTool GUI
```bash
# Clone repository or download release
# Extract files to desired directory

# Navigate to application directory
cd path/to/DSTSTool-GUI

# Run application
python DSTSToolGUIV2.py
```

### Step 4: Verify Installation
- Application will display GUI window with 5 tool tabs
- Check Help menu > README to view documentation
- Test with sample files to ensure functionality

### Advanced Installation

#### Using Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv dststool_env

# Activate virtual environment
dststool_env\Scripts\activate

# Install dependencies in virtual environment
pip install PyQt6

# Run application
python DSTSToolGUIV2.py
```

#### Development Configuration
```bash
# Install additional development packages
pip install pyqt6-tools black flake8 pytest

# Run linter
flake8 *.py

# Format code
black *.py
```

## 📖 Usage

### CPK Tools
1. **Extract Files**:
   - Select CPK file using "📄 Browse" button
   - Select destination directory using "📂 Browse" button
   - Click "🚀 Extract Files"
   - Monitor progress bar

2. **Repack Files**:
   - Select directory containing files using "📂 Browse" button
   - Select output CPK file path using "💾 Browse" button
   - Click "🔧 Repack Files"
   - Monitor progress bar

### MVGL Tools
1. **Extract**:
   - Select source MVGL file
   - Select destination directory
   - Click "🚀 Extract Files"

2. **Repack**:
   - Select directory containing files
   - Select output MVGL file path
   - Click "🔧 Repack Files"

### IMG Tools
1. **IMG to PNG**:
   - Select directory containing IMG files
   - Select destination directory for PNG files
   - Click "🔄 Convert to PNG"

2. **PNG to IMG**:
   - Select directory containing PNG files
   - Select destination directory for IMG files
   - Click "🔄 Convert to IMG"

### MBE Tools
1. **Extract MBE to CSV**:
   - Select directory containing .MBE files
   - Select destination directory for CSV files
   - Click "🚀 Extract Files"

2. **Repack CSV to MBE**:
   - Select directory containing CSV subdirectories
   - Select destination directory for MBE files
   - Click "🔧 Repack Files"

### TEXT Tools
1. **Merge CSV to TSV**:
   - Select directory containing CSV subdirectories
   - Select output TSV file path
   - Click "🔗 Merge CSV to TSV"

2. **Split TSV to CSV**:
   - Select source TSV file
   - Select destination directory for CSV files
   - Click "✂️ Split TSV to CSV"

## 🔧 Internal Tools

DSTSTool GUI uses the following external tools:

### Tools Directory Structure
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

## 🔗 Sources & Acknowledgments

DSTSTool GUI v2 is built on the foundation of excellent open-source tools from the community. We extend our deepest gratitude to all developers who have contributed to these projects.

### 🖼️ Compressonator (GPU Texture Compression)
- **Tác giả**: GPUOpen Tools Team (AMD)
- **Repository**: https://github.com/GPUOpen-Tools/compressonator
- **Sử dụng trong**: IMG Tools - Chuyển đổi texture với nén BC7
- **Giấy phép**: MIT License
- **Đóng góp**: Công cụ nén texture chuyên nghiệp với hỗ trợ GPU acceleration
- **Phiên bản**: v4.3.0 (tích hợp trong DSTSTool)

### 📊 THL-MBE-Parser (Data Parser)
- **Tác giả**: Ahtheerr
- **Repository**: https://github.com/Ahtheerr/THL-MBE-Parser
- **Sử dụng trong**: MBE Tools - Parse và repack file MBE
- **Giấy phép**: MIT License
- **Đóng góp**: Parser chuyên biệt cho định dạng MBE của game Digimon
- **Phiên bản**: Latest (tích hợp Python scripts)

### 🎮 DSCSTools (Archive Processor)
- **Tác giả**: SydMontague
- **Repository**: https://github.com/SydMontague/DSCSTools
- **Sử dụng trong**: MVGL Tools - Xử lý file MVGL/DSCS
- **Giấy phép**: MIT License
- **Đóng góp**: Bộ công cụ toàn diện cho xử lý archive game
- **Phiên bản**: CLI v1.0 (tích hợp executable)

### 📦 YACpkTool (Archive Tool)
- **Tác giả**: Brolijah
- **Repository**: https://github.com/Brolijah/YACpkTool
- **Sử dụng trong**: CPK Tools - Extract và repack file CPK
- **Giấy phép**: MIT License
- **Đóng góp**: Công cụ xử lý archive CPK hiệu quả và đáng tin cậy
- **Phiên bản**: v1.0 (tích hợp với CpkMaker.dll)

### 🙏 Special Thanks

We sincerely thank:

- **Digimon Modding Community**: Providing knowledge and development motivation
- **Tool Developers**: Creating powerful tools and sharing source code
- **Users and Testers**: Contributing valuable feedback to improve the application
- **AMD GPUOpen**: Supporting advanced texture compression technology

### 📜 License and Usage Rights

All third-party tools comply with MIT license or equivalent, allowing:
- ✅ Commercial and non-commercial use
- ✅ Modification and distribution
- ✅ Copyright retention
- ✅ No warranty

### 🤝 Contributing Back

DSTSTool GUI v2 is an open-source project and we encourage:
- Bug reports and feature suggestions
- Code improvement contributions
- Sharing usage experience
- Supporting other users in the community

## 💻 System Requirements

### Minimum Requirements
| Component | Requirement | Notes |
|-----------|-------------|-------|
| **Operating System** | Windows 10 (64-bit) | Windows 11 recommended |
| **Python** | 3.8.0+ | 3.9+ recommended for better performance |
| **RAM** | 4GB | 8GB+ for large files |
| **Storage** | 500MB | SSD recommended |
| **Display** | 1280x720 | 1920x1080+ for better experience |
| **CPU** | Dual-core 2.5GHz+ | Quad-core recommended |

### Recommended Requirements (for optimal performance)
| Component | Recommendation | Benefits |
|-----------|----------------|----------|
| **Operating System** | Windows 11 Pro | Best compatibility |
| **Python** | 3.11.x | High performance, latest support |
| **RAM** | 16GB+ | Smooth large file processing |
| **Storage** | NVMe SSD 1TB+ | High I/O speed |
| **GPU** | DirectX 11+ | Texture compression support |
| **Display** | 2560x1440+ | Sharp interface |

### System Compatibility Check

#### Python Check
```bash
# Check Python version
python --version

# Check pip
pip --version

# Check PyQt6 compatibility
python -c "import sys; print(f'Python: {sys.version}')"
```

#### Windows Features Check
- ✅ .NET Framework 4.8+
- ✅ Visual C++ Redistributables
- ✅ DirectX 11+ (for GPU acceleration)

### Advanced Configuration

#### For large files (>2GB)
```json
{
  "max_file_size": "4GB",
  "buffer_size": "256MB",
  "thread_count": 4,
  "temp_dir": "D:\\Temp"
}
```

#### For batch processing
- **Memory allocation**: Maximum 75% of available RAM
- **Thread pool**: Auto-adjust based on CPU cores
- **I/O optimization**: Use async operations

### Known Issues and Solutions

#### Windows Defender
- **Issue**: May block third-party executables
- **Solution**: Add Tools folder to exclusion list

#### Virtual Machine
- **Support**: VMware, VirtualBox, Hyper-V
- **Note**: Need to enable GPU acceleration for texture compression

#### Remote Desktop
- **Support**: RDP, TeamViewer, AnyDesk
- **Note**: May be slower when processing large files

## ⚠️ Important Notes

1. **Backup Files**: Always backup original files before processing
2. **File Permissions**: Ensure read/write permissions for destination directories
3. **Large Files**: Some files may take considerable time to process
4. **Error Handling**: Application will display errors if issues occur
5. **Progress Monitoring**: Monitor progress bar for processing status

## 🔧 Troubleshooting

### Common Issues and Solutions

#### 1. "Python not found" or "pip not found" Error
```
Error: 'python' is not recognized as an internal or external command
```
**Solution:**
- Check PATH: `echo %PATH%`
- Add Python to PATH in Windows settings
- Use `py` instead of `python`: `py --version`

#### 2. PyQt6 Import Error
```
ModuleNotFoundError: No module named 'PyQt6'
```
**Solution:**
```bash
# Install PyQt6
pip install PyQt6

# Or with admin rights
pip install --user PyQt6

# Verify installation
python -c "import PyQt6; print('PyQt6 installed successfully')"
```

#### 3. "Tool not found" Error (Compressonator, DSCSTools, etc.)
```
Error: compressonatorcli.exe not found at path/to/Tools/compressonator/
```
**Solution:**
- Check if Tools directory is complete
- Ensure executables are not blocked by antivirus
- Add Tools folder to Windows Defender exclusion
- Check file access permissions

#### 4. Application won't start
```
Application crashed on startup
```
**Solution:**
- Check log files in application directory
- Run from command line: `python DSTSToolGUIV2.py`
- Check Python and PyQt6 version compatibility
- Try running with virtual environment

#### 5. Large file processing error
```
Out of memory error or Processing timeout
```
**Solution:**
- Increase system RAM (16GB+ recommended)
- Process files in smaller batches
- Close other applications to free RAM
- Use SSD instead of HDD

### FAQ (Frequently Asked Questions)

#### Q: Is DSTSTool GUI free?
**A:** Yes, completely free and open-source under MIT license.

#### Q: Can I use DSTSTool for other games?
**A:** The application is designed specifically for Digimon Story: Time Stranger, but some tools may work with other games that have similar formats.

#### Q: How to recover overwritten files?
**A:** Always backup original files before processing. If no backup exists, original files may not be recoverable.

#### Q: Why is file processing very slow?
**A:** Possible reasons:
- File too large for available RAM
- Slow storage (HDD instead of SSD)
- Antivirus scanning files
- System resource shortage

#### Q: Can I process multiple files at once?
**A:** Yes, the application supports batch processing. However, too many files at once may overload the system.

#### Q: How to contribute code?
**A:** See the Contributing section below for detailed process.

#### Q: Does the application support Linux/Mac?
**A:** Currently only supports Windows. Third-party tools are primarily Windows-based.

#### Q: Are processed files different from originals?
**A:** Some formats (like IMG with BC7 compression) will have equivalent quality but smaller size. Other formats maintain original quality.

### Debug Mode

To run the application in debug mode:
```bash
# Run with debug logging
python DSTSToolGUIV2.py --debug

# Or set environment variable
set DSTSTOOL_DEBUG=1
python DSTSToolGUIV2.py
```

### Contact Support

If you encounter unresolved issues:
1. Check [Issues](https://github.com/your-repo/DSTSTool-GUI/issues) on GitHub
2. Create a new issue with detailed information:
   - Application version
   - Operating system and Python version
   - Error description and steps to reproduce
   - Log files if available

## 🤝 Contributing

We greatly welcome all contributions from the community! DSTSTool GUI is an open-source project and we believe that collaboration will make this tool increasingly perfect.

### How to Contribute

#### 1. Code Development
```bash
# Fork repository on GitHub
# Clone your repository
git clone https://github.com/your-username/DSTSTool-GUI.git
cd DSTSTool-GUI

# Create branch for new feature
git checkout -b feature/your-feature-name

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest

# Format code
black *.py
flake8 *.py

# Commit changes
git commit -m "feat: Add your feature description"

# Push to your branch
git push origin feature/your-feature-name
```

#### 2. Pull Request Process
1. **Fork** repository on GitHub
2. **Create feature branch** with descriptive name (`feature/add-new-tool`, `fix/bug-fix`, `docs/update-readme`)
3. **Implement** feature or fix bug
4. **Test** thoroughly on your environment
5. **Update documentation** if needed
6. **Commit** with clear message (following conventional commits)
7. **Push** to your branch
8. **Create Pull Request** with detailed description

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

#### 4. Welcome Contribution Types
- ✅ **Bug fixes**: Fix bugs and improve stability
- ✅ **New features**: Add tools or new features
- ✅ **Documentation**: Improve docs, tutorials, examples
- ✅ **Performance**: Optimize processing speed
- ✅ **UI/UX**: Improve user interface
- ✅ **Testing**: Add unit tests and integration tests
- ✅ **Localization**: Support additional languages

#### 5. Issue Reporting
When reporting bugs or suggesting features:
- Use available issue templates
- Provide detailed information:
  - Application version
  - Operating system and Python version
  - Steps to reproduce
  - Expected vs actual behavior
  - Screenshots if possible

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

### Community Rules
- **Respect**: Respect others' opinions
- **Quality**: Ensure high code quality
- **Testing**: Test thoroughly before submit
- **Documentation**: Update docs for all changes
- **Communication**: Discuss before implementing major features

### Contact
- **GitHub Issues**: For bug reports and feature requests
- **GitHub Discussions**: For questions and discussions
- **Discord**: [DSTSTool Community](https://discord.gg/dststool) (optional)

Thank you for contributing to DSTSTool GUI! 🎉

## 📝 Changelog

### [v2.0] - 2025-09-19
#### ✨ New Features
- **Completely new interface**: Redesign UI with PyQt6, modern tab system
- **Multi-format support**: CPK, MVGL, IMG, MBE, TEXT tools integration
- **Batch processing**: Batch processing with progress tracking
- **Error handling**: Smart error handling with detailed messages
- **Process management**: Safe process management, automatic cleanup

### Version Tracking
```bash
# Check current version
python DSTSToolGUIV2.py --version

# Update from GitHub releases
# Download latest release from GitHub
```

### Release Notes Template
```
## [vX.Y.Z] - YYYY-MM-DD

### Added
- New feature description

### Changed
- Changes in existing functionality

### Deprecated
- Soon-to-be removed features

### Removed
- Removed features

### Fixed
- Bug fixes

### Security
- Security-related changes
```

## 📄 License

DSTSTool GUI is distributed under the MIT License. See the `LICENSE` file for more details.

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

- **GitHub Repository**: [View on GitHub](https://github.com/levi-soft/DSTSTools-VN)
- **GitHub Issues**: [Report bugs & request features](https://github.com/levi-soft/DSTSTools-VN/issues)
- **GitHub Discussions**: [Q&A and general discussion](https://github.com/levi-soft/DSTSTools-VN/discussions)
- **Documentation**: [Full documentation](https://levi-soft.github.io/DSTSTools-VN/)
- **README**: [English](README.md) | [Tiếng Việt](README_VI.md)

## 🙏 Acknowledgments

DSTSTool GUI v2 is developed by **Levi** with support from the Digimon Story: Time Stranger modding community.

**Special thanks:**
- Modding community for inspiration
- Open-source tool developers
- Users who contributed valuable feedback

---

**Author**: Levi
**Version**: v2.0
**Last Updated**: 2025-09-19
**Repository**: [GitHub](https://github.com/levi-soft/DSTSTools-VN)

*DSTSTool GUI is developed to support the game modding community, helping process game files easily and efficiently. Open-source under MIT license.*