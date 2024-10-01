import sys

from PySide6.QtWidgets import QApplication
from widget import Widget
from PySide6.QtGui import QColor, QPalette
from PySide6.QtCore import Qt

app = QApplication(sys.argv)
app.setStyle("Fusion")  # Fusion 스타일 적용

darkpalette = app.palette()  # 기본 팔레트 객체 생성

darkpalette.setColor(QPalette.Window, QColor(53, 53, 53))  # 배경색
darkpalette.setColor(QPalette.WindowText, Qt.white)  # 텍스트색
darkpalette.setColor(QPalette.Base, QColor(25, 25, 25))  # 베이스색
darkpalette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))  # 대체색
darkpalette.setColor(QPalette.ToolTipBase, Qt.white)  # 툴팁 베이스색
darkpalette.setColor(QPalette.ToolTipText, Qt.white)  # 툴팁 텍스트색
darkpalette.setColor(QPalette.Text, Qt.white)  # 텍스트색
darkpalette.setColor(QPalette.Button, QColor(53, 53, 53))  # 버튼색
darkpalette.setColor(QPalette.ButtonText, Qt.white)  # 버튼 텍스트색
darkpalette.setColor(QPalette.BrightText, Qt.red)  # 밝은 텍스트색
darkpalette.setColor(QPalette.Link, QColor(42, 130, 218))  # 링크색
darkpalette.setColor(QPalette.Highlight, QColor(42, 130, 218))  # 하이라이트색
darkpalette.setColor(QPalette.HighlightedText, Qt.black)  # 하이라이트 텍스트색

app.setPalette(darkpalette)  # 팔레트 적용

window = Widget()
window.show()

app.exec()
