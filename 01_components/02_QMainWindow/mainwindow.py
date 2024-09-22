from PySide6.QtWidgets import QMainWindow, QToolBar
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QStatusBar


class MainWindow(QMainWindow):
    def __init__(self, app):  # 생성자
        super().__init__()  # 부모 클래스의 생성
        self.app = app  # app 객체를 저장
        self.setWindowTitle("My App")

        # app 크기 설정
        self.resize(600, 400)

        ###################################
        # 메뉴바와 메뉴 생성
        ###################################
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)  # 종료 이벤트 연결

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        menu_bar.addMenu("View")
        menu_bar.addMenu("Window")
        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")

        ###################################
        # 툴 바 생성
        ###################################
        toolbar = QToolBar("My Tool Bar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        toolbar.addAction(quit_action)

        ###################################
        # 툴 바 버튼 생성
        ###################################
        action1 = QAction("Some Action", self)
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2 = QAction(
            QIcon("01_components/02_QMainWindow/start.png"), "Another Action", self
        )
        action2.setStatusTip("Status message for some other action")
        action2.triggered.connect(self.toolbar_button_click)  # 클릭 이벤트 연결
        # action2.setCheckable(True)
        toolbar.addAction(action2)  # 툴바에 액션 추가

        toolbar.addSeparator()  # 구분선 추가
        toolbar.addWidget(QPushButton("Click here"))  # 버튼 추가

        ###################################
        # 상태 바 버튼 생성
        ###################################
        self.setStatusBar(QStatusBar(self))  # 상태바 생성

        button1 = QPushButton("BUTTON1", self)
        button1.clicked.connect(self.button1_click)
        self.setCentralWidget(button1)

    def quit_app(self):
        self.app.quit()  # 어플리케이션 종료

    def toolbar_button_click(self):
        self.statusBar().showMessage("Message from my app", 3000)   # 상태바에 메시지 표시

    def button1_click(self):
        print("Button 1 clicked")