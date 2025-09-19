import os
import subprocess
import sys
import signal
import atexit

# Import for Windows-specific subprocess flags
if sys.platform == 'win32':
    CREATE_NO_WINDOW = subprocess.CREATE_NO_WINDOW
else:
    CREATE_NO_WINDOW = 0
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QLineEdit, QFileDialog, QProgressBar, QMessageBox, QGroupBox
)
from PyQt6.QtCore import QThread, pyqtSignal

# Import path utilities from main application
try:
    from DSTSToolGUIV2 import get_tools_path
except ImportError:
    # Fallback for standalone usage
    def get_tools_path():
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), "Tools")

# Global list to track running processes
running_processes = []

def cleanup_processes():
    """Cleanup function to terminate all running processes when application exits"""
    for process in running_processes[:]:  # Copy list to avoid modification during iteration
        try:
            if process.poll() is None:  # Process is still running
                process.terminate()
                # Wait a bit for graceful termination
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    # Force kill if it doesn't terminate gracefully
                    process.kill()
                    process.wait()
            running_processes.remove(process)
        except Exception:
            pass

# Register cleanup function
atexit.register(cleanup_processes)

# Handle application exit signals
def signal_handler(signum, frame):
    cleanup_processes()
    sys.exit(0)

signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

class WorkerThread(QThread):
    progress_signal = pyqtSignal(int)
    finished_signal = pyqtSignal(bool, str)

    def __init__(self, command):
        super().__init__()
        self.command = command

    def run(self):
        process = None
        try:
            self.progress_signal.emit(5)  # Starting process
            import time
            start_time = time.time()
            estimated_duration = 4.0  # Assume 4 seconds for CPK operations

            # Use subprocess.Popen without capturing output to avoid console handle issues
            # but still allow monitoring of the process
            process = subprocess.Popen(
                self.command,
                cwd=os.path.dirname(sys.executable) if hasattr(sys, '_MEIPASS') else None,
                creationflags=CREATE_NO_WINDOW
            )

            # Add process to global tracking list
            running_processes.append(process)

            self.progress_signal.emit(15)  # Process started

            # Monitor process with time-based progress updates
            while True:
                if process.poll() is not None:
                    break

                # Calculate progress based on elapsed time
                elapsed = time.time() - start_time
                time_progress = min(80, int((elapsed / estimated_duration) * 80))
                self.progress_signal.emit(15 + time_progress)

                time.sleep(0.1)  # Small delay to prevent CPU overuse

            rc = process.poll()
            self.progress_signal.emit(95)  # Almost done

            if rc == 0:
                self.progress_signal.emit(100)
                self.finished_signal.emit(True, "Completed successfully")
            else:
                self.progress_signal.emit(100)
                self.finished_signal.emit(False, f"Error: Exit code {rc}")
        except Exception as e:
            self.progress_signal.emit(100)
            self.finished_signal.emit(False, f"Error: {str(e)}")
        finally:
            # Remove process from tracking list when done
            if process and process in running_processes:
                running_processes.remove(process)

class CPKTool(QWidget):
    """
    CPK Tools widget for batch processing CPK files.

    Features:
    - Extract CPK files to individual files
    - Repack individual files back into CPK format
    - Progress monitoring with real-time updates
    - Process management for clean application exit
    - Uses YACpkTool for high-quality CPK operations
    """
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)

        # Extract Files section
        extract_group = QGroupBox("📤 Extract CPK File")
        extract_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #DC2626;
                border-radius: 5px;
                margin-top: 1ex;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #DC2626;
                font-size: 14px;
            }
        """)

        extract_layout = QVBoxLayout()

        # Input CPK file selection
        extract_input_layout = QHBoxLayout()
        extract_input_label = QLabel("Source File:")
        extract_input_label.setStyleSheet("font-weight: bold; color: #495057;")
        extract_input_layout.addWidget(extract_input_label)

        self.extract_input_edit = QLineEdit()
        self.extract_input_edit.setPlaceholderText("Select CPK file to extract...")
        self.extract_input_edit.setToolTip("Choose the CPK file you want to extract")
        extract_input_layout.addWidget(self.extract_input_edit)

        extract_input_btn = QPushButton("📄 Browse")
        extract_input_btn.setToolTip("Select CPK file")
        extract_input_btn.clicked.connect(self.select_extract_input)
        extract_input_layout.addWidget(extract_input_btn)

        extract_layout.addLayout(extract_input_layout)

        # Output directory selection
        extract_output_layout = QHBoxLayout()
        extract_output_label = QLabel("Target Dir:")
        extract_output_label.setStyleSheet("font-weight: bold; color: #495057;")
        extract_output_layout.addWidget(extract_output_label)

        self.extract_output_edit = QLineEdit()
        self.extract_output_edit.setPlaceholderText("Select destination directory...")
        self.extract_output_edit.setToolTip("Choose where to extract the files")
        extract_output_layout.addWidget(self.extract_output_edit)

        extract_output_btn = QPushButton("📂 Browse")
        extract_output_btn.setToolTip("Select output directory")
        extract_output_btn.clicked.connect(self.select_extract_output)
        extract_output_layout.addWidget(extract_output_btn)

        extract_layout.addLayout(extract_output_layout)

        extract_btn = QPushButton("🚀 Extract Files")
        extract_btn.setToolTip("Start extracting files from CPK")
        extract_btn.clicked.connect(self.extract_files)
        extract_layout.addWidget(extract_btn)

        extract_group.setLayout(extract_layout)
        layout.addWidget(extract_group)

        # Repack Files section
        repack_group = QGroupBox("📦 Repack Files to CPK")
        repack_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #22C55E;
                border-radius: 5px;
                margin-top: 1ex;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #22C55E;
                font-size: 14px;
            }
        """)

        repack_layout = QVBoxLayout()

        # Input directory selection
        repack_input_layout = QHBoxLayout()
        repack_input_label = QLabel("Source Dir:")
        repack_input_label.setStyleSheet("font-weight: bold; color: #495057;")
        repack_input_layout.addWidget(repack_input_label)

        self.repack_input_edit = QLineEdit()
        self.repack_input_edit.setPlaceholderText("Select directory containing files to pack...")
        self.repack_input_edit.setToolTip("Choose directory with files to pack into CPK")
        repack_input_layout.addWidget(self.repack_input_edit)

        repack_input_btn = QPushButton("📂 Browse")
        repack_input_btn.setToolTip("Select input directory")
        repack_input_btn.clicked.connect(self.select_repack_input)
        repack_input_layout.addWidget(repack_input_btn)

        repack_layout.addLayout(repack_input_layout)

        # Output CPK file selection
        repack_output_layout = QHBoxLayout()
        repack_output_label = QLabel("Target File:")
        repack_output_label.setStyleSheet("font-weight: bold; color: #495057;")
        repack_output_layout.addWidget(repack_output_label)

        self.repack_output_edit = QLineEdit()
        self.repack_output_edit.setPlaceholderText("Enter output CPK file path...")
        self.repack_output_edit.setToolTip("Enter the path for the output CPK file")
        repack_output_layout.addWidget(self.repack_output_edit)

        repack_output_btn = QPushButton("💾 Browse")
        repack_output_btn.setToolTip("Select output CPK file location")
        repack_output_btn.clicked.connect(self.select_repack_output)
        repack_output_layout.addWidget(repack_output_btn)

        repack_layout.addLayout(repack_output_layout)

        repack_btn = QPushButton("🔧 Repack Files")
        repack_btn.setToolTip("Start packing files into CPK")
        repack_btn.clicked.connect(self.repack_files)
        repack_layout.addWidget(repack_btn)

        repack_group.setLayout(repack_layout)
        layout.addWidget(repack_group)

        # Progress bar - compact
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setMaximumHeight(20)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

    # ============================================================================
    # File/Directory Selection Methods
    # ============================================================================

    def select_extract_input(self):
        """Select source CPK file for extraction"""
        file_path, _ = QFileDialog.getOpenFileName(self, "Select CPK file", "", "CPK files (*.cpk);;All files (*)")
        if file_path:
            self.extract_input_edit.setText(file_path)

    def select_extract_output(self):
        """Select destination directory for extracted files"""
        dir_path = QFileDialog.getExistingDirectory(self, "Select output directory")
        if dir_path:
            self.extract_output_edit.setText(dir_path)

    def select_repack_input(self):
        """Select source directory containing files to pack"""
        dir_path = QFileDialog.getExistingDirectory(self, "Select input directory")
        if dir_path:
            self.repack_input_edit.setText(dir_path)

    def select_repack_output(self):
        """Select destination CPK file for packing"""
        file_path, _ = QFileDialog.getSaveFileName(self, "Save CPK file", "", "CPK files (*.cpk);;All files (*)")
        if file_path:
            self.repack_output_edit.setText(file_path)

    # ============================================================================
    # Main Processing Methods
    # ============================================================================

    def extract_files(self):
        """Extract files from CPK archive"""
        input_file = self.extract_input_edit.text()
        output_dir = self.extract_output_edit.text()
        if not input_file or not output_dir:
            QMessageBox.warning(self, "Warning", "Please select input CPK file and output directory")
            return

        # Check if YACpkTool.exe exists
        yacpktool_path = os.path.join(get_tools_path(), "YACpkTool", "YACpkTool.exe")
        if not os.path.exists(yacpktool_path):
            QMessageBox.critical(self, "Error", f"YACpkTool.exe not found at {yacpktool_path}")
            return

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Execute extract command: YACpkTool.exe <INPUT_CPK> <OUT_FOLDER>
        command = [yacpktool_path, input_file, output_dir]
        self.run_command(command)

    def repack_files(self):
        """Repack files into CPK archive"""
        input_dir = self.repack_input_edit.text()
        output_file = self.repack_output_edit.text()
        if not input_dir or not output_file:
            QMessageBox.warning(self, "Warning", "Please select input directory and output CPK file")
            return

        # Check if YACpkTool.exe exists
        yacpktool_path = os.path.join(get_tools_path(), "YACpkTool", "YACpkTool.exe")
        if not os.path.exists(yacpktool_path):
            QMessageBox.critical(self, "Error", f"YACpkTool.exe not found at {yacpktool_path}")
            return

        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_file)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        # Execute repack command: YACpkTool.exe <IN_FOLDER> <OUT_CPK_FILE>
        command = [yacpktool_path, input_dir, output_file]
        self.run_command(command)


    # ============================================================================
    # Command Execution and Progress Management
    # ============================================================================

    def run_command(self, command):
        """Execute command in worker thread with progress monitoring"""
        self.progress_bar.setValue(0)
        self.worker = WorkerThread(command)
        self.worker.progress_signal.connect(self.update_progress)
        self.worker.finished_signal.connect(self.command_finished)
        self.worker.start()

    # ============================================================================
    # Progress and UI Update Methods
    # ============================================================================

    def update_progress(self, value):
        """Update progress bar value"""
        self.progress_bar.setValue(value)

    def command_finished(self, success, message):
        """Handle command completion with user notification"""
        self.progress_bar.setValue(100)
        if success:
            QMessageBox.information(self, "Success", message)
        else:
            QMessageBox.critical(self, "Error", message)