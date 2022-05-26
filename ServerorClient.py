from ctypes import alignment
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QMainWindow
from PyQt6.QtGui import QColor,QFont
from PyQt6.QtCore import Qt
import sys
import Home
import Server.serverinstruction1
import Client.clientinstruction1


class ChooseWindow(QWidget,QColor):  
    def __init__(self):
        super().__init__()                                     
        self.setWindowTitle("Client or Server")
        self.question = QLabel("Would you like this PC to be the Server or the Client?", self)
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
        self.chooseWindow1=Server.serverinstruction1.MainServerPage()
        self.chooseWindow2=Client.clientinstruction1.MainClientPage()
        self.server.clicked.connect(self.chooseWindow1.server1)
        self.server.clicked.connect(self.hide)
        self.client.clicked.connect(self.chooseWindow2.client1)
        self.client.clicked.connect(self.hide)

    def serverclient(self):  
        self.serclient=ChooseWindow()                                         
        self.serclient.show()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Home.Window()
    sys.exit(app.exec())