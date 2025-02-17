import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
from PyQt6.QtGui import QPixmap, QImage, QColor



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/main_form.ui')
        self.button_plus.clicked.connect(self.change_size, args=(0))

    def change_size(self):



