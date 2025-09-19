import sys
import os
import webbrowser
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QMenuBar, QMenu, QMessageBox
from PyQt6.QtGui import QIcon, QAction

from MVGLTool import MVGLTool
from MBETool import MBETool
from TEXTTool import TEXTTool
from IMGTool import IMGTool
from CPKTool import CPKTool

def get_application_path():
    """
    Get the correct application path whether running as script or executable.

    Returns:
        str: Path to the application directory
    """
    if getattr(sys, 'frozen', False):
        # Running as PyInstaller executable
        return os.path.dirname(sys.executable)
    else:
        # Running as Python script
        return os.path.dirname(os.path.abspath(__file__))

def get_tools_path():
    """
    Get the correct Tools directory path.

    Returns:
        str: Path to the Tools directory
    """
    return os.path.join(get_application_path(), "Tools")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("DSTSTool GUI V2 Created by Levi")
        self.setGeometry(100, 100, 600, 400)
        self.setMinimumSize(600, 400)

        # Create menu bar
        self.create_menu_bar()

        # Set window icon using universal path method
        icon_path = os.path.join(get_application_path(), 'icon.ico')

        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
            # Set for QApplication as well
            if QApplication.instance():
                QApplication.instance().setWindowIcon(QIcon(icon_path))

        # Create tab widget
        self.tab_widget = QTabWidget()

        # Create tabs
        self.mvgl_tab = MVGLTool()
        self.mbe_tab = MBETool()
        self.text_tab = TEXTTool()
        self.img_tab = IMGTool()
        self.cpk_tab = CPKTool()

        # Add tabs to widget
        self.tab_widget.addTab(self.mvgl_tab, "MVGL Tools")
        self.tab_widget.addTab(self.cpk_tab, "CPK Tools")
        self.tab_widget.addTab(self.mbe_tab, "MBE Tools")
        self.tab_widget.addTab(self.img_tab, "IMG Tools")
        self.tab_widget.addTab(self.text_tab, "TEXT Tools")

        # Set central widget
        self.setCentralWidget(self.tab_widget)

    def create_menu_bar(self):
        """Create menu bar with Help menu"""
        menubar = self.menuBar()

        # Help menu
        help_menu = menubar.addMenu('Help')

        # README English
        readme_en_action = QAction('📖 README.md', self)
        readme_en_action.triggered.connect(self.open_readme_en)
        help_menu.addAction(readme_en_action)

        # Separator
        help_menu.addSeparator()

        # About
        about_action = QAction('ℹ️ About', self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def open_readme_en(self):
        """Open English README on GitHub"""
        try:
            webbrowser.open('https://github.com/levi-soft/DSTSTools-VN')
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Could not open GitHub README: {str(e)}")

    def open_readme_vi(self):
        """Open Vietnamese README on GitHub"""
        try:
            webbrowser.open('https://github.com/levi-soft/DSTSTools-VN/blob/main/README_VI.md')
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Không thể mở GitHub README: {str(e)}")

    def show_about(self):
        """Show about dialog"""
        about_text = """
        <h2>DSTSTool GUI v2</h2>
        <p><b>Created by:</b> Levi</p>
        <p><b>Version:</b> 2.0</p>
        <p><b>Description:</b> A comprehensive GUI tool for processing game files</p>
        <p><b>Supported formats:</b> CPK, MVGL, IMG, MBE, TEXT</p>
        <br>
        <p>This application is developed to support the game modding community.</p>
        """
        QMessageBox.about(self, "About DSTSTool GUI", about_text)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()