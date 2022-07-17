from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QLineEdit
from PyQt6.QtGui import QColor,QRegularExpressionValidator
import sys
import socket
import ServerorClient
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtWidgets import QMessageBox



class MainClientPage(QWidget,QColor):  
    def __init__(self):
        super().__init__()     
        # try: 
        #     host_name=socket.getfqdn()
        #     ip=socket.gethostbyname(host_name)
        # except:
        #     ip="Disconnected"
        # if ip=="Disconnected":
        #     self.disconnected() 

        # self.setWindowTitle(f"Client PC : {ip}")
                             
        self.main_window()
        
    def disconnected(self):
        msg=QMessageBox(self)
        msg.setWindowTitle("Network Disconnected")
        msg.setText("Server PC appears to be disconnected from the Client PC")
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setStandardButtons(QMessageBox.StandardButton.Abort)
    
    def receive_from_server():
        s = socket.socket()
        host = socket.gethostname()
        port = 9077
        s.connect((host, port))
        print(s.recv(1024))
    
    def main_window(self):   
        self.setGeometry(750,200,450,350)
        self.vbox=QVBoxLayout()

        self.new_client_user=QLineEdit()
        self.new_client_user.setFixedHeight(35)
        self.setProperty("class","main")
        self.new_client_user.setPlaceholderText(" Name of new user")
        
        self.new_client_password=QLineEdit()
        self.new_client_password.setFixedHeight(35)
        self.new_client_password.setPlaceholderText(" Password")
        self.new_client_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.server_ip=QLineEdit()
        self.server_ip.setFixedHeight(35)
        self.server_ip.setPlaceholderText(" Server IP Address")

        self.main_user_account_password=QLineEdit()
        self.main_user_account_password.setFixedHeight(35)
        self.main_user_account_password.setPlaceholderText(" Main user account password")
        self.main_user_account_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.main_user_account_password.setProperty("class","server_input")

        ip_address="(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
        regex_ip=QRegularExpression("^" + ip_address + "\\." + ip_address + "\\." + ip_address + "\\." + ip_address + "$")
        ipValidator=QRegularExpressionValidator(regex_ip, self) 
        self.server_ip.setValidator(ipValidator)

        self.client=QPushButton("Begin Process",self)
        self.client.setStyleSheet('background-color: green')
        self.client.setFixedHeight(50)
        self.client.clicked.connect(self.proceed)


        self.exit=QPushButton("Exit",self)
        self.exit.setStyleSheet('background-color: red')
        self.exit.setFixedHeight(50)
        
        self.vbox.addWidget(self.new_client_user)
        self.vbox.addWidget(self.new_client_password)
        self.vbox.addWidget(self.server_ip)
        self.vbox.addWidget(self.main_user_account_password)
        self.vbox.addWidget(self.client)
        self.vbox.addWidget(self.exit)
        self.setLayout(self.vbox)

        try:
            self.exit.clicked.connect(self.close)
        except:
            pass
    def buttonClicked(self):
            sys.exit()
    def proceed(self):
        def report(self,text):
            report=QMessageBox(self)
            report.setWindowTitle("Incomplete Details")
            report.setText(f"{text}")
            report.setIcon(QMessageBox.Icon.Critical)
            report.setStandardButtons(QMessageBox.StandardButton.Ok)
            report.exec()

        if len(self.new_client_user.text())==0:
            report(self,text="Name of new user is empty")

        elif len(self.new_client_password.text())==0:
            report(self,text="Please input a password")

        elif len(self.server_ip.text())==0:
            report(self,text="Please input Server IP Address")

        elif self.server_ip.text().count(".") < 3:
            report(self,text="Incomplete Server IP Address")
        else:
            
            msg=QMessageBox(self)
            msg.setWindowTitle("Review Details")
            msg.setText("These details will be used to create the MPI cluster. Proceed?")
            msg.setInformativeText(f"Name of user : {self.new_client_user.text()}\nServer IP Address : {self.server_ip.text()}")
    
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.No|QMessageBox.StandardButton.Yes)
            button=msg.exec()
            if button==QMessageBox.StandardButton.Yes:
                pass
           

    def client1(self):  
        self.client01=MainClientPage()                                         
        self.client01.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServerorClient.Window()
    sys.exit(app.exec())