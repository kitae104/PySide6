from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QDialog, QFileDialog, QFontDialog, QColorDialog, QInputDialog
from ui_widget import Ui_Widget
from PySide6.QtGui import QFont
from PySide6.QtGui import QPalette


class Widget(QWidget, Ui_Widget):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.setWindowTitle("CommonDialog")

    self.btn_file_dialog.clicked.connect(self.show_file_dialog)
    self.btn_font_dialog.clicked.connect(self.show_font_dialog) 
    self.btn_color.clicked.connect(self.show_color_dialog)
    self.btn_background.clicked.connect(self.show_background_dialog)
    self.btn_str_input.clicked.connect(self.show_str_input_dialog)
    self.btn_int_input.clicked.connect(self.show_int_input_dialog)
    self.btn_item_input.clicked.connect(self.show_item_input_dialog)

  def show_str_input_dialog(self):
    text, ok = QInputDialog.getText(self, "Input Dialog", "Enter your name:")
    if (ok and not(text == "")):
      self.lbl_font.setText(text)

  def show_int_input_dialog(self):
    value, ok = QInputDialog.getInt(self, "Get int", "Select a value : ",150,100,200) # (부모, 제목, 메시지, 기본값, 최소값, 최대값)
    if (ok) :
        self.lbl_font.setText(f'{value}')

  def show_item_input_dialog(self):
    items =  ["Spring","Summer","Fall","Winter"]
    item, ok = QInputDialog.getItem(self, "Get item", "Season:", items, 0, False) # (부모, 제목, 메시지, 아이템, 기본값, 수정가능여부)
    if ok and item:
        self.lbl_font.setText(item)

  def show_color_dialog(self):
    palette = self.lbl_font.palette() # 현재 팔레트 반환
    color = palette.color(QPalette.WindowText)  # 현재 텍스트 색상
    chosenColor = QColorDialog.getColor(color, self, "Choose text color") # 색상 대화상자

    if chosenColor.isValid():
      palette.setColor(QPalette.WindowText, chosenColor)
      self.lbl_font.setPalette(palette)
    else:
      print("Color dialog canceled")

  def show_background_dialog(self):
    palette = self.lbl_font.palette()
    color = palette.color(QPalette.Window)
    chosenColor = QColorDialog.getColor(color,self,"Choose background color")

    if(chosenColor.isValid()):
        palette.setColor(QPalette.Window,chosenColor)
        self.lbl_font.setPalette(palette)
        self.lbl_font.setAutoFillBackground(True)  # 배경을 채우도록 설정
    else:
        print("User chose a bad background color")


  def show_font_dialog(self):
    ok, font = QFontDialog.getFont(QFont("Helvetica [Cronyx]", 20),self) # 선택한 폰트 반환
    if ok:
      self.lbl_font.setFont(font)
      print(f"Font: {font}")
    else:
      print("Font dialog canceled")


  def show_file_dialog(self):
    # 기존 디렉토리 선택 대화상자
    # dir = QFileDialog.getExistingDirectory(self, "Select Directory", "C:/Temp", 
    #                 QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
    # print(f"Selected directory: {dir}")

    # 파일 선택 대화상자
    # file_names, _ = QFileDialog.getOpenFileNames(self, "Select Files", "C:/Temp",
    #                 "All Files (*);;Python Files (*.py)")
    # for f in file_names:
    #   print(f"file: {f}")

    # 파일 저장 대화상자
    file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "C:/Temp", 
                    "All Files (*);;Python Files (*.py)")
    print(f"file: {file_name}")
