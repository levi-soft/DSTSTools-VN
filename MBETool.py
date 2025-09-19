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

    def __init__(self, commands, cwd=None, repack_func=None, total_files=0):
        super().__init__()
        self.commands = commands if isinstance(commands, list) else [commands]
        self.cwd = cwd
        self.repack_func = repack_func
        self.total_files = total_files

    def run(self):
        try:
            self.progress_signal.emit(5)  # Starting

            if self.repack_func:
                # Direct function call for MBE repacker - no process tracking needed
                total_commands = len(self.commands)
                self.progress_signal.emit(10)  # Ready to process

                for i, (input_dir, output_filepath) in enumerate(self.commands):
                    progress = 10 + int((i / total_commands) * 85)  # 10% to 95%
                    self.progress_signal.emit(progress)

                    try:
                        self.repack_func(input_dir, output_filepath)
                    except Exception as e:
                        self.progress_signal.emit(100)
                        self.finished_signal.emit(False, f"Error processing {input_dir}: {str(e)}")
                        return
            else:
                # Subprocess calls - track processes for cleanup
                total_commands = len(self.commands)
                self.progress_signal.emit(10)  # Ready to process

                for i, command in enumerate(self.commands):
                    progress = 10 + int((i / total_commands) * 85)  # 10% to 95%
                    self.progress_signal.emit(progress)

                    process = subprocess.Popen(
                        command,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                        text=True,
                        cwd=self.cwd
                    )

                    # Add process to global tracking list
                    running_processes.append(process)

                    # Wait for completion with progress updates
                    import time
                    start_time = time.time()
                    while True:
                        if process.poll() is not None:
                            break
                        # Small progress increment while waiting
                        elapsed = time.time() - start_time
                        if elapsed > 1.0:  # After 1 second, add small increment
                            current_progress = 10 + int((i / total_commands) * 85)
                            self.progress_signal.emit(min(95, current_progress + 2))
                        time.sleep(0.1)

                    rc = process.poll()
                    # Remove process from tracking list when done
                    if process in running_processes:
                        running_processes.remove(process)

                    if rc != 0:
                        self.progress_signal.emit(100)
                        self.finished_signal.emit(False, f"Error with command: {' '.join(command)}, Exit code {rc}")
                        return

            self.progress_signal.emit(100)
            if self.total_files > 0:
                self.finished_signal.emit(True, f"Completed successfully - {self.total_files} file(s) processed")
            else:
                self.finished_signal.emit(True, "Completed successfully")
        except Exception as e:
            self.progress_signal.emit(100)
            self.finished_signal.emit(False, f"Error: {str(e)}")

class MBETool(QWidget):
    """
    MBE Tools widget for batch processing MBE files.

    Features:
    - Extract MBE files to CSV format (batch processing)
    - Repack CSV directories back to MBE format (batch processing)
    - Progress monitoring with real-time updates
    - Process management for clean application exit
    """
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)

        # Parse section
        parse_group = QGroupBox("📤 Extract MBE to CSV (Batch)")
        parse_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #7E22CE;
                border-radius: 5px;
                margin-top: 1ex;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #7E22CE;
                font-size: 14px;
            }
        """)

        parse_layout = QVBoxLayout()

        # Source directory selection
        parse_source_layout = QHBoxLayout()
        parse_source_label = QLabel("Source Dir:")
        parse_source_label.setStyleSheet("font-weight: bold; color: #495057;")
        parse_source_layout.addWidget(parse_source_label)

        self.extract_source_edit = QLineEdit()
        self.extract_source_edit.setPlaceholderText("Select directory containing .MBE files...")
        self.extract_source_edit.setToolTip("Choose directory with MBE files to parse")
        parse_source_layout.addWidget(self.extract_source_edit)

        parse_source_btn = QPushButton("📂 Browse")
        parse_source_btn.setToolTip("Select source directory")
        parse_source_btn.clicked.connect(self.select_parse_source)
        parse_source_layout.addWidget(parse_source_btn)

        parse_layout.addLayout(parse_source_layout)

        # Target directory selection
        parse_target_layout = QHBoxLayout()
        parse_target_label = QLabel("Target Dir:")
        parse_target_label.setStyleSheet("font-weight: bold; color: #495057;")
        parse_target_layout.addWidget(parse_target_label)

        self.extract_target_edit = QLineEdit()
        self.extract_target_edit.setPlaceholderText("Select destination directory for CSV files...")
        self.extract_target_edit.setToolTip("Choose where to save parsed CSV files")
        parse_target_layout.addWidget(self.extract_target_edit)

        parse_target_btn = QPushButton("📂 Browse")
        parse_target_btn.setToolTip("Select destination directory")
        parse_target_btn.clicked.connect(self.select_parse_target)
        parse_target_layout.addWidget(parse_target_btn)

        parse_layout.addLayout(parse_target_layout)

        parse_btn = QPushButton("🚀 Extract Files")
        parse_btn.setToolTip("Start extracting MBE files to CSV")
        parse_btn.clicked.connect(self.parse_mbe)
        parse_layout.addWidget(parse_btn)

        parse_group.setLayout(parse_layout)
        layout.addWidget(parse_group)

        # Repack section
        repack_group = QGroupBox("📦 Repack CSV to MBE (Batch)")
        repack_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #EAB308;
                border-radius: 5px;
                margin-top: 1ex;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #EAB308;
                font-size: 14px;
            }
        """)

        repack_layout = QVBoxLayout()

        # Source directory selection
        repack_source_layout = QHBoxLayout()
        repack_source_label = QLabel("Source Dir:")
        repack_source_label.setStyleSheet("font-weight: bold; color: #495057;")
        repack_source_layout.addWidget(repack_source_label)

        self.pack_source_edit = QLineEdit()
        self.pack_source_edit.setPlaceholderText("Select directory containing CSV subdirectories...")
        self.pack_source_edit.setToolTip("Choose directory with CSV subdirectories to repack")
        repack_source_layout.addWidget(self.pack_source_edit)

        repack_source_btn = QPushButton("📂 Browse")
        repack_source_btn.setToolTip("Select source directory")
        repack_source_btn.clicked.connect(self.select_repack_source)
        repack_source_layout.addWidget(repack_source_btn)

        repack_layout.addLayout(repack_source_layout)

        # Target directory selection
        repack_target_layout = QHBoxLayout()
        repack_target_label = QLabel("Target Dir:")
        repack_target_label.setStyleSheet("font-weight: bold; color: #495057;")
        repack_target_layout.addWidget(repack_target_label)

        self.pack_target_edit = QLineEdit()
        self.pack_target_edit.setPlaceholderText("Select destination directory for MBE files...")
        self.pack_target_edit.setToolTip("Choose where to save repacked MBE files")
        repack_target_layout.addWidget(self.pack_target_edit)

        repack_target_btn = QPushButton("📂 Browse")
        repack_target_btn.setToolTip("Select destination directory")
        repack_target_btn.clicked.connect(self.select_repack_target)
        repack_target_layout.addWidget(repack_target_btn)

        repack_layout.addLayout(repack_target_layout)

        repack_btn = QPushButton("🔧 Repack Files")
        repack_btn.setToolTip("Start repacking CSV directories to MBE files")
        repack_btn.clicked.connect(self.repack_mbe)
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

    # File/Directory selection methods
    # ============================================================================
    # File/Directory Selection Methods
    # ============================================================================

    def select_parse_source(self):
        dir_path = QFileDialog.getExistingDirectory(self, "Select directory containing .MBE files")
        if dir_path:
            self.extract_source_edit.setText(dir_path)

    def select_parse_target(self):
        dir_path = QFileDialog.getExistingDirectory(self, "Select destination directory for CSV")
        if dir_path:
            self.extract_target_edit.setText(dir_path)

    def select_repack_source(self):
        dir_path = QFileDialog.getExistingDirectory(self, "Select directory containing CSV subdirectories")
        if dir_path:
            self.pack_source_edit.setText(dir_path)

    def select_repack_target(self):
        dir_path = QFileDialog.getExistingDirectory(self, "Select destination directory for MBE files")
        if dir_path:
            self.pack_target_edit.setText(dir_path)

    # ============================================================================
    # Main Action Methods
    # ============================================================================

    def parse_mbe(self):
        """Parse MBE files to CSV format (batch processing)"""
        source = self.extract_source_edit.text()
        target = self.extract_target_edit.text()
        if not source or not target:
            QMessageBox.warning(self, "Warning", "Please select source and destination directories")
            return

        mbe_files = self._scan_mbe_files(source)
        if not mbe_files:
            QMessageBox.warning(self, "Warning", "No .MBE files found in source directory")
            return

        commands = self._build_parse_commands(mbe_files, source)
        self.run_command(commands, cwd=target, total_files=len(mbe_files))


    def repack_mbe(self):
        """Repack CSV directories to MBE format (batch processing)"""
        source = self.pack_source_edit.text()
        target = self.pack_target_edit.text()
        if not source or not target:
            QMessageBox.warning(self, "Warning", "Please select source and destination directories")
            return

        csv_dirs = self._scan_csv_directories(source)
        if not csv_dirs:
            QMessageBox.warning(self, "Warning", "No directories containing CSV files found")
            return

        repack_func = self._import_repack_function()
        if not repack_func:
            return

        commands = self._build_repack_commands(csv_dirs, target)
        self.run_command(commands, repack_func=repack_func, total_files=len(csv_dirs))

    def _scan_csv_directories(self, source_dir):
        """Scan for directories containing CSV files"""
        csv_dirs = []
        for item in os.listdir(source_dir):
            item_path = os.path.join(source_dir, item)
            if os.path.isdir(item_path):
                # Check if directory contains CSV files
                if any(f.lower().endswith('.csv') for f in os.listdir(item_path)):
                    csv_dirs.append(item_path)
        return csv_dirs

    def _import_repack_function(self):
        """Import the MBE repack function"""
        # TODO: Update to use get_tools_path() when available
        tools_path = os.path.join(os.getcwd(), "Tools", "THL-MBE-Parser")
        if tools_path not in sys.path:
            sys.path.append(tools_path)
        try:
            from MBE_Repacker import repack_mbe  # type: ignore  # IDE may not recognize dynamic import
            return repack_mbe
        except ImportError as e:
            QMessageBox.critical(self, "Error", f"Cannot import MBE_Repacker.py: {str(e)}")
            return None

    def _build_repack_commands(self, csv_dirs, target_dir):
        """Build command list for repacking CSV directories"""
        commands = []
        for csv_dir in csv_dirs:
            # Calculate output filepath in target directory
            dir_name = os.path.basename(os.path.normpath(csv_dir))
            output_filename = dir_name + ".mbe"
            output_filepath = os.path.join(target_dir, output_filename)
            commands.append([csv_dir, output_filepath])
        return commands

    # ============================================================================
    # Command Execution and Progress Management
    # ============================================================================

    def run_command(self, commands, cwd=None, repack_func=None, total_files=0):
        """Execute commands in worker thread with progress monitoring"""
        self.progress_bar.setValue(0)
        self.worker = WorkerThread(commands, cwd, repack_func, total_files)
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

    # ============================================================================
    # Helper Methods
    # ============================================================================

    def _scan_mbe_files(self, source_dir):
        """Scan for MBE files in the source directory"""
        return [f for f in os.listdir(source_dir) if f.lower().endswith('.mbe')]

    def _build_parse_commands(self, mbe_files, source_dir):
        """Build command list for parsing MBE files"""
        commands = []
        tools_dir = os.path.join(os.getcwd(), "Tools", "THL-MBE-Parser")
        for mbe_file in mbe_files:
            full_path = os.path.join(source_dir, mbe_file)
            commands.append([sys.executable, os.path.join(tools_dir, "MBE_Parser.py"), full_path])
        return commands

    def _scan_csv_directories(self, source_dir):
        """Scan for directories containing CSV files"""
        csv_dirs = []
        for item in os.listdir(source_dir):
            item_path = os.path.join(source_dir, item)
            if os.path.isdir(item_path):
                # Check if directory contains CSV files
                if any(f.lower().endswith('.csv') for f in os.listdir(item_path)):
                    csv_dirs.append(item_path)
        return csv_dirs

    def _import_repack_function(self):
        """Import the MBE repack function"""
        tools_path = os.path.join(os.getcwd(), "Tools", "THL-MBE-Parser")
        if tools_path not in sys.path:
            sys.path.append(tools_path)
        try:
            from MBE_Repacker import repack_mbe  # type: ignore  # IDE may not recognize dynamic import
            return repack_mbe
        except ImportError as e:
            QMessageBox.critical(self, "Error", f"Cannot import MBE_Repacker.py: {str(e)}")
            return None

    def _build_repack_commands(self, csv_dirs, target_dir):
        """Build command list for repacking CSV directories"""
        commands = []
        for csv_dir in csv_dirs:
            # Calculate output filepath in target directory
            dir_name = os.path.basename(os.path.normpath(csv_dir))
            output_filename = dir_name + ".mbe"
            output_filepath = os.path.join(target_dir, output_filename)
            commands.append([csv_dir, output_filepath])
        return commands