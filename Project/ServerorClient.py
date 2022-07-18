from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout
from PyQt6.QtGui import QColor,QFont
from PyQt6.QtCore import Qt
import sys
import Home
import Server.serverinstruction1
import Client.clientinstruction1


class ChooseWindow(QWidget,QColor):  
    def __init__(self):
        super().__init__()
        self.main_window()   

    def main_window(self):                                  
        self.setWindowTitle("Client or Server")
        self.setProperty("class","main")

        self.question = QLabel("Would you like this PC to be the Server or the Client?", self)
        self.question.setProperty("class","label")
        self.question.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.question.setFont(QFont("Arial",20))

        self.setGeometry(350,200,600,500)

        self.vbox=QVBoxLayout()
        self.vbox.setProperty("class","server_client_layout")

        self.server=QPushButton("Server",self)
        self.server.setFixedHeight(50)
        self.server.setProperty("class","server_button")
       

        self.client=QPushButton("Client",self)
        self.client.setFixedHeight(50)
        self.client.setProperty("class","client_button")

        self.vbox.addWidget(self.question)
        self.vbox.addWidget(self.server)
        self.vbox.addWidget(self.client)
        
        self.setLayout(self.vbox)

        self.chooseWindow1=Server.serverinstruction1.MainServerPage()
        self.chooseWindow2=Client.clientinstruction1.MainClientPage()

        self.server.clicked.connect(self.chooseWindow1.server1)
        self.client.clicked.connect(self.chooseWindow2.client1)           

    def serverclient(self):  
        self.serclient=ChooseWindow()                                         
        self.serclient.show()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Home.Window()
    sys.exit(app.exec())