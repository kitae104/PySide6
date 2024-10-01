import sys

from PySide6.QtWidgets import QApplication
from widget import Widget
from PySide6.QtGui import QColor, QPalette
from PySide6.QtCore import Qt

app = QApplication(sys.argv)

# 전체적으로 스타일 적용
# app.setStyle("Fusion")  # Fusion 스타일 적용
# app.setStyleSheet("QPushButton { background-color: white; color: red; }")

# 외부 스타일시트 파일 적용
with open("04_Styling/04_Stylesheets/styles/style.css", 'r') as f:
    app.setStyleSheet(f.read())


window = Widget()
window.show()

app.exec()
