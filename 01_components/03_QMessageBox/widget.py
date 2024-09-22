from PySide6.QtWidgets import QWidget, QPushButton
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QMessageBox


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox")

        ########################################################
        # Widgets
        ########################################################
        button_hard = QPushButton("Hard")
        button_hard.clicked.connect(self.button_clicked_hard)

        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.button_clicked_critical)

        button_question = QPushButton("Question")
        button_question.clicked.connect(self.button_clicked_question)

        button_information = QPushButton("Information")
        button_information.clicked.connect(self.button_clicked_information)

        button_warning = QPushButton("Warning")
        button_warning.clicked.connect(self.button_clicked_warning)

        button_about = QPushButton("About")
        button_about.clicked.connect(self.button_clicked_about)

        ########################################################
        # Layout
        ########################################################
        layout = QVBoxLayout()
        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)
        self.setLayout(layout)

    ########################################################
    # Slot - indent 확인!!
    ########################################################
    def button_clicked_hard(self):
        message = QMessageBox()  # 메시지 박스 생성
        message.setMinimumSize(700, 200)  # 최소 크기
        message.setWindowTitle("Message Title")  # 타이틀
        message.setText("Message Text")  # 메시지
        message.setInformativeText("Informative Text")  # 추가 정보
        message.setDetailedText("Detailed Text")  # 상세 정보
        message.setIcon(QMessageBox.Critical)  # 아이콘
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)  # 버튼
        message.setDefaultButton(QMessageBox.Cancel)  # 기본 버튼

        ret = message.exec()  # 메시지 박스 실행
        if ret == QMessageBox.Ok:
            print("Ok")
        else:
            print("Cancel")

    def button_clicked_critical(self):
        ret = QMessageBox.critical(
            self, "Critical", "Critical Message", QMessageBox.Ok | QMessageBox.Cancel
        )
        if ret == QMessageBox.Ok:
            print("Ok")
        else:
            print("Cancel")

    def button_clicked_question(self):
        ret = QMessageBox.question(
            self, "Question", "Question Message", QMessageBox.Ok | QMessageBox.Cancel
        )
        if ret == QMessageBox.Ok:
            print("Ok")
        else:
            print("Cancel")

    def button_clicked_information(self):
        ret = QMessageBox.information(
            self,
            "Information",
            "Information Message",
            QMessageBox.Ok | QMessageBox.Cancel,
        )
        if ret == QMessageBox.Ok:
            print("Ok")
        else:
            print("Cancel")

    def button_clicked_warning(self):
        ret = QMessageBox.warning(
            self, "Warning", "Warning Message", QMessageBox.Ok | QMessageBox.Cancel
        )
        if ret == QMessageBox.Ok:
            print("Ok")
        else:
            print("Cancel")

    def button_clicked_about(self):
        ret = QMessageBox.about(self, "About", "About Message")

        if ret == QMessageBox.Ok:
            print("Ok")
        else:
            print("Cancel")
