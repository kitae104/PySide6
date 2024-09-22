from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPushButton")

        ########################################################
        # Widgets
        ########################################################
        button = QPushButton("Click")
        button.clicked.connect(self.button_clicked)  # 클릭 시그널
        button.pressed.connect(self.button_pressed)  # 눌렀을 때 시그널
        button.released.connect(self.button_released)  # 뗐을 때 시그널

        ########################################################
        # Layout
        ########################################################
        layout = QVBoxLayout()
        layout.addWidget(button)

        self.setLayout(layout)

    ########################################################
    # Slot
    ########################################################
    def button_clicked(self):
        print("Clicked")

    def button_pressed(self):
        print("Pressed")

    def button_released(self):
        print("Released")
