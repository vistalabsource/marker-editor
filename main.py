import sys
from PySide6.QtWidgets import QApplication

from src.windowlogic import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Marker")
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
