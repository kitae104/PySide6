from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout

class RockWidget(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("첫번째 위젯")

    button1 = QPushButton("버튼1")                # 버튼 생성
    button1.clicked.connect(self.button1_clicked) # 버튼 클릭 시그널 연결

    button2 = QPushButton("버튼2")
    button2.clicked.connect(self.button2_clicked)

    # button_layout = QVBoxLayout()            # 버튼 레이아웃 생성
    button_layout = QHBoxLayout()            # 버튼 레이아웃 생성
    button_layout.addWidget(button1)       # 버튼 레이아웃에 버튼 추가
    button_layout.addWidget(button2)

    self.setLayout(button_layout)         # 위젯에 버튼 레이아웃 설정

  def button1_clicked(self):            # 버튼1 클릭 시그널 핸들러
    print("버튼1 클릭")

  def button2_clicked(self):
    print("버튼2 클릭")