from ctypes import alignment
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QMainWindow
from PyQt6.QtGui import QColor,QFont
from PyQt6.QtCore import Qt
import sys
import ServerorClient
import services


class MainClientPage(QWidget,QColor):  
    def __init__(self):
        super().__init__()                                     
        self.setWindowTitle(f"Client PC : {services.ip}")
      
     
        self.setGeometry(450,200,600,500)
        self.vbox=QVBoxLayout()
        self.client=QPushButton("Create a new user",self)
        self.client.setStyleSheet('background-color: green')

        self.vbox.addWidget(self.client)
        self.setLayout(self.vbox)
        

    def client1(self):  
        self.client01=MainClientPage()                                         
        self.client01.show()


        
        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServerorClient.Window()
    sys.exit(app.exec())