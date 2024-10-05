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
        self.setWindowTitle("QTreeView - QStandardItemModel")

        self.model = QStandardItemModel(self)

        # 루트 아이템
        root_item = self.model.invisibleRootItem()  # 루트 아이템

        # 1단계 아이템 생성 
        africa_item =  QStandardItem("Africa")
        rwanda_item =  QStandardItem("Rwanda")
        musanze_item = QStandardItem("Musanze")
        kigali_item =  QStandardItem("Kigali")
        uganda_item =   QStandardItem("Uganda")
        kampala_item =  QStandardItem("Kampala")
        entebbe_item =  QStandardItem("Entebbe")
        asia_item =     QStandardItem("Asia")
        china_item =   QStandardItem("China")
        shanghai_item =  QStandardItem("Shanghai")
        beijing_item =   QStandardItem("Beijing")
        europe_item =  QStandardItem("Europe")
        france_item =  QStandardItem("France")
        paris_item =  QStandardItem("Paris")
        toulouse_item =   QStandardItem("Toulouse")

        # 2단계 트리 구조 정의 
        # Africa
        root_item.appendRow(africa_item)
        africa_item.appendRow(rwanda_item)
        africa_item.appendRow(uganda_item)

        rwanda_item.appendRow(musanze_item)
        rwanda_item.appendRow(kigali_item)

        uganda_item.appendRow(kampala_item)
        uganda_item.appendRow(entebbe_item)

        #Asia
        root_item.appendRow(asia_item)
        asia_item.appendRow(china_item)
        china_item.appendRow(beijing_item)
        china_item.appendRow(shanghai_item)

        #Europe
        root_item.appendRow(europe_item)
        europe_item.appendRow(france_item)
        france_item.appendRow(paris_item)
        france_item.appendRow(toulouse_item)

        # 트리뷰에 모델 설정
        self.treeView.setModel(self.model)
        self.treeView.expandAll()  # 모든 아이템 펼치기