from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QPushButton, QLabel
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout
from PySide6.QtGui import QPixmap


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel Image")

        ########################################################
        # Widgets
        ########################################################
        image_label = QLabel()
        image_label.setPixmap(QPixmap("01_components/07_QLabel_Image/minions.png"))

                
        ########################################################
        # Layout
        ########################################################
        v_layout = QVBoxLayout()
        v_layout.addWidget(image_label)
        
        self.setLayout(v_layout)

    ########################################################
    # Slot
    ########################################################
    