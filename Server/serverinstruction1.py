from ctypes import alignment
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QMainWindow
from PyQt6.QtGui import QColor,QFont
from PyQt6.QtCore import Qt
import sys
import ServerorClient


class MainServerPage(QWidget,QColor):  
    def __init__(self):
        super().__init__()                                     
        self.setWindowTitle("Client or Server")
        self.question = QLabel("You have now been connected as the server", self)
        self.question.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.question.setFont(QFont("Arial",20))
        self.setGeometry(450,200,600,500)
        self.vbox=QVBoxLayout()
        self.server=QPushButton("Server",self)
        self.client=QPushButton("Client",self)
        self.server.setStyleSheet('background-color: green')
        self.client.setStyleSheet('background-color: blue')
        self.vbox.addWidget(self.question)
        self.vbox.addWidget(self.server)
        self.vbox.addWidget(self.client)
        self.setLayout(self.vbox)
        

    def server1(self):  
        self.server01=MainServerPage()                                         
        self.server01.show()


        
        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServerorClient.Window()
    sys.exit(app.exec())