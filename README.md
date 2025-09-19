# DSTSTool GUI v2

DSTSTool GUI is a graphical user interface (GUI) application built with Python and PyQt6, providing tools for processing and converting popular game file formats. The application supports batch processing with progress monitoring and error handling.

## 📋 Table of Contents

- [Key Features](#-key-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Internal Tools](#-internal-tools)
- [Sources](#-sources)
- [System Requirements](#-system-requirements)
- [Contributing](#-contributing)
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

## 📦 Installation

### Requirements
- Python 3.8+
- PyQt6
- Internal tools (included)

### Install Dependencies
```bash
pip install PyQt6
```

### Run Application
```bash
python DSTSToolGUIV2.py
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

## 🔗 Sources

DSTSTool GUI uses the following open-source tools:

### 1. Compressonator
- **Source**: https://github.com/GPUOpen-Tools/compressonator
- **Usage**: IMG Tools - Texture conversion with BC7 compression
- **License**: MIT License

### 2. THL-MBE-Parser
- **Source**: https://github.com/Ahtheerr/THL-MBE-Parser
- **Usage**: MBE Tools - Parse and repack MBE files
- **License**: MIT License

### 3. DSCSTools
- **Source**: https://github.com/SydMontague/DSCSTools
- **Usage**: MVGL Tools - MVGL/DSCS file processing
- **License**: MIT License

### 4. YACpkTool
- **Source**: https://github.com/Brolijah/YACpkTool
- **Usage**: CPK Tools - CPK archive extraction/repacking
- **License**: MIT License

## 💻 System Requirements

- **OS**: Windows 10/11
- **Python**: 3.8 or higher
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 500MB for application and tools
- **Display**: 1280x720 minimum resolution

## ⚠️ Important Notes

1. **Backup Files**: Always backup original files before processing
2. **File Permissions**: Ensure read/write permissions for destination directories
3. **Large Files**: Some files may take considerable time to process
4. **Error Handling**: Application will display errors if issues occur
5. **Progress Monitoring**: Monitor progress bar for processing status

## 🤝 Contributing

We welcome all contributions! Please:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

DSTSTool GUI is distributed under the MIT License. See the `LICENSE` file for more details.

---

**Created by**: Levi
**Version**: v2.0
**Last Updated**: 2025-01-19

*This application is developed to support the game modding community and handle game files in an easy and efficient way.*