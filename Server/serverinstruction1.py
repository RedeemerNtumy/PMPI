from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit,QGridLayout,QLabel,QComboBox,QFileDialog
from PyQt6.QtGui import QColor,QFont
from PyQt6.QtCore import Qt
import sys
import ServerorClient
import services
from pathlib import Path
import os

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
        self.new_server_user.setFixedHeight(35)
        self.new_server_user.setPlaceholderText(" Name of new user")

        self.new_server_password=QLineEdit()
        self.new_server_password.setFixedHeight(35)
        self.new_server_password.setPlaceholderText(" Password")
        self.new_server_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.choose_file=QPushButton("Choose File")
        self.choose_file.setFixedHeight(35)
        self.choose_file.clicked.connect(self.showDialog)

        self.type_of_code=QComboBox()
        self.type_of_code.setFixedHeight(35)
        self.type_of_code.addItems(["Type of MPI Code","C","C++"])

        self.number_of_hosts=QLineEdit()
        self.number_of_hosts.setFixedHeight(35)
        self.number_of_hosts.setPlaceholderText(" Number of hosts")

        self.ssh_key=QComboBox()
        self.ssh_key.setFixedHeight(35)
        self.ssh_key.addItems(["Type of ssh key","RSA","DSA"])

       
       
        self.server=QPushButton("Establish Connection",self)
        self.server.setStyleSheet('background-color: green')

       
        self.gbox.addWidget(self.new_server_user,1,0)
        self.gbox.addWidget(self.new_server_password,1,1)
        self.gbox.addWidget(self.choose_file,2,0)
        self.gbox.addWidget(self.type_of_code,2,1)
        self.gbox.addWidget(self.number_of_hosts,3,0)
        self.gbox.addWidget(self.ssh_key,3,1)
      
        self.gbox.addWidget(self.back,5,0)
        self.gbox.addWidget(self.server,5,1)

        self.setLayout(self.gbox)
        try:
            self.go_back=ServerorClient.ChooseWindow()
            self.back.clicked.connect(self.go_back.serverclient)
            self.back.clicked.connect(self.close)
        except:
            pass

    def showDialog(self):
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
                self.choose_file.setText("Invalid File Type")
                print(type(self.type_of_code.currentText()))
                self.choose_file.setStyleSheet("background-color: red")       
        except:
            pass
        # try:
        #     if self.type_of_code.currentText()=="Type of MPI code":
        #         pass
        #     elif self.type_of_code.currentText()=="C++" and ".c++" not in file_name:
        #         self.choose_file.setText("Invalid File Type")
        #         self.choose_file.setStyleSheet("background-color: red")
        #     elif self.type_of_code.currentText()=="C" and ".c" not in file_name:
        #         self.choose_file.setText("Invalid File Type")
        #         self.choose_file.setStyleSheet("background-color: red")
        # except:
        #     pass


           

    def server1(self):  
        self.server01=MainServerPage()                                         
        self.server01.show()


        
        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServerorClient.Window()
    sys.exit(app.exec())