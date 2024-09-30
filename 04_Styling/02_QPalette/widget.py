from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from ui_widget import Ui_Widget


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QPalette Example")

        palette = QPalette() # 팔레트 객체 생성

        palette.setColor(QPalette.Window, Qt.blue)  # 배경색
        palette.setColor(QPalette.WindowText, Qt.red) # 텍스트색

        self.the_sky_label.setAutoFillBackground(True)  # 배경색 전체 적용
        self.the_sky_label.setPalette(palette)  # 팔레트 적용

        self.blue_label.setAutoFillBackground(True)
        self.blue_label.setPalette(self.the_sky_label.palette())

