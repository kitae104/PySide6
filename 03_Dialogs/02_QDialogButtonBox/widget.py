from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QDialog
from ui_widget import Ui_Widget
from infodialog import InfoDialog

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QDialog")

        self.btn_provide.clicked.connect(self.show_info_dialog)

        self.info_dialog = InfoDialog()

    def show_info_dialog(self):
        ret = self.info_dialog.exec() # QDialog.exec() 메서드는 사용자가 다이얼로그를 닫을 때까지 실행을 중단하고 사용자가 다이얼로그를 닫을 때까지 대기합니다.
        if(ret == QDialog.Accepted):
            self.lbl_info.setText(f"Position: {self.info_dialog.position}, Favorite OS: {self.info_dialog.favorite_os}")
        else:
            print("Dialog canceled")