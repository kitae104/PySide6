from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtCore import Qt  # Import Qt


class Widget(QWidget, Ui_Widget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QTableWidget")

        # 시그널과 슬롯 연결
        self.btn_list_items.clicked.connect(self.list_items)
        self.btn_add_item.clicked.connect(self.add_item)

    # 슬롯
    def list_items(self):
        rows = self.tableWidget.rowCount()  # 행의 개수
        cols = self.tableWidget.columnCount()  # 열의 개수
        for r in range(rows):
            for c in range(cols):
                item = self.tableWidget.item(r, c)  # r행 c열의 아이템을 가져옴
                if item is not None:  # 아이템이 존재하면
                    data = item.data(
                        Qt.DisplayRole
                    )  # Qt.DisplayRole에 해당하는 데이터를 가져옴
                    print(data)
                else:
                    print("No Data")

    def add_item(self):
        in_str = self.lineEdit.text()
        if not (in_str == ""):
            self.tableWidget.insertRow(self.tableWidget.rowCount())  # 행 추가
            self.tableWidget.insertColumn(self.tableWidget.columnCount())
            self.tableWidget.setItem(
                self.tableWidget.rowCount() - 1,
                self.tableWidget.columnCount() - 1,
                QTableWidgetItem(in_str),
            )
        else:
            QMessageBox.warning(self, "Warning", "아이템을 입력하세요.")
