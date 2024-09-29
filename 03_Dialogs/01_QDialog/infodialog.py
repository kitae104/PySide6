from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
from ui_infodialog import Ui_InfoDialog

class InfoDialog(QDialog, Ui_InfoDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Info Dialog")
        
        # 필드
        self.position = ''
        self.favorite_os = ''

        # 이벤트 핸들러 연결
        self.btn_ok.clicked.connect(self.ok)
        self.btn_cancel.clicked.connect(self.cancel)

    def ok(self):
        if(not(self.edit_position.text() == '')):
            self.position = self.edit_position.text()
        self.favorite_os = self.cmb_favorite.currentText()
        self.accept()

    def cancel(self):
        self.reject()