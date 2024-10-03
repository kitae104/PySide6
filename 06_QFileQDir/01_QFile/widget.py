from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget
from PySide6.QtWidgets import QFileDialog  
from PySide6.QtCore import QFile
from PySide6.QtCore import QIODevice
from PySide6.QtCore import QTextStream  
from PySide6.QtWidgets import QMessageBox

class Widget(QWidget, Ui_Widget):

  def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.setWindowTitle("QFile Example")

    self.btn_write.clicked.connect(self.btn_write_clicked)
    self.btn_read.clicked.connect(self.btn_read_clicked)
    self.btn_select.clicked.connect(self.btn_select_clicked)
    self.btn_copy.clicked.connect(self.btn_copy_clicked)

  def btn_write_clicked(self):
    file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", 
      "Text(*.txt);;Images (*.png *.xpm *.jpg);;All files(*.*)")
    
    if file_name == "":
      return
    print("file : ", file_name) 
    
    file = QFile(file_name) # QFile 객체 생성
    
    if(not file.open(QIODevice.WriteOnly | QIODevice.Text)):  # 파일 열기 실패시 
      return
    
    out = QTextStream(file)   # 텍스트스트림 생성
    out << self.ta_text.toPlainText() << "\n" # 텍스트 내용 저장
    
    file.close()  # 파일 닫기

  def btn_read_clicked(self):
    file_content = ""  # 파일 내용 저장할 변수
    file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", 
      "Text(*.txt);;Images (*.png *.xpm *.jpg);;All files(*.*)")
    
    if file_name == "": # 파일 선택 안하면
      return  # 함수 종료
    print("file : ", file_name)   
    
    file = QFile(file_name) # QFile 객체 생성
    
    if(not file.open(QIODevice.ReadOnly | QIODevice.Text)):  # 파일 열기 실패시 
      return
    
    in_stream = QTextStream(file)   # 텍스트스트림 생성
    
    while not in_stream.atEnd():  # 파일 끝까지 읽기
      line = in_stream.readLine() # 한 줄 읽기
      file_content = file_content + line + '\n'  # 파일 내용에 추가      
    file.close()  # 파일 닫기

    self.ta_text.clear()  # 텍스트 영역 초기화
    self.ta_text.setPlainText(file_content)  # 텍스트 영역에 파일 내용 출력    

  def btn_select_clicked(self):
    file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", 
      "Text(*.txt);;Images (*.png *.xpm *.jpg);;All files(*.*)")
    
    if file_name == "":
      return
    
    self.tf_select_file.setText(file_name)  # 파일 경로 표시

  def btn_copy_clicked(self):
    src = self.tf_select_file.text()  # 복사할 파일 경로
    dst = self.tf_copy.text()  # 복사될 파일 경로

    if src == "" or dst == "":
      QMessageBox.information(self, "Warning", "파일을 먼저 선택해 주세요.")
      return

    file = QFile(src)  # QFile 객체 생성
    if(file.copy(dst)):
      QMessageBox.information(self, "Success", "File Copy Success")
    else:
      QMessageBox.critical(self, "Error", "File Copy Error")