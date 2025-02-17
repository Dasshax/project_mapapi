import sys
from data.map_image_func import get_map_image

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
from PyQt6.QtGui import QPixmap, QImage, QColor



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/main_form.ui')
        self.button_plus.clicked.connect(self.change_size, args=(0))
        self.coordinates = [0, 0]
        self.spn = [0, 0]


    def change_size(self, a):
        if not a:
            self.spn[0] += 0.01
            self.spn[0] += 0.01
        else:
            self.spn[0] -= 0.01
            self.spn[0] -= 0.01

    def change_coords(self):
        t = self.field_coord.text()
        x, y = tuple(map(float, t.split(',')))
        self.coordinates[0] = x
        self.coordinates[1] = y


    def show_map(self, image):
        self.pixmap = QPixmap(image)
        self.map_image.setPixmap(self.pixmap)


