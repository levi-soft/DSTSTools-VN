import os
import csv
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QLineEdit, QFileDialog, QProgressBar, QMessageBox, QGroupBox
)
from PyQt6.QtCore import QThread, pyqtSignal

class WorkerThread(QThread):
    progress_signal = pyqtSignal(int)
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

class TEXTTool(QWidget):
    """
    TEXT Tools widget for CSV/TSV file processing.

    Features:
    - Merge multiple CSV files from subdirectories into a single TSV file
    - Split TSV file back into multiple CSV files organized by subdirectories
    - Progress monitoring with real-time updates
    - Automatic metadata handling for file organization
    - Line break escaping/unescaping for data integrity
    """
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)

        # Merge section
        merge_group = QGroupBox("🔗 Merge CSV to TSV")
        merge_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #374151;
                border-radius: 5px;
                margin-top: 1ex;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #374151;
                font-size: 14px;
            }
        """)

        merge_layout = QVBoxLayout()

        # Source directory selection
        merge_source_layout = QHBoxLayout()
        merge_source_label = QLabel("Source Dir:")
        merge_source_label.setStyleSheet("font-weight: bold; color: #495057;")
        merge_source_layout.addWidget(merge_source_label)

        self.merge_source_edit = QLineEdit()
        self.merge_source_edit.setPlaceholderText("Select directory containing CSV subdirectories...")
        self.merge_source_edit.setToolTip("Choose directory with CSV subdirectories to merge")
        merge_source_layout.addWidget(self.merge_source_edit)

        merge_source_btn = QPushButton("📂 Browse")
        merge_source_btn.setToolTip("Select source directory")
        merge_source_btn.clicked.connect(self.select_merge_source)
        merge_source_layout.addWidget(merge_source_btn)

        merge_layout.addLayout(merge_source_layout)

        # Target file selection
        merge_target_layout = QHBoxLayout()
        merge_target_label = QLabel("Target File:")
        merge_target_label.setStyleSheet("font-weight: bold; color: #495057;")
        merge_target_layout.addWidget(merge_target_label)

        self.merge_target_edit = QLineEdit()
        self.merge_target_edit.setPlaceholderText("Select output TSV file...")
        self.merge_target_edit.setToolTip("Choose where to save the merged TSV file")
        merge_target_layout.addWidget(self.merge_target_edit)

        merge_target_btn = QPushButton("💾 Browse")
        merge_target_btn.setToolTip("Select output file")
        merge_target_btn.clicked.connect(self.select_merge_target)
        merge_target_layout.addWidget(merge_target_btn)

        merge_layout.addLayout(merge_target_layout)

        merge_btn = QPushButton("🔄 Merge to TSV")
        merge_btn.setToolTip("Start merging CSV files to TSV")
        merge_btn.clicked.connect(self.merge_csv_to_tsv)
        merge_layout.addWidget(merge_btn)

        merge_group.setLayout(merge_layout)
        layout.addWidget(merge_group)

        # Split section
        split_group = QGroupBox("✂️ Split TSV to CSV")
        split_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #3B82F6;
                border-radius: 5px;
                margin-top: 1ex;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #3B82F6;
                font-size: 14px;
            }
        """)

        split_layout = QVBoxLayout()

        # Source file selection
        split_source_layout = QHBoxLayout()
        split_source_label = QLabel("Source File:")
        split_source_label.setStyleSheet("font-weight: bold; color: #495057;")
        split_source_layout.addWidget(split_source_label)

        self.split_source_edit = QLineEdit()
        self.split_source_edit.setPlaceholderText("Select TSV file to split...")
        self.split_source_edit.setToolTip("Choose TSV file to split into CSV files")
        split_source_layout.addWidget(self.split_source_edit)

        split_source_btn = QPushButton("📄 Browse")
        split_source_btn.setToolTip("Select TSV file")
        split_source_btn.clicked.connect(self.select_split_source)
        split_source_layout.addWidget(split_source_btn)

        split_layout.addLayout(split_source_layout)

        # Target directory selection
        split_target_layout = QHBoxLayout()
        split_target_label = QLabel("Target Dir:")
        split_target_label.setStyleSheet("font-weight: bold; color: #495057;")
        split_target_layout.addWidget(split_target_label)

        self.split_target_edit = QLineEdit()
        self.split_target_edit.setPlaceholderText("Select destination directory...")
        self.split_target_edit.setToolTip("Choose where to save the split CSV files")
        split_target_layout.addWidget(self.split_target_edit)

        split_target_btn = QPushButton("📂 Browse")
        split_target_btn.setToolTip("Select destination directory")
        split_target_btn.clicked.connect(self.select_split_target)
        split_target_layout.addWidget(split_target_btn)

        split_layout.addLayout(split_target_layout)

        split_btn = QPushButton("🔄 Split to CSV")
        split_btn.setToolTip("Start splitting TSV file to CSV files")
        split_btn.clicked.connect(self.split_tsv_to_csv)
        split_layout.addWidget(split_btn)

        split_group.setLayout(split_layout)
        layout.addWidget(split_group)

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

    def select_merge_source(self):
        """Select source directory containing CSV subdirectories for merging"""
        dir_path = QFileDialog.getExistingDirectory(self, "Select directory containing CSV subdirectories")
        if dir_path:
            self.merge_source_edit.setText(dir_path)

    def select_merge_target(self):
        """Select destination TSV file for merged output"""
        file_path, _ = QFileDialog.getSaveFileName(self, "Select destination TSV file", "", "TSV Files (*.tsv)")
        if file_path:
            self.merge_target_edit.setText(file_path)

    def select_split_source(self):
        """Select source TSV file for splitting"""
        file_path, _ = QFileDialog.getOpenFileName(self, "Select .TSV file", "", "TSV Files (*.tsv)")
        if file_path:
            self.split_source_edit.setText(file_path)

    def select_split_target(self):
        """Select destination directory for split CSV files"""
        dir_path = QFileDialog.getExistingDirectory(self, "Select destination directory for CSV directories")
        if dir_path:
            self.split_target_edit.setText(dir_path)

    # ============================================================================
    # Main Processing Methods
    # ============================================================================

    def merge_csv_to_tsv(self):
        """Merge CSV files from subdirectories into a single TSV file"""
        source = self.merge_source_edit.text()
        target = self.merge_target_edit.text()
        if not source or not target:
            QMessageBox.warning(self, "Warning", "Please select source directory and destination file")
            return

        self.progress_bar.setValue(0)
        self.worker = WorkerThread(self._merge_batch, source, target)
        self.worker.progress_signal.connect(self.update_progress)
        self.worker.finished_signal.connect(self.command_finished)
        self.worker.start()

    def split_tsv_to_csv(self):
        """Split TSV file into multiple CSV files organized by subdirectories"""
        source = self.split_source_edit.text()
        target = self.split_target_edit.text()
        if not source or not target:
            QMessageBox.warning(self, "Warning", "Please select TSV file and destination directory")
            return

        self.progress_bar.setValue(0)
        self.worker = WorkerThread(self._split_tsv, source, target)
        self.worker.progress_signal.connect(self.update_progress)
        self.worker.finished_signal.connect(self.command_finished)
        self.worker.start()

    # ============================================================================
    # Processing Implementation Methods
    # ============================================================================

    def _merge_batch(self, worker, source, target):
        """Merge multiple CSV files from subdirectories into a single TSV file"""
        worker.progress_signal.emit(15)  # Starting scan

        csv_dirs = self._scan_csv_directories(source)
        if not csv_dirs:
            return "No directories containing CSV files found"

        worker.progress_signal.emit(25)  # Scan complete, starting processing

        all_rows = []
        headers = None
        total_files = sum(len(csv_files) for _, _, csv_files in csv_dirs)
        processed_files = 0

        for dir_name, dir_path, csv_files in csv_dirs:
            for csv_file in csv_files:
                csv_path = os.path.join(dir_path, csv_file)
                with open(csv_path, 'r', encoding='utf-8-sig') as f:
                    reader = csv.reader(f)
                    file_rows = list(reader)
                    if file_rows:
                        if headers is None:
                            headers = file_rows[0] + ['metadata']
                            all_rows.append(headers)
                        # Add metadata to each row
                        metadata = f"{dir_name}/{csv_file}"
                        for row in file_rows[1:]:  # Skip header
                            all_rows.append(row + [metadata])

                processed_files += 1
                progress = 25 + int((processed_files / total_files) * 50)  # 25% to 75%
                worker.progress_signal.emit(progress)

        worker.progress_signal.emit(80)  # Processing complete, starting write

        if all_rows:
            escaped_rows = self._escape_line_breaks(all_rows)
            self._write_tsv_file(target, escaped_rows)

        worker.progress_signal.emit(95)  # Write complete
        return "Merge completed"

    # ============================================================================
    # Helper Methods
    # ============================================================================

    def _scan_csv_directories(self, source_dir):
        """Scan for directories containing CSV files"""
        csv_dirs = []
        for item in os.listdir(source_dir):
            item_path = os.path.join(source_dir, item)
            if os.path.isdir(item_path):
                csv_files = [f for f in os.listdir(item_path) if f.lower().endswith('.csv')]
                if csv_files:
                    csv_dirs.append((item, item_path, csv_files))
        return csv_dirs

    def _escape_line_breaks(self, rows):
        """Escape line breaks in CSV data for TSV compatibility"""
        escaped_rows = []
        for row in rows:
            escaped_row = []
            for cell in row:
                # Replace actual line breaks with \n
                escaped_cell = str(cell).replace('\n', '\\n').replace('\r', '')
                escaped_row.append(escaped_cell)
            escaped_rows.append(escaped_row)
        return escaped_rows

    def _write_tsv_file(self, target_path, rows):
        """Write rows to TSV file"""
        with open(target_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerows(rows)

    def _read_tsv_file(self, tsv_path):
        """Read TSV file and return rows"""
        with open(tsv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='\t')
            return list(reader)

    def _group_rows_by_metadata(self, rows, metadata_idx):
        """Group rows by metadata column"""
        grouped_data = {}
        for row in rows[1:]:  # Skip header
            metadata = row[metadata_idx]
            row_no_meta = row[:-1]  # Remove metadata
            # Unescape line breaks
            unescaped_row = []
            for cell in row_no_meta:
                unescaped_cell = cell.replace('\\n', '\n')
                unescaped_row.append(unescaped_cell)

            if metadata not in grouped_data:
                grouped_data[metadata] = []
            grouped_data[metadata].append(unescaped_row)
        return grouped_data

    def _write_grouped_csv_files(self, grouped_data, headers, target_dir, worker):
        """Write grouped data to CSV files organized by subdirectories"""
        total_groups = len(grouped_data)
        processed_groups = 0

        for metadata, data_rows in grouped_data.items():
            dir_name, file_name = metadata.split('/', 1)
            output_dir = os.path.join(target_dir, dir_name)
            os.makedirs(output_dir, exist_ok=True)

            csv_path = os.path.join(output_dir, file_name)
            with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(headers)
                writer.writerows(data_rows)

            processed_groups += 1
            progress = 80 + int((processed_groups / total_groups) * 15)  # 80% to 95%
            worker.progress_signal.emit(progress)

    def _split_tsv(self, worker, tsv_path, target_dir):
        """Split TSV file into multiple CSV files organized by subdirectories"""
        worker.progress_signal.emit(15)  # Starting read

        rows = self._read_tsv_file(tsv_path)
        if not rows:
            return "TSV file is empty"

        worker.progress_signal.emit(25)  # Read complete, starting validation

        headers = rows[0]
        if 'metadata' not in headers:
            return "TSV file does not have metadata column"

        metadata_idx = headers.index('metadata')
        headers_no_meta = headers[:-1]  # Remove metadata column

        worker.progress_signal.emit(35)  # Validation complete, starting grouping

        # Group rows by metadata
        grouped_data = self._group_rows_by_metadata(rows, metadata_idx)
        total_rows = len(rows) - 1  # Exclude header

        # Update progress during grouping
        processed_rows = 0
        for row in rows[1:]:  # Skip header
            processed_rows += 1
            progress = 35 + int((processed_rows / total_rows) * 40)  # 35% to 75%
            worker.progress_signal.emit(progress)

        worker.progress_signal.emit(80)  # Grouping complete, starting write

        # Create directories and files
        self._write_grouped_csv_files(grouped_data, headers_no_meta, target_dir, worker)

        worker.progress_signal.emit(95)  # Write complete
        return "Split completed"

    # ============================================================================
    # Progress and UI Update Methods
    # ============================================================================

    def update_progress(self, value):
        """Update progress bar value"""
        self.progress_bar.setValue(value)

    def command_finished(self, success, message):
        """Handle processing completion with user notification"""
        self.progress_bar.setValue(100)
        if success:
            QMessageBox.information(self, "Success", message)
        else:
            QMessageBox.critical(self, "Error", message)