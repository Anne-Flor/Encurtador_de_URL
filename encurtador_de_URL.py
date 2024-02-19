from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFrame, QLineEdit, QPushButton
from PySide2.QtCore import QSize,Qt
import sys
import pyshorteners

class MainWindow(QmainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Short link")
        self.resize(400, 300)

        layout = QVBoxLayout()

        self.frame = QFrame()

        self.link = QLineEdit(self.frame)

        self.link.setPlaceholderText('Coloque o seu link aqui')
