from ctypes import alignment
from turtle import _Screen, Screen, screensize, width
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QLineEdit
from PyQt6.QtGui import QColor,QFont
from PyQt6.QtCore import Qt
import sys

from numpy import spacing
import ServerorClient
import services


class MainClientPage(QWidget,QColor):  
    def __init__(self):
        super().__init__()                                     
        self.setWindowTitle(f"Client PC : {services.ip}")
      
     
        self.setGeometry(450,200,600,500)
        self.vbox=QVBoxLayout()

        self.new_client_user=QLineEdit()
        self.new_client_user.setFixedHeight(35)
        # print(type(QApplication(sys.argv).primaryScreen().size().width()))
        # self.new_client_user.setFixedWidth(app.primaryScreen().size().width())
        self.new_client_user.setPlaceholderText(" Name of new user")


        self.new_client_password=QLineEdit()
        self.new_client_password.setFixedHeight(35)
        self.new_client_password.setPlaceholderText(" Password")
        self.new_client_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.client=QPushButton("Begin Process",self)
        self.client.setStyleSheet('background-color: green')

        self.back=QPushButton("<<   Back",self)
        self.back.setStyleSheet('background-color: red')

        self.vbox.addWidget(self.new_client_user)
        self.vbox.addWidget(self.new_client_password)
        self.vbox.addWidget(self.client)
        self.vbox.addWidget(self.back)
        self.setLayout(self.vbox)
        

    def client1(self):  
        self.client01=MainClientPage()                                         
        self.client01.show()


        
        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServerorClient.Window()
    sys.exit(app.exec())