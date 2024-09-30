import sys

from PySide6 import QtWidgets
from widget import Widget

app = QtWidgets.QApplication(sys.argv)
app.setStyle("Fusion")  # Fusion 스타일 적용

window = Widget()
window.show()

app.exec()