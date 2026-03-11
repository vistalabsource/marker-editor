import markdown
from PySide6.QtWidgets import QMainWindow

from ui.mainwindow import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.input_md.textChanged.connect(self._update_preview)
        
    def _update_preview(self):
        text = self.input_md.toPlainText()
        html = markdown.markdown(text, extensions=['extra', 'nl2br'])
        self.preview_md.setHtml(html)
