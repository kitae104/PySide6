import sys
from PySide6.QtWidgets import QApplication
from widget import Widget

app = QApplication(sys.argv)
app.setStyle("Fusion")  # Fusion 스타일 적용

window = Widget()
window.show()

app.exec()
