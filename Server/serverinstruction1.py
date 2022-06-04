from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QMainWindow
from PyQt6.QtGui import QColor,QFont
from PyQt6.QtCore import Qt
import sys
import ServerorClient
import services
  

class MainServerPage(QWidget,QColor):  
    def __init__(self):
        super().__init__()                                     
        self.setWindowTitle("Server Window")
        self.address = QLabel(f"Server PC : {services.ip}", self)
        self.address.setAlignment(Qt.AlignmentFlag.AlignLeading)
        self.address.setFont(QFont("Arial",15))
        self.setGeometry(450,200,600,500)
        self.vbox=QVBoxLayout()
        self.server=QPushButton("Create a new user",self)
       
        self.server.setStyleSheet('background-color: green')
        self.vbox.addWidget(self.address)
        self.vbox.addWidget(self.server)
        self.setLayout(self.vbox)
        

    def server1(self):  
        self.server01=MainServerPage()                                         
        self.server01.show()


        
        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServerorClient.Window()
    sys.exit(app.exec())