import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()  # QUiLoader 객체 생성

app = QtWidgets.QApplication(sys.argv)  # QApplication 객체 생성
window = loader.load("02_Qt_Designer/03_QUiLoader/widget.ui", None)  # ui 파일 로드


def do_something():
    print(window.editFullName.text(), "is a", window.editOccupation.text())

window.setWindowTitle("QUiLoader")

window.btnSubmit.clicked.connect(do_something)  # 버튼 클릭 시 do_something 함수 호출
window.show()  # 창 보이기
app.exec()  # 이벤트 루프 실행