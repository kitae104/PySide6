from PySide6.QtWidgets import QWidget
from PySide6.QtNetwork import QNetworkAccessManager
from PySide6.QtNetwork import QNetworkRequest  # Import QNetworkRequest
from PySide6.QtNetwork import QNetworkReply  # Import QNetworkReply
from PySide6.QtCore import QByteArray  # Import QByteArray
from ui_widget import Ui_Widget
from PySide6.QtCore import QUrl  # Import QUrl
import requests
from bs4 import BeautifulSoup

class Widget(QWidget, Ui_Widget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QNetworkAccessManager")

        self.manager = QNetworkAccessManager(self)
        self.m_data_buffer = QByteArray()  # QByteArray 객체 생성
        self.request = QNetworkRequest()  # QNetworkRequest 객체 생성

        self.request.setUrl(QUrl("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%9D%B8%ED%95%98%EA%B3%B5%EC%A0%84"))  # 요청할 URL 설정

        self.net_reply = self.manager.get(self.request)  # 요청 보내기

        self.net_reply.readyRead.connect(
            self.ready_read
        )  # 데이터를 읽을 수 있을 때 ready_read 함수 호출
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
        if self.net_reply.error()!= QNetworkReply.NoError:  # 에러가 있으면
            print("Error")  # 에러 메시지 출력
        else:
            html = str(self.m_data_buffer, 'utf-8')
            soup = BeautifulSoup(html, 'html.parser')
            links = soup.select('.news_tit')          # 결과는 리스트 
            news = ""
            for i, link in enumerate(links):
                title = link.text         # 텍스트 요소 
                url = link.attrs['href']  # 속성값 
                news = news + f"{i+1} : {title}, {url}\n"

            self.textEdit.setText(
                news
            )  # 읽은 데이터를 텍스트에 표시
