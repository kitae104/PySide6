from PySide6.QtWidgets import QApplication, QWidget
import sys
from rockwidget import RockWidget

app = QApplication(sys.argv)

windows = RockWidget()
windows.show()

sys.exit(app.exec()) # 이벤트 루프 시작