from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Qt  # Import Qt
from PySide6.QtWidgets import QListWidgetItem  # Import QListWidgetItem


class Widget(QWidget, Ui_Widget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QListWidget")

        # 시그널과 슬롯 연결
        self.btn_list_items.clicked.connect(self.list_items)
        self.btn_add_item.clicked.connect(self.add_item)

    # 슬롯
    def list_items(self):
        for i in range(self.listWidget.count()):  # 리스트 위젯의 아이템 개수만큼 반복
            item = self.listWidget.item(i)  # i번째 아이템을 가져옴
            data = item.data(
                Qt.DisplayRole
            )  # Qt.DisplayRole에 해당하는 데이터를 가져옴
            print(data)

    def add_item(self):
        in_str = self.lineEdit.text()
        if not(in_str == ""):
            self.listWidget.addItem(QListWidgetItem(in_str))
        else:
            QMessageBox.warning(self, "Warning", "아이템을 입력하세요.")