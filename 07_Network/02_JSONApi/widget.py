from PySide6.QtWidgets import QWidget
from PySide6.QtNetwork import QNetworkAccessManager
from PySide6.QtNetwork import QNetworkRequest  # Import QNetworkRequest
from PySide6.QtNetwork import QNetworkReply  # Import QNetworkReply
from PySide6.QtCore import QJsonDocument  # Import QJsonDocument
from PySide6.QtCore import QByteArray  # Import QByteArray
from PySide6.QtCore import QJsonArray  # Import QJsonArray
from ui_widget import Ui_Widget
from PySide6.QtCore import QUrl  # Import QUrl


class Widget(QWidget, Ui_Widget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("JSON API Demo")

        self.manager = QNetworkAccessManager(self)
        self.m_data_buffer = QByteArray()  # QByteArray 객체 생성
        self.request = QNetworkRequest()  # QNetworkRequest 객체 생성

        self.request.setUrl(
            QUrl("https://jsonplaceholder.typicode.com/posts")
        )  # 요청할 URL 설정

        self.btn_fetch.clicked.connect(self.btn_fetch_clicked)

    def btn_fetch_clicked(self):
        self.net_reply = self.manager.get(self.request)  # 요청 보내기
        self.net_reply.readyRead.connect(
            self.ready_read
        )  # 데이터를 읽을 수 있을 때 ready_read 함수 호출)
        self.net_reply.finished.connect(
            self.finished
        )  # 데이터 읽기가 끝나면 finished 함수 호출

    

    def ready_read(self):
      print("Some data available")
      self.m_data_buffer.append(
        self.net_reply.readAll()
      )  # 읽은 데이터를 m_data_buffer에 추가

    def finished(self):
      print("Data read finished")
      if self.net_reply.error() != QNetworkReply.NoError:  # 에러가 있으면
        print("Some error occured")
      else:  # 에러가 없으면
        doc = QJsonDocument.fromJson(self.m_data_buffer) # JSON 문서로 변환
        array = QJsonArray(doc.array()) # QJsonArray로 변환
        for i in range(array.count()): # 배열 크기만큼 반복
          obj = array.at(i).toObject()  # QJsonObject로 변환
          text = f"{[obj['id']]} : {obj['title']}"  # 텍스트 요소
          self.list_fetch.addItem(text) # 리스트에 추가
