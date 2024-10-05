from typing import Any
from PySide6.QtCore import Qt
from PySide6.QtCore import QAbstractTableModel
from PySide6.QtCore import Qt, QTimer
from PySide6.QtCore import QTime
from PySide6.QtGui import QFont
from PySide6.QtGui import QBrush
from PySide6.QtGui import QColor
from PySide6.QtCore import QModelIndex


class MyTableModel(QAbstractTableModel):
    def __init__(self, *args, **kwargs):
        super(MyTableModel, self).__init__(*args, **kwargs)

        self.table = [
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "red"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "green"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "blue"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "yellow"],
        ]

    def data(self, index, role):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            return self.table[index.row()][index.column()]
        elif role == Qt.DecorationRole and index.column() == 6:
            return QColor(self.table[index.row()][index.column()])    

    def rowCount(self, index: QModelIndex):
        if(not(index.isValid())):   # 부모 인덱스가 유효하지 않다면
            return len(self.table)  # 테이블의 행 수 반환
        return 0

    def columnCount(self, index):
        if(not(index.isValid())):   # 부모 인덱스가 유효하지 않다면
            return len(self.table[0])   # 테이블의 열 수 반환        

    def columnCount(self,index) :
        if(not(index.isValid())):   # 부모 인덱스가 유효하지 않다면
            return len(self.table[0])  # 테이블의 열 수 반환

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole: # 수평 헤더
            if section == 0:
                return "First Name"
            if section == 1:
                return "Last Name"
            if section == 2:
                return "Age"
            if section == 3:
                return "Proffession"
            if section == 4:
                return "Marital Status"
            if section == 5:
                return "Country"
            if section == 6:
                return "Favorite Color"
        return super().headerData(section, orientation, role)
    
    def setData(self, index, value, role):
        if role != Qt.EditRole:
            return False
        self.table[index.row()][index.column()] = value
        self.dataChanged.emit(index, index)
        return True

    def flags(self, index):
        # 편집 가능, 활성화, 선택 가능 플래그 반환
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable 