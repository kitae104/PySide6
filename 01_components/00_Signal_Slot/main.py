import sys
from PySide6.QtWidgets import QApplication, QPushButton, QSlider
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QWidget


def button_clicked():
    print("You clicked the button")


def respond_to_slider(value):
    print(f"Slider value: {value}")


app = QApplication(sys.argv)
window = QWidget()  # 레이아웃을 설정할 위젯 생성

button = QPushButton("Click me")
button.clicked.connect(button_clicked)


slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)
slider.valueChanged.connect(respond_to_slider)

layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(slider)
window.setLayout(layout)
window.show()


sys.exit(app.exec())  # 이벤트 루프 시작
