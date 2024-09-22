from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel & QLineEdit")

        ########################################################
        # Widgets
        ########################################################
        label = QLabel("Fullname : ")
        self.line_edit = QLineEdit()
        # self.line_edit.textChanged.connect(self.text_changed)  # 텍스트 변경 시그널
        # self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed)
        self.line_edit.returnPressed.connect(self.return_pressed)
        #self.line_edit.selectionChanged.connect(self.selection_changed)

        button = QPushButton("Grab data")
        button.clicked.connect(self.button_clicked)  # 클릭 시그널
        self.text_holder_label = QLabel("I AM HERE")

        ########################################################
        # Layout
        ########################################################
        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)

        self.setLayout(v_layout)

    ########################################################
    # Slot
    ########################################################
    def button_clicked(self):
        self.text_holder_label.setText(self.line_edit.text()) # 텍스트 설정

    def text_changed(self):
        self.text_holder_label.setText(self.line_edit.text()) # 텍스트 설정

    def cursor_position_changed(self):
        self.text_holder_label.setText(str(self.line_edit.cursorPosition())) # 커서 위치 설정

    def return_pressed(self):
        self.text_holder_label.setText(self.line_edit.text()) # 텍스트 설정
