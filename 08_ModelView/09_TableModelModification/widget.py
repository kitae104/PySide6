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
from tablemodel import MyTableModel


class Widget(QWidget, Ui_Widget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Custom Table Model")

        self.model = MyTableModel()
        self.tableView.setModel(self.model)
