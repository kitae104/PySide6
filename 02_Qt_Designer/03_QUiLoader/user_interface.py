from PySide6 import QtCore, QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()  # QUiLoader 객체 생성

class UserInterface(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("02_Qt_Designer/03_QUiLoader/widget.ui", None)
        self.ui.setWindowTitle("New QUiLoader")
        self.ui.btnSubmit.clicked.connect(self.do_something)

    def show(self):
        self.ui.show()

    def do_something(self):
        print(self.ui.editFullName.text(), "is a", self.ui.editOccupation.text())