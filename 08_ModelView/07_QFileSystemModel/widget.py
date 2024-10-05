from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QStringListModel
from PySide6.QtCore import QModelIndex
from PySide6.QtGui import QStandardItemModel
from PySide6.QtWidgets import QFileSystemModel
from PySide6.QtCore import Qt  # Import Qt
from PySide6.QtGui import QStandardItem  # Import QStandardItem
from PySide6.QtCore import QDir  # Import QDir

class Widget(QWidget, Ui_Widget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QFileSystemModel, ListView, TreeView")

        # QFileSystemModel 객체 생성         
        self.dir_model = QFileSystemModel(self) # QFileSystemModel 객체 생성
        self.dir_model.setFilter(QDir.Dirs | QDir.Files) # 디렉토리와 파일만 표시
        self.dir_model.setRootPath(QDir.currentPath()) # 현재 디렉토리를 루트로 설정

        self.treeView.setModel(self.dir_model)
        self.listView.setModel(self.dir_model) 
        

        #QStandardItemModel
        """ self.standard_model = QStandardItemModel() # QStandardItemModel 객체 생성
        parent_item = self.standard_model.invisibleRootItem() # 루트 아이템

        for i in range(4):
            item = QStandardItem(f"Item : {i}")
            parent_item.appendRow(item)
            parent_item = item

        self.treeView.setModel(self.standard_model)
        self.listView.setModel(self.standard_model) """

        self.btn_read_data.clicked.connect(self.read_data)  
        # self.btn_read_data.clicked.connect(self.read_data2)  

    def read_data(self):
        print("Row Count:", self.dir_model.rowCount(QModelIndex())) # 루트의 자식 수
        print("Column Count:", self.dir_model.columnCount(QModelIndex())) # 열 수
        index = self.dir_model.index(0, 0, QModelIndex()) # 첫 번째 행의 첫 번째 열
        data = index.data() # 데이터 읽기
        print("Data:", data)

    def read_data2(self):
        print("Row Count:", self.standard_model.rowCount(QModelIndex()))
        print("Column Count:", self.standard_model.columnCount(QModelIndex()))
        index = self.standard_model.index(0, 0, QModelIndex())  # 첫 번째 행의 첫 번째 열
        data = index.data() # 데이터 읽기
        print("Data:", data)