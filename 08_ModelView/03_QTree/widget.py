from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QTreeWidgetItem
from PySide6.QtCore import Qt  # Import Qt


class Widget(QWidget, Ui_Widget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QTreeWidget")

        self.treeWidget.setColumnCount(2)   # 2개의 컬럼 생성

        # 헤더 설정
        self.treeWidget.setHeaderLabels(["ID", "Name"])

        # 트리 아이템 추가
        treeItem1 = QTreeWidgetItem(self.treeWidget)    # 최상위 아이템
        treeItem1.setText(0, "11")
        treeItem1.setText(1, "Snow")

        treeItem2 = QTreeWidgetItem(self.treeWidget)    # 최상위 아이템
        treeItem2.setText(0, "22")
        treeItem2.setText(1, "David")

        treeItem3 = QTreeWidgetItem(treeItem1)          # treeItem1의 자식 아이템
        treeItem3.setText(0, "33")
        treeItem3.setText(1, "John")

        treeItem4 = QTreeWidgetItem()                 # 최상위 아이템
        treeItem4.setText(0, "44")
        treeItem4.setText(1, "Jane")

        treeItem5 = QTreeWidgetItem(treeItem4)         # treeItem4의 자식 아이템
        treeItem5.setText(0, "55")
        treeItem5.setText(1, "Tom")

        treeItem2.addChild(treeItem4)                 # treeItem2의 자식 아이템으로 추가

        # 시그널 슬롯 연결
        self.pushButton.clicked.connect(self.list_items)

    def list_items(self):
        top_level_item_count = self.treeWidget.topLevelItemCount()
        for i in range(top_level_item_count):
            item = self.treeWidget.topLevelItem(i)
            if(item is not None):
                print(f"ID :  {item.data(0, Qt.DisplayRole)}, | Name : {item.data(1, Qt.DisplayRole)}")
                child_count = item.childCount()
                for c in range(child_count):
                    child = item.child(c)
                    print(f"ID :  {child.data(0, Qt.DisplayRole)}, | Name : {child.data(1, Qt.DisplayRole)}")