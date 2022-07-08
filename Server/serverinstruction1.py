from logging import critical
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit,QGridLayout,QComboBox,QFileDialog,QLabel
from PyQt6.QtGui import QColor,QMovie,QIntValidator,QRegularExpressionValidator
import sys
import ServerorClient
from pathlib import Path
import os
import cmd
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt,QRegularExpression
import socket

class loading_screen(QWidget):
    def __init__(self):     
        super().__init__() 
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint| Qt.WindowType.CustomizeWindowHint |Qt.WindowType.FramelessWindowHint)  
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground)
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)  
        self.label_animate=QLabel(self)
        self.movie=QMovie('images/load_small.gif')
        self.label_animate.setMovie(self.movie)
        self.setFixedSize(50,50)
        self.setGeometry(625,420,450,350)
        self.start_animation()
        

        self.show()

    def start_animation(self):
        self.movie.start()
    

    

class MainServerPage(QWidget,QColor):  
    def __init__(self):     
        super().__init__() 
        # try: 
        #     ip=socket.gethostbyname(socket.getfqdn())
        # except:
        #     ip="Disconnected"
        # if ip=="Disconnected":
        #     self.disconnected() 

        # self.setWindowTitle(f"Server PC : {ip}")
        self.main_window()     
           
       
    def disconnected(self):
        msg=QMessageBox(self)
        msg.setWindowTitle("Network Disconnected")
        msg.setText("Server PC appears to be disconnected from the Client PC")
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setStandardButtons(QMessageBox.StandardButton.Abort)
       
        button=msg.exec()
        if button==QMessageBox.StandardButton.Abort:
            os.system(cmd)
            QApplication.instance().quit()
        else:
            pass

      
    def main_window(self):
        self.back=QPushButton("Exit",self)
        self.back.setFixedHeight(35)
        self.back.setStyleSheet('background-color: red')
        self.setGeometry(150,200,450,350)

        self.gbox=QGridLayout()
        
        self.new_server_user=QLineEdit()
        self.new_server_user.setFixedHeight(35)
        self.new_server_user.setPlaceholderText(" Name of new user")

        self.new_server_password=QLineEdit()
        self.new_server_password.setFixedHeight(35)
        self.new_server_password.setPlaceholderText(" Password")
        self.new_server_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.choose_file=QPushButton("Choose File")
        self.choose_file.setFixedHeight(35)
        self.choose_file.clicked.connect(self.showFileDialog)

        self.type_of_code=QComboBox()
        self.type_of_code.setFixedHeight(35)
        self.type_of_code.addItems(["Type of MPI Code","C","C++"])

        self.number_of_hosts=QLineEdit()
        self.number_of_hosts.setFixedHeight(35)
        self.number_of_hosts.setPlaceholderText(" Number of hosts")
        self.number_of_hosts.setValidator(QIntValidator())

        self.ssh_key=QComboBox()
        self.ssh_key.setFixedHeight(35)
        self.ssh_key.addItems(["Type of ssh key","RSA","DSA"])
        
        self.client_ip=QLineEdit()
        self.client_ip.setFixedHeight(35)
        self.client_ip.setPlaceholderText(" Client IP Address")
        ip_address="(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
        regex_ip=QRegularExpression("^" + ip_address + "\\." + ip_address + "\\." + ip_address + "\\." + ip_address + "$")
        ipValidator=QRegularExpressionValidator(regex_ip, self) 
        self.client_ip.setValidator(ipValidator)
      
        self.server=QPushButton("Establish Connection",self)
        self.server.setFixedHeight(35)
        self.server.setStyleSheet('background-color: green')
        self.load=loading_screen()
        self.load.hide()
        self.server.clicked.connect(self.load.show)
       
        self.gbox.addWidget(self.new_server_user,1,0)
        self.gbox.addWidget(self.new_server_password,1,1)
        self.gbox.addWidget(self.choose_file,2,0)
        self.gbox.addWidget(self.type_of_code,2,1)
        self.gbox.addWidget(self.number_of_hosts,3,0)
        self.gbox.addWidget(self.ssh_key,3,1)
        self.gbox.addWidget(self.client_ip,4,0)
        self.gbox.addWidget(self.back,5,0)
        self.gbox.addWidget(self.server,5,1)


        self.setLayout(self.gbox)
    
        try:
            self.back.clicked.connect(self.buttonClicked)
        except:
            pass

    def buttonClicked(self):
            os.system(cmd)
            QApplication.instance().quit()

    def showFileDialog(self):
        try:
            home_dir = str(Path.home())
            mpich_file=QFileDialog.getOpenFileName(self, 'Open file', home_dir)
            file_name = os.path.basename(str(mpich_file))
            file_name=file_name.split(",")[0]
            file_name=file_name[:-1]
            self.choose_file.setText(file_name)
            if ".c++" in file_name:
                self.type_of_code.setCurrentText("C++")
                self.choose_file.setStyleSheet("background-color: green")
            elif ".c" in file_name:
                self.type_of_code.setCurrentText("C")
                self.choose_file.setStyleSheet("background-color: green")
            else:
                self.choose_file.setText("Choose File")
                self.invalid_file()
                pass 

         
        except:
            pass
        
    def invalid_file(self):
        msg=QMessageBox(self)
        msg.setWindowTitle("Invalid File")
        msg.setText("The file you chose has an invalid file format")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setStandardButtons(QMessageBox.StandardButton.Retry)
        msg.exec()
       
     
    def server1(self):  
        self.server01=MainServerPage()                                         
        self.server01.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServerorClient.Window()
    sys.exit(app.exec())