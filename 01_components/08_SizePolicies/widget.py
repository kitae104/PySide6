from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout
from PySide6.QtWidgets import QSizePolicy


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Size policies & stretches")
        self.setBaseSize(400, 200)

        ########################################################
        # Widgets
        ########################################################
        label = QLabel("Some text : ")
        line_edit = QLineEdit()
        line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed) # Expanding : 확장, Fixed : 고정
        # label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed) # 너비를 확장하고 높이를 고정

        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")

        ########################################################
        # Layout
        ########################################################
        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(line_edit)

        h_layout2 = QHBoxLayout()
        h_layout2.addWidget(button1, 2) # 2 : 2배로 늘어남
        h_layout2.addWidget(button2, 1) # 1 : 1배로 늘어남
        h_layout2.addWidget(button3, 1) # 1 : 1배로 늘어남    

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addLayout(h_layout2)

        self.setLayout(v_layout)

    ########################################################
    # Slot
    ########################################################
    