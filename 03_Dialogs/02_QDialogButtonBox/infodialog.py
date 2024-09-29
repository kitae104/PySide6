from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QDialogButtonBox
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
        self.button_box.clicked.connect(self.button_box_clicked)

    ############################
    # Slots
    ############################
    def button_box_clicked(self, button):
        std_button = self.button_box.standardButton(button) # QDialogButtonBox의 표준 버튼을 반환합니다.
        if(std_button == QDialogButtonBox.Ok):
            if(not(self.edit_position.text() == '')):
                self.position = self.edit_position.text()
            self.favorite_os = self.cmb_favorite.currentText()
            self.accept()
        elif(std_button == QDialogButtonBox.Cancel):
            self.reject()
        elif(std_button == QDialogButtonBox.Save):
            print("Save clicked")
        elif(std_button == QDialogButtonBox.Open):
            print("Open clicked")
        else:
            print("Unknown button clicked")