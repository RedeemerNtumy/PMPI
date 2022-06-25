from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit,QGridLayout,QLabel
from PyQt6.QtGui import QColor,QFont
from PyQt6.QtCore import Qt
import sys
import ServerorClient
import services
  

class MainServerPage(QWidget,QColor):  
    def __init__(self):     
        super().__init__()                                
        self.setWindowTitle(f"Server PC : {services.ip}")
        self.main_window()
        
     
      
    def main_window(self):
        self.back=QPushButton("<<    Back",self)
        self.back.setStyleSheet('background-color: red')
        self.setGeometry(450,200,600,500)
        self.gbox=QGridLayout()
        self.new_server_user=QLineEdit()
        self.new_server_user.setPlaceholderText("Name of new user")
        self.new_server_password=QLineEdit()
        self.new_server_password.setPlaceholderText("Password")
        self.new_server_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.o=QLineEdit()
        self.p=QLineEdit()
        self.q=QLineEdit()
        self.r=QLineEdit()
        self.s=QLineEdit()
        self.t=QLineEdit()
        self.heading=QPushButton("FILL IN THE INFORMATION BELOW",self)
        self.heading.setStyleSheet('background:rgb(50,50,50)')
        self.server=QPushButton("Next   >>",self)
        self.server.setStyleSheet('background-color: green')
        self.gbox.addWidget(self.heading,0,0)
        self.gbox.addWidget(self.new_server_user,1,0)
        self.gbox.addWidget(self.new_server_password,1,1)
        self.gbox.addWidget(self.o,2,0)
        self.gbox.addWidget(self.p,2,1)
        self.gbox.addWidget(self.q,3,0)
        self.gbox.addWidget(self.r,3,1)
        self.gbox.addWidget(self.s,4,0)
        self.gbox.addWidget(self.t,4,1)
        self.gbox.addWidget(self.back,5,0)
        self.gbox.addWidget(self.server,5,1)
        self.setLayout(self.gbox)
        try:
            self.go_back=ServerorClient.ChooseWindow()
            self.back.clicked.connect(self.go_back.serverclient)
            self.back.clicked.connect(self.close)
        except:
            pass

    def server1(self):  
        self.server01=MainServerPage()                                         
        self.server01.show()


        
        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServerorClient.Window()
    sys.exit(app.exec())