from PySide6.QtWidgets import QApplication
import sys
from widget import Widget

app = QApplication(sys.argv)

windows = Widget()
windows.show()

sys.exit(app.exec()) # 이벤트 루프 시작