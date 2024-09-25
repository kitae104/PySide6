from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from ui_widget import Ui_Widget
import resource_rc

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Widget")
        self.spin_box.setValue(50)
        self.btn_plus.clicked.connect(self.plus)
        self.btn_minus.clicked.connect(self.minus)

        plus_icon = QIcon(':/images/plus.png')
        minus_icon = QIcon(':/images/minus.png')

        self.btn_plus.setIcon(plus_icon)
        self.btn_minus.setIcon(minus_icon)

    def plus(self):
        value = self.spin_box.value()
        self.spin_box.setValue(value + 1)

    def minus(self):
        value = self.spin_box.value()
        self.spin_box.setValue(value - 1)

    

