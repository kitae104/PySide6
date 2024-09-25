from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_widget import Ui_frmWidget


class Widget(QWidget, Ui_frmWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 사용자 인터페이스에 있는 내용에 접근 가능 
        self.setWindowTitle("User data")
        self.btnSubmit.clicked.connect(self.submit)

    def submit(self):
        print(self.editFullName.text(), "is a", self.editOccupation.text())
