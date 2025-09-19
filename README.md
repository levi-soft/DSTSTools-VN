# DSTSTools - Digimon Story: Time Stranger Modding Tools

[![Version](https://img.shields.io/badge/version-2.0-blue.svg)](https://github.com/levi-soft/DSTSTools-VN)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)

**DSTSTools** is a comprehensive graphical user interface (GUI) application built with Python and PyQt6, specialized for Digimon Story: Time Stranger game modding. This tool provides powerful utilities for processing and converting game file formats including .cpk, .mvgl, .img, and .mbe files, supporting batch processing with real-time progress monitoring and intelligent error handling.


## 🎯 Purpose and Benefits

DSTSTools is specially designed for Digimon Story: Time Stranger modding to:
- **Simplify modding process**: Intuitive interface helps users easily manipulate .cpk, .mvgl, .img, and .mbe game files
- **Increase efficiency**: Batch processing and multi-threading save significant time
- **Ensure safety**: Automatic backup and file integrity checking
- **Support community**: Open-source tool serving the Digimon Story: Time Stranger modding community

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

## 🏗️ Architecture

**DSTSTool GUI v2** uses a modular architecture:
- **Main GUI**: PyQt6-based interface with 5 specialized tool tabs
- **Processing Modules**: Separate Python modules for each file format
- **External Tools**: Integrated third-party executables for heavy processing
- **Multi-threading**: Background processing with progress monitoring
- **Error Handling**: Comprehensive error recovery and user feedback

## 📁 Supported File Formats

### Archive Formats (Digimon Story: Time Stranger)
| Format | Extension | Description | Tool Used |
|--------|-----------|-------------|-----------|
| **CPK Archive** | `.cpk` | Digimon Story: Time Stranger game archive format | YACpkTool |
| **MVGL Archive** | `.mvgl` | Digimon Story: Time Stranger model/texture archive | DSCSTools |

### Image Formats (Texture Tools)
| Format | Extension | Description | Compression |
|--------|-----------|-------------|-------------|
| **IMG Texture** | `.img` | Digimon Story: Time Stranger game texture format | BC7 (via DDS) |
| **PNG Image** | `.png` | Standard image format for texture conversion | Lossless |
| **DDS Texture** | `.dds` | DirectDraw Surface for advanced compression | BC7/BC1/BC3 |

### Data Formats (Modding Tools)
| Format | Extension | Description | Tool Used |
|--------|-----------|-------------|-----------|
| **MBE Data** | `.mbe` | Digimon Story: Time Stranger game data format | THL-MBE-Parser |
| **CSV Data** | `.csv` | Comma-separated values for data editing | Built-in |
| **TSV Data** | `.tsv` | Tab-separated values for text processing | Built-in |

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
- **YACpk Tool**: `YACpkTool.exe`

## 🔗 Sources & Acknowledgments

DSTSTool GUI v2 is built on the foundation of excellent open-source tools from the community. We extend our deepest gratitude to all developers who have contributed to these projects.

### 🖼️ Compressonator (Texture Compression)
- **Author**: GPUOpen-Tools
- **Repository**: https://github.com/GPUOpen-Tools/compressonator
- **Usage**: IMG Tools - Texture conversion with BC7 compression

### 📊 THL-MBE-Parser (Data Parser)
- **Author**: Ahtheerr
- **Repository**: https://github.com/Ahtheerr/THL-MBE-Parser
- **Usage**: MBE Tools - Parse and repack MBE files

### 🎮 DSCSTools (Archive Processor)
- **Author**: SydMontague
- **Repository**: https://github.com/SydMontague/DSCSTools
- **Usage**: MVGL Tools - MVGL/DSCS file processing

### 📦 YACpkTool (Archive Tool)
- **Author**: Brolijah
- **Repository**: https://github.com/Brolijah/YACpkTool
- **Usage**: CPK Tools - CPK archive extraction/repacking

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

### Minimum
- **OS**: Windows 10/11 (64-bit)
- **Python**: 3.8+
- **RAM**: 4GB (8GB recommended)
- **Storage**: 500MB
- **Display**: 1280x720 minimum

### Recommended
- **OS**: Windows 11
- **Python**: 3.11+
- **RAM**: 16GB+
- **Storage**: SSD/NVMe
- **GPU**: DirectX 11+ (for texture compression)

## ⚠️ Important Notes

1. **Backup Files**: Always backup original files before processing
2. **File Permissions**: Ensure read/write permissions for destination directories
3. **Large Files**: Some files may take considerable time to process
4. **Error Handling**: Application will display errors if issues occur
5. **Progress Monitoring**: Monitor progress bar for processing status

## 🔧 Troubleshooting

### Common Issues

#### Python/PyQt6 Issues
```bash
# Install PyQt6
pip install PyQt6

# Check Python version
python --version
```

#### Tool Not Found
- Ensure Tools directory is complete
- Add Tools folder to antivirus exclusion
- Check file permissions

#### Large File Processing
- Increase RAM (16GB+ recommended)
- Process in smaller batches
- Use SSD storage

### FAQ

**Q: Is DSTSTool GUI free?**
A: Yes, completely free and open-source under MIT license.

**Q: Can I use DSTSTool for other games?**
A: Designed specifically for Digimon Story: Time Stranger.

**Q: How to recover overwritten files?**
A: Always backup original files before processing.

**Q: Why is processing slow?**
A: Check RAM, storage type, and antivirus settings.

### Support
- [GitHub Issues](https://github.com/levi-soft/DSTSTools-VN/issues)
- Include: version, OS, Python version, error details

## 🤝 Contributing

We welcome contributions! This is an open-source project.

### How to Contribute
1. Fork the repository on GitHub
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a Pull Request

### Development Setup
```bash
git clone https://github.com/levi-soft/DSTSTools-VN.git
cd DSTSTool-GUI
pip install PyQt6
python DSTSToolGUIV2.py
```

### Report Issues
- Use [GitHub Issues](https://github.com/levi-soft/DSTSTools-VN/issues)
- Include: version, OS, Python version, error details

## 📝 Changelog

### [v2.0] - 2025-09-19
- Complete UI redesign with PyQt6
- 5 integrated tools: CPK, MVGL, IMG, MBE, TEXT
- Batch processing with progress tracking
- Enhanced error handling and process management

## 📄 License

DSTSTool GUI is distributed under the MIT License. See the `LICENSE` file for more details.

---

## 🔍 Keywords & Tags

### Primary Keywords
- DSTSTools
- Digimon Story: Time Stranger
- Digimon Story: Time Stranger mod
- Digimon Story: Time Stranger tool

### Tool Keywords
- Tool .mvgl
- Tool .cpk
- Tool .mbe
- Tool .img

### Category Tags
- game modding
- Python GUI
- file converter
- archive extractor
- modding tools
- game development
- file processing

### GitHub Topics (Recommended)
digimon, modding, tools, game-modding, python-gui, digimon-story-time-stranger, file-converter, archive-tools, game-tools

---

## 🚀 Quick Start for Digimon Story: Time Stranger Modders

**Latest Release**: [v2.0](https://github.com/levi-soft/DSTSTools-VN/releases/latest)

**Installation & Run**:
```bash
pip install PyQt6
python DSTSToolGUIV2.py
```

**Common Modding Workflows**:
- Extract .cpk files → Modify contents → Repack .cpk
- Convert .img textures to .png → Edit in image software → Convert back to .img
- Parse .mbe data to .csv → Edit values → Repack to .mbe
- Process .mvgl archives for 3D model/texture modding

## 📦 Downloads

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/levi-soft/DSTSTools-VN/issues)
- **README**: [English](README.md)

---

**Author**: Levi | **Version**: v2.0 | **License**: MIT