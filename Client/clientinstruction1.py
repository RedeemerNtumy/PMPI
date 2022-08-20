from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QLineEdit,QLabel,QHBoxLayout
from PyQt6.QtGui import QColor,QRegularExpressionValidator,QGuiApplication,QFont
import sys
import socket
import ServerorClient
from PyQt6.QtCore import QRegularExpression,Qt
from PyQt6.QtWidgets import QMessageBox



class MainClientPage(QWidget,QColor):  
    def __init__(self):
        super().__init__()     
        try: 
            host_name=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            host_name.connect(("8.8.8.8",80))
            ip=host_name.getsockname()[0]
        except:
            ip="Disconnected"
        if ip=="Disconnected":
            self.disconnected() 

        self.setWindowTitle(f"Client PC : {ip}")
                             
        self.main_window()

    def center(self):
        qr=self.frameGeometry()
        cp=QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.center())
        
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
       
        self.fill_form=QLabel("Fill form below to establish connection")
        self.fill_form.setStyleSheet("margin-bottom: 20")
        self.fill_form.setFont(QFont("Serif",20,QFont.Weight.DemiBold))
        self.fill_form.setProperty("class","label_fill")
        self.setProperty("class","main")
        
       

        self.vbox=QVBoxLayout()
        self.vbox.setAlignment(Qt.AlignmentFlag.AlignAbsolute)

        self.vbox.addStretch()
        self.vbox.setSpacing(0)

        self.name_user=QLabel("Name")
        self.name_user.setStyleSheet("margin-bottom: 5")
        self.name_user.setFont(QFont("Serif",12,QFont.Weight.ExtraLight))
        self.name_user.setProperty("class","label_cons")

        self.connect_password=QLabel("Connection Password",self)
        self.connect_password.setFont(QFont("Serif",12,QFont.Weight.ExtraLight))
        self.connect_password.setStyleSheet("margin-bottom: 5")
        self.connect_password.setProperty("class","label_cons")

        self.main_password=QLabel("Main User Account Password",self)
        self.main_password.setStyleSheet("margin-bottom: 5")
        self.main_password.setFont(QFont("Serif",12,QFont.Weight.ExtraLight))
        self.main_password.setProperty("class","label_cons")

        self.ip_server=QLabel("IP Address",self)
        self.ip_server.setStyleSheet("margin-bottom: 5")
        self.ip_server.setFont(QFont("Serif",12,QFont.Weight.ExtraLight))
        self.ip_server.setProperty("class","label_cons")


        self.new_client_user=QLineEdit()
        self.new_client_user.setFixedHeight(55)
        self.new_client_user.setFixedWidth(650)
        self.new_client_user.setProperty("class","server_input")
        self.new_client_user.setStyleSheet("border: 1px solid rgb(123, 156, 222);\n border-radius:5px;\nmargin-bottom:15")
        self.new_client_user.setPlaceholderText(" Name of new user")
        
        self.new_client_password=QLineEdit()
        self.new_client_password.setFixedHeight(55)
        self.new_client_password.setFixedWidth(650)
        self.new_client_password.setProperty("class","server_input")
        self.new_client_password.setStyleSheet("border: 1px solid rgb(123, 156, 222);\n border-radius:5px;\nmargin-bottom:15")
        self.new_client_password.setPlaceholderText(" Password")
        self.new_client_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.server_ip=QLineEdit()
        self.server_ip.setFixedHeight(55)
        self.server_ip.setFixedWidth(650)
        self.server_ip.setProperty("class","server_input")
        self.server_ip.setStyleSheet("border: 1px solid rgb(123, 156, 222);\n border-radius:5px;\nmargin-bottom:15")
        self.server_ip.setPlaceholderText(" Server IP Address")

        self.main_user_account_password=QLineEdit()
        self.main_user_account_password.setFixedHeight(55)
        self.main_user_account_password.setFixedWidth(650)
        self.main_user_account_password.setProperty("class","server_input")
        self.main_user_account_password.setStyleSheet("border: 1px solid rgb(123, 156, 222);\n border-radius:5px;\nmargin-bottom:15")
        self.main_user_account_password.setPlaceholderText(" Main user account password")
        self.main_user_account_password.setEchoMode(QLineEdit.EchoMode.Password)
        

        ip_address="(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
        regex_ip=QRegularExpression("^" + ip_address + "\\." + ip_address + "\\." + ip_address + "\\." + ip_address + "$")
        ipValidator=QRegularExpressionValidator(regex_ip, self) 
        self.server_ip.setValidator(ipValidator)

        self.client=QPushButton("Connect",self)
        self.client.setProperty("class","continued")
        self.client.setFont(QFont("Serif",16,QFont.Weight.ExtraLight))
        self.client.setFixedHeight(40)
        self.client.setFixedWidth(150)
        self.client.clicked.connect(self.proceed)
        self.space1=QLabel("    ",self)

        self.exit=QPushButton("Cancel",self)
        self.exit.setProperty("class","cancel")
        self.exit.setFixedHeight(40)
        self.exit.setFixedWidth(150)
        self.exit.setFont(QFont("Serif",16,QFont.Weight.ExtraLight))
        
        self.vbox.addWidget(self.fill_form)
        
        self.vbox.addWidget(self.name_user)
        self.vbox.addWidget(self.new_client_user,alignment=Qt.AlignmentFlag.AlignCenter)

        self.vbox.addWidget(self.connect_password)
        self.vbox.addWidget(self.new_client_password,alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.vbox.addWidget(self.ip_server)
        self.vbox.addWidget(self.server_ip,alignment=Qt.AlignmentFlag.AlignCenter)

        self.vbox.addWidget(self.main_password)
        self.vbox.addWidget(self.main_user_account_password,alignment=Qt.AlignmentFlag.AlignCenter)
        self.vbox.addWidget(self.space1)
        


        self.hbox=QHBoxLayout()
        self.hbox.addWidget(self.exit)
        self.hbox.addWidget(self.client)
        

        self.vbox.addLayout(self.hbox)

        self.vbox.addStretch(0)
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