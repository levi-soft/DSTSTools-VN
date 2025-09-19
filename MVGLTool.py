import os
import subprocess
import sys
import signal
import atexit
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QLineEdit, QFileDialog, QProgressBar, QMessageBox, QGroupBox
)
from PyQt6.QtCore import QThread, pyqtSignal

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
            process = subprocess.Popen(
                self.command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                cwd=os.path.dirname(sys.executable) if hasattr(sys, '_MEIPASS') else None
            )

            # Add process to global tracking list
            running_processes.append(process)

            self.progress_signal.emit(15)  # Process started

            # Monitor process with more granular progress
            import time
            start_time = time.time()
            estimated_duration = 300.0  # Assume 300 seconds for typical operations

            while True:
                if process.poll() is not None:
                    break

                # Calculate progress based on elapsed time
                elapsed = time.time() - start_time
                time_progress = min(70, int((elapsed / estimated_duration) * 70))
                self.progress_signal.emit(15 + time_progress)

                # Read output to prevent blocking
                output = process.stdout.readline()
                if output:
                    # Could parse output for more specific progress if available
                    pass

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

class MVGLTool(QWidget):
    """
    MVGL Tools widget for batch processing MVGL files.

    Features:
    - Extract MVGL files to individual files
    - Repack individual files back into MVGL format
    - Progress monitoring with real-time updates
    - Process management for clean application exit
    - Uses DSCSTools CLI for high-quality conversions
    """
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)

        # Extract section
        extract_group = QGroupBox("📤 Extract MVGL File")
        extract_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #1E3A8A;
                border-radius: 5px;
                margin-top: 1ex;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #1E3A8A;
                font-size: 14px;
            }
        """)

        extract_layout = QVBoxLayout()

        # Source file selection
        source_layout = QHBoxLayout()
        source_label = QLabel("Source File:")
        source_label.setStyleSheet("font-weight: bold; color: #495057;")
        source_layout.addWidget(source_label)

        self.extract_source_edit = QLineEdit()
        self.extract_source_edit.setPlaceholderText("Select MVGL file to extract...")
        self.extract_source_edit.setToolTip("Choose the MVGL file you want to extract")
        source_layout.addWidget(self.extract_source_edit)

        extract_source_btn = QPushButton("📄 Browse")
        extract_source_btn.setToolTip("Select MVGL file")
        extract_source_btn.clicked.connect(self.select_extract_source)
        source_layout.addWidget(extract_source_btn)

        extract_layout.addLayout(source_layout)

        # Target directory selection
        target_layout = QHBoxLayout()
        target_label = QLabel("Target Dir:")
        target_label.setStyleSheet("font-weight: bold; color: #495057;")
        target_layout.addWidget(target_label)

        self.extract_target_edit = QLineEdit()
        self.extract_target_edit.setPlaceholderText("Select destination directory...")
        self.extract_target_edit.setToolTip("Choose where to extract the files")
        target_layout.addWidget(self.extract_target_edit)

        extract_target_btn = QPushButton("📂 Browse")
        extract_target_btn.setToolTip("Select destination directory")
        extract_target_btn.clicked.connect(self.select_extract_target)
        target_layout.addWidget(extract_target_btn)

        extract_layout.addLayout(target_layout)

        extract_btn = QPushButton("🚀 Extract Files")
        extract_btn.setToolTip("Start extracting MVGL file")
        extract_btn.clicked.connect(self.extract)
        extract_layout.addWidget(extract_btn)

        extract_group.setLayout(extract_layout)
        layout.addWidget(extract_group)

        # Pack section
        pack_group = QGroupBox("📦 Repack File to MVGL")
        pack_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #FB923C;
                border-radius: 5px;
                margin-top: 1ex;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #FB923C;
                font-size: 14px;
            }
        """)

        pack_layout = QVBoxLayout()

        # Source directory selection
        pack_source_layout = QHBoxLayout()
        pack_source_label = QLabel("Source Dir:")
        pack_source_label.setStyleSheet("font-weight: bold; color: #495057;")
        pack_source_layout.addWidget(pack_source_label)

        self.pack_source_edit = QLineEdit()
        self.pack_source_edit.setPlaceholderText("Select directory containing files to pack...")
        self.pack_source_edit.setToolTip("Choose the directory with files to pack into MVGL")
        pack_source_layout.addWidget(self.pack_source_edit)

        pack_source_btn = QPushButton("📂 Browse")
        pack_source_btn.setToolTip("Select source directory")
        pack_source_btn.clicked.connect(self.select_pack_source)
        pack_source_layout.addWidget(pack_source_btn)

        pack_layout.addLayout(pack_source_layout)

        # Target file selection
        pack_target_layout = QHBoxLayout()
        pack_target_label = QLabel("Target File:")
        pack_target_label.setStyleSheet("font-weight: bold; color: #495057;")
        pack_target_layout.addWidget(pack_target_label)

        self.pack_target_edit = QLineEdit()
        self.pack_target_edit.setPlaceholderText("Enter output MVGL file path...")
        self.pack_target_edit.setToolTip("Choose where to save the packed MVGL file")
        pack_target_layout.addWidget(self.pack_target_edit)

        pack_target_btn = QPushButton("💾 Browse")
        pack_target_btn.setToolTip("Select output file")
        pack_target_btn.clicked.connect(self.select_pack_target)
        pack_target_layout.addWidget(pack_target_btn)

        pack_layout.addLayout(pack_target_layout)

        pack_btn = QPushButton("🔧 Repack Files")
        pack_btn.setToolTip("Start repacking files into MVGL")
        pack_btn.clicked.connect(self.pack)
        pack_layout.addWidget(pack_btn)

        pack_group.setLayout(pack_layout)
        layout.addWidget(pack_group)

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

    def select_extract_source(self):
        """Select source MVGL file for extraction"""
        file_path, _ = QFileDialog.getOpenFileName(self, "Select source file to extract", "", "MVGL Files (*.mvgl);;All Files (*)")
        if file_path:
            self.extract_source_edit.setText(file_path)

    def select_extract_target(self):
        """Select destination directory for extracted files"""
        dir_path = QFileDialog.getExistingDirectory(self, "Select destination directory for extract")
        if dir_path:
            self.extract_target_edit.setText(dir_path)

    def select_pack_source(self):
        """Select source directory containing files to pack"""
        dir_path = QFileDialog.getExistingDirectory(self, "Select source directory to pack")
        if dir_path:
            self.pack_source_edit.setText(dir_path)

    def select_pack_target(self):
        """Select destination MVGL file for packing"""
        file_path, _ = QFileDialog.getSaveFileName(self, "Select destination file for pack", "", "MVGL Files (*.mvgl);;All Files (*)")
        if file_path:
            # Ensure .mvgl extension
            if not file_path.lower().endswith('.mvgl'):
                file_path += '.mvgl'
            self.pack_target_edit.setText(file_path)

    # ============================================================================
    # Main Processing Methods
    # ============================================================================

    def extract(self):
        """Extract files from MVGL archive"""
        source = self.extract_source_edit.text()
        target = self.extract_target_edit.text()
        if not source or not target:
            QMessageBox.warning(self, "Warning", "Please select source file and destination directory")
            return

        tools_dir = os.path.join(os.getcwd(), "Tools", "DSCSTools")
        # TODO: Update to use get_tools_path() when available
        command = [os.path.join(tools_dir, "DSCSToolsCLI.exe"), "--extract", source, target]
        self.run_command(command)

    def pack(self):
        """Pack files into MVGL archive"""
        source = self.pack_source_edit.text()
        target = self.pack_target_edit.text()
        if not source or not target:
            QMessageBox.warning(self, "Warning", "Please select source directory and destination file")
            return

        tools_dir = os.path.join(os.getcwd(), "Tools", "DSCSTools")
        command = [os.path.join(tools_dir, "DSCSToolsCLI.exe"), "--pack", source, target]
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