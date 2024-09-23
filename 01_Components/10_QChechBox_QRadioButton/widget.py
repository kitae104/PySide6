from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QGroupBox, QCheckBox, QRadioButton
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
from PySide6.QtWidgets import QButtonGroup


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCheckBox and QRadioButton")
        
        # 창 크기 조정
        self.resize(600, 400)

        ########################################################
        # Widgets
        ########################################################
        os = QGroupBox("Choose operating system")
        windows = QCheckBox("Windows")
        windows.toggled.connect(self.windows_box_toggled)

        linux = QCheckBox("Linux")
        linux.toggled.connect(self.linux_box_toggled)

        mac = QCheckBox("Mac")
        mac.toggled.connect(self.mac_box_toggled)

        drinks = QGroupBox("Choose your drink")
        beer = QCheckBox("Beer")
        beer.setChecked(True)
        wine = QCheckBox("Wine")
        whiskey = QCheckBox("Whiskey")
        coffee = QCheckBox("Coffee")

        # 한번에 하나만 선택할 수 있게 하는 버튼 그룹
        exclusive_button_group = QButtonGroup(self) # self는 부모 위젯을 의미
        exclusive_button_group.addButton(beer)
        exclusive_button_group.addButton(wine)
        exclusive_button_group.addButton(whiskey)
        exclusive_button_group.addButton(coffee) 
        exclusive_button_group.setExclusive(True) # 한번에 하나만 선택할 수 있게 설정

        answers = QGroupBox("Choose answer")
        answer1 = QRadioButton("A")
        answer2 = QRadioButton("B")
        answer3 = QRadioButton("C")
        answer1.setChecked(True)

        ########################################################
        # Layout
        ########################################################
        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)

        os.setLayout(os_layout)

        drinks_layout = QVBoxLayout()
        drinks_layout.addWidget(beer)
        drinks_layout.addWidget(wine)
        drinks_layout.addWidget(whiskey)
        drinks_layout.addWidget(coffee)
        drinks.setLayout(drinks_layout)

        answers_layout = QVBoxLayout()
        answers_layout.addWidget(answer1)
        answers_layout.addWidget(answer2)
        answers_layout.addWidget(answer3)
        answers.setLayout(answers_layout)

        h_layout = QHBoxLayout()
        h_layout.addWidget(os)
        h_layout.addWidget(drinks)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(answers)

        self.setLayout(v_layout)

    ########################################################
    # Slot
    ########################################################
    def windows_box_toggled(self, checked):
        if checked:
            print("Windows is checked")
        else:
            print("Windows is unchecked")

    def linux_box_toggled(self, checked):
        if checked:
            print("Linux is checked")
        else:
            print("Linux is unchecked")

    def mac_box_toggled(self, checked):
        if checked:
            print("Mac is checked")
        else:
            print("Mac is unchecked")
