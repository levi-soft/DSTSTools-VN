import os
import subprocess
import sys
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QLineEdit, QFileDialog, QProgressBar, QMessageBox, QGroupBox
)
from PyQt6.QtCore import QThread, pyqtSignal

class WorkerThread(QThread):
    progress_signal = pyqtSignal(int)
    output_signal = pyqtSignal(str)
    finished_signal = pyqtSignal(bool, str)

    def __init__(self, func, *args):
        super().__init__()
        self.func = func
        self.args = args

    def run(self):
        try:
            self.progress_signal.emit(10)
            result = self.func(self, *self.args)
            self.progress_signal.emit(100)
            self.finished_signal.emit(True, result)
        except Exception as e:
            self.finished_signal.emit(False, f"Error: {str(e)}")

class IMGTool(QWidget):
    """
    IMG Tools widget for batch image conversion.

    Features:
    - Convert IMG files to PNG format (batch processing)
    - Convert PNG files to IMG format with BC7 compression (batch processing)
    - Progress monitoring with real-time updates
    - Automatic DDS extension management
    - Uses Compressonator CLI for high-quality conversions
    """
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)

        # IMG to PNG section
        img2png_group = QGroupBox("🖼️ Convert IMG to PNG (Batch)")
        img2png_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #14B8A6;
                border-radius: 5px;
                margin-top: 1ex;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #14B8A6;
                font-size: 14px;
            }
        """)

        img2png_layout = QVBoxLayout()

        # Source directory selection
        img2png_source_layout = QHBoxLayout()
        img2png_source_label = QLabel("Source Dir:")
        img2png_source_label.setStyleSheet("font-weight: bold; color: #495057;")
        img2png_source_layout.addWidget(img2png_source_label)

        self.img2png_source_edit = QLineEdit()
        self.img2png_source_edit.setPlaceholderText("Select directory containing IMG files...")
        self.img2png_source_edit.setToolTip("Choose directory with IMG files to convert to PNG")
        img2png_source_layout.addWidget(self.img2png_source_edit)

        img2png_source_btn = QPushButton("📂 Browse")
        img2png_source_btn.setToolTip("Select source directory")
        img2png_source_btn.clicked.connect(self.select_img2png_source)
        img2png_source_layout.addWidget(img2png_source_btn)

        img2png_layout.addLayout(img2png_source_layout)

        # Target directory selection
        img2png_target_layout = QHBoxLayout()
        img2png_target_label = QLabel("Target Dir:")
        img2png_target_label.setStyleSheet("font-weight: bold; color: #495057;")
        img2png_target_layout.addWidget(img2png_target_label)

        self.img2png_target_edit = QLineEdit()
        self.img2png_target_edit.setPlaceholderText("Select destination directory for PNG files...")
        self.img2png_target_edit.setToolTip("Choose where to save converted PNG files")
        img2png_target_layout.addWidget(self.img2png_target_edit)

        img2png_target_btn = QPushButton("📂 Browse")
        img2png_target_btn.setToolTip("Select destination directory")
        img2png_target_btn.clicked.connect(self.select_img2png_target)
        img2png_target_layout.addWidget(img2png_target_btn)

        img2png_layout.addLayout(img2png_target_layout)

        img2png_btn = QPushButton("🔄 Convert to PNG")
        img2png_btn.setToolTip("Start converting IMG files to PNG")
        img2png_btn.clicked.connect(self.convert_img_to_png)
        img2png_layout.addWidget(img2png_btn)

        img2png_group.setLayout(img2png_layout)
        layout.addWidget(img2png_group)

        # PNG to IMG section
        png2img_group = QGroupBox("🎨 Convert PNG to IMG (Batch)")
        png2img_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #F43F5E;
                border-radius: 5px;
                margin-top: 1ex;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #F43F5E;
                font-size: 14px;
            }
        """)

        png2img_layout = QVBoxLayout()

        # Source directory selection
        png2img_source_layout = QHBoxLayout()
        png2img_source_label = QLabel("Source Dir:")
        png2img_source_label.setStyleSheet("font-weight: bold; color: #495057;")
        png2img_source_layout.addWidget(png2img_source_label)

        self.png2img_source_edit = QLineEdit()
        self.png2img_source_edit.setPlaceholderText("Select directory containing PNG files...")
        self.png2img_source_edit.setToolTip("Choose directory with PNG files to convert to IMG")
        png2img_source_layout.addWidget(self.png2img_source_edit)

        png2img_source_btn = QPushButton("📂 Browse")
        png2img_source_btn.setToolTip("Select source directory")
        png2img_source_btn.clicked.connect(self.select_png2img_source)
        png2img_source_layout.addWidget(png2img_source_btn)

        png2img_layout.addLayout(png2img_source_layout)

        # Target directory selection
        png2img_target_layout = QHBoxLayout()
        png2img_target_label = QLabel("Target Dir:")
        png2img_target_label.setStyleSheet("font-weight: bold; color: #495057;")
        png2img_target_layout.addWidget(png2img_target_label)

        self.png2img_target_edit = QLineEdit()
        self.png2img_target_edit.setPlaceholderText("Select destination directory for IMG files...")
        self.png2img_target_edit.setToolTip("Choose where to save converted IMG files")
        png2img_target_layout.addWidget(self.png2img_target_edit)

        png2img_target_btn = QPushButton("📂 Browse")
        png2img_target_btn.setToolTip("Select destination directory")
        png2img_target_btn.clicked.connect(self.select_png2img_target)
        png2img_target_layout.addWidget(png2img_target_btn)

        png2img_layout.addLayout(png2img_target_layout)

        png2img_btn = QPushButton("🔄 Convert to IMG")
        png2img_btn.setToolTip("Start converting PNG files to IMG (BC7 compression)")
        png2img_btn.clicked.connect(self.convert_png_to_img)
        png2img_layout.addWidget(png2img_btn)

        png2img_group.setLayout(png2img_layout)
        layout.addWidget(png2img_group)

        # Progress bar - compact
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setMaximumHeight(20)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

    # ============================================================================
    # Directory Selection Methods
    # ============================================================================

    def select_img2png_source(self):
        """Select source directory containing IMG files for PNG conversion"""
        dir_path = QFileDialog.getExistingDirectory(self, "Select directory containing IMG files")
        if dir_path:
            self.img2png_source_edit.setText(dir_path)

    def select_img2png_target(self):
        """Select destination directory for PNG files"""
        dir_path = QFileDialog.getExistingDirectory(self, "Select destination directory for PNG files")
        if dir_path:
            self.img2png_target_edit.setText(dir_path)

    def select_png2img_source(self):
        """Select source directory containing PNG files for IMG conversion"""
        dir_path = QFileDialog.getExistingDirectory(self, "Select directory containing PNG files")
        if dir_path:
            self.png2img_source_edit.setText(dir_path)

    def select_png2img_target(self):
        """Select destination directory for IMG files"""
        dir_path = QFileDialog.getExistingDirectory(self, "Select destination directory for IMG files")
        if dir_path:
            self.png2img_target_edit.setText(dir_path)

    # ============================================================================
    # Main Conversion Methods
    # ============================================================================

    def convert_img_to_png(self):
        """Convert IMG files to PNG format (batch processing)"""
        source = self.img2png_source_edit.text()
        target = self.img2png_target_edit.text()
        if not source or not target:
            QMessageBox.warning(self, "Warning", "Please select source and destination directories")
            return

        self.progress_bar.setValue(0)
        self.worker = WorkerThread(self._convert_img_to_png, source, target)
        self.worker.progress_signal.connect(self.update_progress)
        self.worker.finished_signal.connect(self.command_finished)
        self.worker.start()

    def convert_png_to_img(self):
        """Convert PNG files to IMG format with BC7 compression (batch processing)"""
        source = self.png2img_source_edit.text()
        target = self.png2img_target_edit.text()
        if not source or not target:
            QMessageBox.warning(self, "Warning", "Please select source and destination directories")
            return

        self.progress_bar.setValue(0)
        self.worker = WorkerThread(self._convert_png_to_img, source, target)
        self.worker.progress_signal.connect(self.update_progress)
        self.worker.finished_signal.connect(self.command_finished)
        self.worker.start()

    # ============================================================================
    # Conversion Implementation Methods
    # ============================================================================

    def _convert_img_to_png(self, worker, source, target):
        """Convert IMG files to PNG format using Compressonator CLI"""
        worker.progress_signal.emit(5)  # Starting
        worker.progress_signal.emit(10)  # Initializing

        # Step 1: Add .dds extension to files
        worker.progress_signal.emit(15)  # Preparing files
        self._add_dds_extension(source)
        worker.progress_signal.emit(25)  # Files prepared

        # Step 2: Convert DDS to PNG using compressonatorcli
        # TODO: Update to use get_tools_path() when available
        compressonator_path = os.path.join(os.getcwd(), "Tools", "compressonator", "compressonatorcli.exe")

        # Check if compressonatorcli exists
        if not os.path.exists(compressonator_path):
            return f"Error: compressonatorcli.exe not found at {compressonator_path}"

        worker.progress_signal.emit(30)  # Tool verified, scanning files

        # For batch processing with DDS files, use -fd with decompression or direct conversion
        # Try a different approach - convert each DDS file individually
        dds_files = [f for f in os.listdir(source) if f.lower().endswith('.dds')]

        if not dds_files:
            return "Error: No DDS files found in source directory"

        worker.progress_signal.emit(35)  # Files found, starting conversion

        # Convert each DDS file to PNG individually
        success_count = 0
        total_files = len(dds_files)

        for i, dds_file in enumerate(dds_files):
            progress = 35 + int((i / total_files) * 50)  # Progress from 35% to 85%
            worker.progress_signal.emit(progress)

            dds_path = os.path.join(source, dds_file)
            png_filename = dds_file[:-4] + '.png'  # Remove .dds and add .png
            png_path = os.path.join(target, png_filename)

            # Use single file conversion
            cmd = [compressonator_path, dds_path, png_path]

            result = subprocess.run(cmd, capture_output=True, text=True, cwd=os.path.dirname(compressonator_path))

            if result.returncode == 0:
                success_count += 1
                worker.output_signal.emit(f"Converted: {dds_file} → {png_filename}")
            else:
                worker.output_signal.emit(f"Conversion error {dds_file}: {result.stderr}")

        if success_count == 0:
            return f"Error: Could not convert any files. Check DDS file format."

        # Step 3: Remove .dds extension
        worker.progress_signal.emit(90)  # Conversion complete, cleaning up
        self._remove_dds_extension(source)
        worker.progress_signal.emit(95)  # Cleanup complete

        return f"Conversion completed {success_count}/{total_files} file IMG to PNG"

    def _convert_png_to_img(self, worker, source, target):
        """Convert PNG files to IMG format with BC7 compression using Compressonator CLI"""
        worker.progress_signal.emit(5)  # Starting
        worker.progress_signal.emit(10)  # Initializing

        # Step 1: Convert PNG to DDS using compressonatorcli
        compressonator_path = os.path.join(os.getcwd(), "Tools", "compressonator", "compressonatorcli.exe")

        # Check if compressonatorcli exists
        if not os.path.exists(compressonator_path):
            return f"Error: compressonatorcli.exe not found at {compressonator_path}"

        worker.progress_signal.emit(15)  # Tool verified, scanning files

        # Convert each PNG file to DDS individually
        png_files = [f for f in os.listdir(source) if f.lower().endswith('.png')]

        if not png_files:
            return "Error: No PNG files found in source directory"

        worker.progress_signal.emit(20)  # Files found, starting conversion

        # Convert each PNG file to DDS with BC7 compression
        success_count = 0
        total_files = len(png_files)

        for i, png_file in enumerate(png_files):
            progress = 20 + int((i / total_files) * 65)  # Progress from 20% to 85%
            worker.progress_signal.emit(progress)

            png_path = os.path.join(source, png_file)
            dds_filename = png_file[:-4] + '.dds'  # Remove .png and add .dds
            dds_path = os.path.join(target, dds_filename)

            # Use single file conversion with BC7 compression
            cmd = [compressonator_path, "-fd", "BC7", png_path, dds_path]

            result = subprocess.run(cmd, capture_output=True, text=True, cwd=os.path.dirname(compressonator_path))

            if result.returncode == 0:
                success_count += 1
                worker.output_signal.emit(f"Converted: {png_file} → {dds_filename}")
            else:
                worker.output_signal.emit(f"Conversion error {png_file}: {result.stderr}")

        if success_count == 0:
            return f"Error: Could not convert any files. Check PNG file format."

        # Step 2: Remove .dds extension
        worker.progress_signal.emit(90)  # Conversion complete, cleaning up
        self._remove_dds_extension(target)
        worker.progress_signal.emit(95)  # Cleanup complete

        return f"Conversion completed {success_count}/{total_files} file PNG to IMG"

    # ============================================================================
    # File Management Helper Methods
    # ============================================================================

    def _add_dds_extension(self, folder):
        """Add .dds extension to all files in folder for Compressonator compatibility"""
        for filename in os.listdir(folder):
            filepath = os.path.join(folder, filename)
            if os.path.isfile(filepath) and not filename.lower().endswith('.dds'):
                new_filepath = filepath + '.dds'
                os.rename(filepath, new_filepath)

    def _remove_dds_extension(self, folder):
        """Remove .dds extension from all files in folder to restore original names"""
        for filename in os.listdir(folder):
            if filename.lower().endswith('.dds'):
                filepath = os.path.join(folder, filename)
                new_filepath = filepath[:-4]  # Remove .dds
                os.rename(filepath, new_filepath)

    # ============================================================================
    # Progress and UI Update Methods
    # ============================================================================

    def update_progress(self, value):
        """Update progress bar value"""
        self.progress_bar.setValue(value)

    def command_finished(self, success, message):
        """Handle conversion completion with user notification"""
        self.progress_bar.setValue(100)
        if success:
            QMessageBox.information(self, "Success", message)
        else:
            QMessageBox.critical(self, "Error", message)