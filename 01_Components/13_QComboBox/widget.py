from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QComboBox, QPushButton
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox")

        # 창 크기 조정
        self.resize(400, 150)

        ########################################################
        # Widgets
        ########################################################
        self.combo_box = QComboBox(self)
        self.combo_box.addItem("Earth")
        self.combo_box.addItem("Mars")
        self.combo_box.addItem("Jupiter")
        self.combo_box.addItem("Saturn")
        self.combo_box.addItem("Uranus")
        self.combo_box.addItem("Neptune")

        button_current_value = QPushButton("Current Value")
        button_current_value.clicked.connect(self.current_value)

        button_set_current = QPushButton("Set Value")
        button_set_current.clicked.connect(self.set_current)

        button_get_values = QPushButton("Get Values")
        button_get_values.clicked.connect(self.get_values)

        ########################################################
        # Layout
        ########################################################
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.combo_box)
        v_layout.addWidget(button_current_value)
        v_layout.addWidget(button_set_current)
        v_layout.addWidget(button_get_values)        

        self.setLayout(v_layout)

    ########################################################
    # Slot
    ########################################################
    def current_value(self):
        print("Current Item : ", self.combo_box.currentText(), 
              " - Current Index : ", self.combo_box.currentIndex())

    def set_current(self):
        self.combo_box.setCurrentIndex(2)

    def get_values(self):
        for i in range(self.combo_box.count()):
            print(f"index[{i}] : {self.combo_box.itemText(i)}")