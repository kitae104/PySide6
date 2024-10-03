from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget
from PySide6.QtWidgets import QFileDialog  
from PySide6.QtCore import QFile
from PySide6.QtCore import QDir  
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QFileInfo


class Widget(QWidget, Ui_Widget):

  def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.setWindowTitle("QDir Example")

    self.choose_dir_button.clicked.connect(self.choose_dir_button_clicked)
    self.create_dir_button.clicked.connect(self.create_dir_button_clicked)
    self.dir_exists_button.clicked.connect(self.dir_exists_button_clicked)
    self.dir_or_file_button.clicked.connect(self.dir_or_file_button_clicked)
    self.folder_content_button.clicked.connect(self.folder_content_button_clicked)

  def choose_dir_button_clicked(self):
    dir_name= QFileDialog.getExistingDirectory(self, "Choose Folder") # 폴더 선택 다이얼로그
    
    if((dir_name == "")):
      return
    
    print("file :",dir_name)
    
    self.lineEdit.setText(dir_name) # 선택한 폴더명을 LineEdit에 표시

  def create_dir_button_clicked(self):
    dir_name = self.lineEdit.text()  # LineEdit에 있는 폴더명 가져오기
    
    if(dir_name == ""):  # 폴더명이 없으면
      return  # 함수 종료
    
    dir = QFile(dir_name)  # QDir 객체 생성
    
    if(not dir.exists()):  # 폴더가 없으면
      dir.mkdir(dir_name)  # 폴더 생성
      QMessageBox.information(self, "Success", "Folder created")  # 메시지 박스 표시
    else:
      QMessageBox.information(self, "Fail", "Folder already exists")  # 이미 폴더가 있으면 메시지 박스 표시

  def dir_exists_button_clicked(self):
    dir_name = self.lineEdit.text()  # LineEdit에 있는 폴더명 가져오기
    
    if(dir_name == ""):  # 폴더명이 없으면
      return  # 함수 종료
    
    dir = QFile(dir_name)  # QDir 객체 생성
    
    if(dir.exists()):  # 폴더가 있으면
      QMessageBox.information(self, "Success", "Folder exists")  # 메시지 박스 표시
    else:
      QMessageBox.information(self, "Fail", "Folder does not exist")  # 폴더가 없으면 메시지 박스 표시

  def dir_or_file_button_clicked(self):
    file_info = QFileInfo(self.listWidget.currentItem().text())  # 선택한 파일 정보 가져오기

    if(file_info.isDir()):
      QMessageBox.information(self, "Type", "Folder")
    elif(file_info.isFile()):
      QMessageBox.information(self, "Type", "File")
    else:
      QMessageBox.information(self, "Type", "Something else")
    
  def folder_content_button_clicked(self):
    self.listWidget.clear()
    dir_path = self.lineEdit.text()
    if dir_path == "":
      return
    dir = QDir(dir_path)  # Use the QDir class
    file_list = dir.entryInfoList()
    for i in range(len(file_list)):
      file_info = QFileInfo(file_list[i])
      self.listWidget.addItem(file_info.absoluteFilePath())