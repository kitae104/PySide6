from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QStringListModel
from PySide6.QtCore import QModelIndex
from PySide6.QtCore import Qt  # Import Qt


class Widget(QWidget, Ui_Widget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QStringListModel-ListView")

        # 모델 설정 
        self.model = QStringListModel(self) # 모델 생성      
        list = ["AAA", "BBB", "CCC", "DDD", "EEE"]
        self.model.setStringList(list)  # 리스트 설정    

        self.listView.setModel(self.model)  # 모델 설정

        self.btn_show_data.clicked.connect(self.show_data)

    def show_data(self):
        """ 
        list = self.model.stringList()  # 리스트 가져오기
        for i in list:
            print(i) 
        """

        for i in range(self.model.rowCount(QModelIndex())): # 모델의 행 수만큼 반복
            index = self.model.index(i, 0, QModelIndex())   # 인덱스 생성
            data = self.model.data(index, Qt.DisplayRole) # 데이터 가져오기
            print(data)
            