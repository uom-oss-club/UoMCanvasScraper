from PySide6 import QtCore, QtWidgets
from utils.download_utils import get_files


class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.files)

    @QtCore.Slot()
    def add_items(self):
        self.files = get_files()
