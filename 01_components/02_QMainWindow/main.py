from PySide6.QtWidgets import QApplication
import sys
from mainwindow import MainWindow

app = QApplication(sys.argv)

windows = MainWindow(app)
windows.show()

app.exec() # 이벤트 루프 시작