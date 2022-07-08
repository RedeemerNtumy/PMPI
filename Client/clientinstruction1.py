from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QLineEdit
from PyQt6.QtGui import QColor
import sys
import os
import cmd
import socket
import ServerorClient



class MainClientPage(QWidget,QColor):  
    def __init__(self):
        super().__init__()     
        try: 
            ip=socket.gethostbyname(socket.getfqdn())
        except:
            ip="Disconnected"
        if ip=="Disconnected":
            self.disconnected() 

        self.setWindowTitle(f"Client PC : {ip}")
                             
        self.main_window()
    
    def main_window(self):   
        self.setGeometry(750,200,450,350)
        self.vbox=QVBoxLayout()

        self.new_client_user=QLineEdit()
        self.new_client_user.setFixedHeight(35)
       
        self.new_client_user.setPlaceholderText(" Name of new user")
        
        
        
        

        self.new_client_password=QLineEdit()
        self.new_client_password.setFixedHeight(35)
        self.new_client_password.setPlaceholderText(" Password")
        self.new_client_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.server_ip=QLineEdit()
        self.server_ip.setFixedHeight(35)
        self.server_ip.setPlaceholderText(" Server IP Address")

        self.client=QPushButton("Begin Process",self)
        self.client.setStyleSheet('background-color: green')
        self.client.setFixedHeight(50)

        self.back=QPushButton("Exit",self)
        self.back.setStyleSheet('background-color: red')
        self.back.setFixedHeight(50)
        

        self.vbox.addWidget(self.new_client_user)
        self.vbox.addWidget(self.new_client_password)
        self.vbox.addWidget(self.server_ip)
        self.vbox.addWidget(self.client)
        self.vbox.addWidget(self.back)
        self.setLayout(self.vbox)

        try:
            self.back.clicked.connect(self.buttonClicked)
        except:
            pass
    def buttonClicked(self):
            os.system(cmd)
            QApplication.instance().quit()

    def client1(self):  
        self.client01=MainClientPage()                                         
        self.client01.show()


        
        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServerorClient.Window()
    sys.exit(app.exec())