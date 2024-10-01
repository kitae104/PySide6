from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from ui_widget import Ui_Widget
from PySide6.QtWidgets import QDialog
from infodialog import InfoDialog


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Stylesheet Example")
        self.provide_info_button.clicked.connect(self.provide_info)

        self.info_dialog = InfoDialog()

    def provide_info(self):
        ret = self.info_dialog.exec()
        if(ret == QDialog.Accepted):
            self.info_label.setText("Your position is " + self.info_dialog.position +
                                 " and your favorite os is " + self.info_dialog.favorite_os)
        else:
            self.info_label.setText("Rejected")

        
