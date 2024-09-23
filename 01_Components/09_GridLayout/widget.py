from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QGridLayout
from PySide6.QtWidgets import QSizePolicy


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout")
        # 창 크기 조정
        self.resize(400, 100)

        ########################################################
        # Widgets
        ########################################################
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")
        button3.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        button4 = QPushButton("Button 4")
        button5 = QPushButton("Button 5")
        button6 = QPushButton("Button 6")
        button7 = QPushButton("Button 7")

        ########################################################
        # Layout
        ########################################################
        grid_layout = QGridLayout()
        grid_layout.addWidget(button1, 0, 0)
        grid_layout.addWidget(button2, 0, 1, 1, 2) # 1행 2열 차지
        grid_layout.addWidget(button3, 1, 0, 2, 1) # 2행 1열 차지
        grid_layout.addWidget(button4, 1, 1)
        grid_layout.addWidget(button5, 1, 2)
        grid_layout.addWidget(button6, 2, 1)
        grid_layout.addWidget(button7, 2, 2)

        self.setLayout(grid_layout)
    ########################################################
    # Slot
    ########################################################
    