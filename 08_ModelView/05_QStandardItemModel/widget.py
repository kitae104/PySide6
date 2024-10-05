from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QStringListModel
from PySide6.QtCore import QModelIndex
from PySide6.QtGui import QStandardItemModel
from PySide6.QtCore import Qt  # Import Qt
from PySide6.QtGui import QStandardItem  # Import QStandardItem

class Widget(QWidget, Ui_Widget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QTableView - QStandardItemModel")

        # 모델 설정
        self.model = QStandardItemModel(4, 4, self)  # 모델 생성
        for r in range(self.model.rowCount()):
            for c in range(self.model.columnCount()):
                item = QStandardItem(f"({r}, {c})")
                self.model.setItem(r, c, item)

        self.tableView.setModel(self.model)  # 모델 설정

        # 시그널-슬롯 연결
        self.btn_read_data.clicked.connect(self.read_data)

    # 슬롯 메서드
    def read_data(self):
        for r in range(self.model.rowCount()): # 행 순회
            for c in range(self.model.columnCount()): # 열 순회
                index = self.model.index(r, c, QModelIndex()) # 인덱스 생성
                item = self.model.data(index, Qt.DisplayRole) # 데이터 읽기
                print(item)
