from typing import Any
from PySide6.QtCore import Qt
from PySide6.QtCore import QAbstractTableModel
from PySide6.QtCore import Qt, QTimer
from PySide6.QtCore import QTime
from PySide6.QtGui import QFont
from PySide6.QtGui import QBrush


class MyTableModel(QAbstractTableModel):
    def __init__(self, *args, **kwargs):
        super(MyTableModel, self).__init__(*args, **kwargs)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_timeout)
        self.timer.start()
        
    def data(self, index, role):
                row = index.row()
                col = index.column()

                if role == Qt.DisplayRole:
                    if(row == 0 and col == 1):
                        return "<-- left"
                    if(row == 1 and col == 1):
                        return "right -->"
                    if(row == 0 and col == 0):
                        return QTime.currentTime().toString()
                    value = " [ Row : " + str(index.row() + 1) + ", Column : " + str(index.column() + 1) +"]"
                    return value
                
                if role == Qt.FontRole:
                    if row == 0:
                        font = QFont()
                        font.setBold(True)
                        return font

                if role == Qt.BackgroundRole:
                    if(row == 0 and col == 0):
                        background = QBrush(Qt.yellow)
                        return background
                    
                if role == Qt.TextAlignmentRole:
                    if row == 1 and col == 1:
                        return Qt.AlignRight

    def timer_timeout(self):
        top_left = self.index(0,0)  # Top left 인덱스
        self.dataChanged.emit(top_left, top_left) # 데이터 변경 이벤트 발생

    def rowCount(self, parent):
        return 2
    
    def columnCount(self, parent):
        return 4

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        if role == Qt.DisplayRole:
            if(orientation == Qt.Horizontal):   # 수평 헤더
                if(section == 0):
                    return "First"
                if(section == 1):
                    return "Second"
                if(section == 2):   
                    return "Third"               
                if(section == 3):   
                    return "Fourth"
        return super().headerData(section, orientation, role)   # 헤더 데이터 반환