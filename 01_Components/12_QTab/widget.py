from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QTabWidget, QPushButton, QLabel, QLineEdit
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTab")

        # 창 크기 조정
        self.resize(600, 300)

        ########################################################
        # Widgets
        ########################################################
        tab_widget = QTabWidget(self)

        widget_form = QWidget()
        label_full_name = QLabel("Full Name")
        self.line_edit_full_name = QLineEdit()
        button_submit = QPushButton("Submit")
        button_submit.clicked.connect(self.button_submit_clicked)

        widget_buttons = QWidget()
        button1 = QPushButton("One")
        button1.clicked.connect(self.button1_clicked)
        button2 = QPushButton("Two")
        button3 = QPushButton("Three")

        tab_widget.addTab(widget_form, "Information")
        tab_widget.addTab(widget_buttons, "Buttons")

        ########################################################
        # Layout
        ########################################################
        name_layout = QHBoxLayout()
        name_layout.addWidget(label_full_name)
        name_layout.addWidget(self.line_edit_full_name)
        form_layout = QVBoxLayout()
        form_layout.addLayout(name_layout)
        form_layout.addWidget(button_submit)
        widget_form.setLayout(form_layout)

        
        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(button1)
        buttons_layout.addWidget(button2)
        buttons_layout.addWidget(button3)
        widget_buttons.setLayout(buttons_layout)
        
        layout = QVBoxLayout()
        layout.addWidget(tab_widget)

        self.setLayout(layout)

    ########################################################
    # Slot
    ########################################################
    def button1_clicked(self):
        print("Button 1 Clicked")

    def button_submit_clicked(self):
        print("Submit Clicked")
        print("Full Name:", self.line_edit_full_name.text())