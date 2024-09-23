from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QListWidget, QPushButton
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QAbstractItemView


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QList")

        # 창 크기 조정
        self.resize(400, 600)

        ########################################################
        # Widgets
        ########################################################
        self.list = QListWidget()
        self.list.setSelectionMode(QAbstractItemView.MultiSelection)  # 다중 선택 가능
        self.list.addItem("One") # 리스트에 아이템 추가
        self.list.addItems(["Two", "Three"]) # 리스트에 여러 아이템 추가
        self.list.currentItemChanged.connect(self.current_item_changed) # 현재 아이템이 바뀌면 current_item_changed 함수 호출
        self.list.currentTextChanged.connect(self.current_text_changed) # 현재 아이템의 텍스트가 바뀌면 current_text_changed 함수 호출

        button_add_item = QPushButton("Add Item") 
        button_add_item.clicked.connect(self.addItem) # 버튼을 클릭하면 addItem 함수 호출

        button_remove_item = QPushButton("Remove Item")
        button_remove_item.clicked.connect(self.removeItem)

        button_item_count = QPushButton("Item Count")
        button_item_count.clicked.connect(self.itemCount)

        button_selected_items = QPushButton("Selected Items")
        button_selected_items.clicked.connect(self.selectedItems)

        ########################################################
        # Layout
        ########################################################
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.list)
        v_layout.addWidget(button_add_item)
        v_layout.addWidget(button_remove_item)
        v_layout.addWidget(button_item_count)
        v_layout.addWidget(button_selected_items)

        self.setLayout(v_layout)

    ########################################################
    # Slot
    ########################################################
    def current_item_changed(self, item):        
        print("Current item : ", item.text())

    def current_text_changed(self, text):
        print("Current text changed : ", text)

    def addItem(self):
        self.list.addItem("New Item")

    def removeItem(self):
        self.list.takeItem(self.list.currentRow())  # 현재 선택된 아이템 삭제

    def itemCount(self):
        print("Item count : ", self.list.count()) # 리스트에 있는 아이템 개수 출력

    def selectedItems(self):
        items = self.list.selectedItems()
        for item in items:
            print("Selected item : ", item.text())