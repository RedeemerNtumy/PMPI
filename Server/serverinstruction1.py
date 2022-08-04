from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit,QGridLayout,QComboBox,QFileDialog,QLabel
from PyQt6.QtGui import QColor,QMovie,QIntValidator,QRegularExpressionValidator,QGuiApplication,QFont
import sys
import os
import ServerorClient
from pathlib import Path
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt,QRegularExpression
import socket
import subprocess




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
        # self.setGeometry(625,420,450,350)

        self.start_animation()
        self.show()

    def center(self):
        qr=self.frameGeometry()
        cp=QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft()) 

    def start_animation(self):
        self.movie.start()

class MainServerPage(QWidget,QColor):  
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

        self.setWindowTitle(f"Server PC : {ip}")
        self.main_window() 
      

    def send_to_client():
        s = socket.socket()
        host = socket.gethostname()
        port = 9077
        s.bind((host,port))
        s.listen(5)

        while True:
            c, addr = s.accept()
            print("Connection accepted from " + repr(addr[1]))
            c.send("Thank you for connecting")
            c.close() 
           
       
    def disconnected(self):
        msg=QMessageBox(self)
        msg.setWindowTitle("Network Disconnected")
        msg.setText("Server PC appears to be disconnected from the Client PC")
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setStandardButtons(QMessageBox.StandardButton.Abort)
       
        button=msg.exec()
        if button==QMessageBox.StandardButton.Abort:
            sys.exit()
        else:
            pass

      
    def main_window(self):
        
        self.setFixedHeight(700)
        self.setFixedWidth(1000)
        self.setProperty("class","main")

        self.gbox=QGridLayout()
        self.gbox.setSpacing(0)
        
        self.fill_form=QLabel("Fill form below to establish connection")
        self.fill_form.setFont(QFont("Serif",20,QFont.Weight.DemiBold))
        self.fill_form.setProperty("class","label_fill")
        
        self.name_server=QLabel("Name",self)
        self.name_server.setFont(QFont("Serif",14,QFont.Weight.ExtraLight))
        self.name_server.setProperty("class","label_cons")
        
        self.new_server_user=QLineEdit()
        self.new_server_user.setStyleSheet("border: 1px solid rgb(123, 156, 222);\n border-radius:5px")
        self.new_server_user.setFixedHeight(55)
        self.new_server_user.setFixedWidth(350)
        self.new_server_user.setPlaceholderText(" Name of new user")
        self.new_server_user.setProperty("class","server_input")
        # self.new_server_user.setText("Yes")
        # something=self.new_server_user.text()
        # os.environ(something)

        self.ip_client=QLabel("IP Address")
        self.ip_client.setFont(QFont("Serif",14,QFont.Weight.ExtraLight))
        self.ip_client.setProperty("class","label_cons")
        
        self.connect_password=QLabel("Connection Password",self)
        self.connect_password.setProperty("class","label_cons")

        self.mpi_file=QLabel("MPI File",self)
        self.mpi_file.setFont(QFont("Serif",14,QFont.Weight.ExtraLight))
        self.mpi_file.setProperty("class","label_cons")

        self.main_password=QLabel("Main User Account Password",self)
        self.main_password.setFont(QFont("Serif",14,QFont.Weight.ExtraLight))
        self.main_password.setProperty("class","label_cons")

        self.mpi_code=QLabel("MPI Code",self)
        self.mpi_code.setFont(QFont("Serif",14,QFont.Weight.ExtraLight))
        self.mpi_code.setProperty("class","label_cons")

        self.hosts=QLabel("Hosts",self)
        self.hosts.setFont(QFont("Serif",14,QFont.Weight.ExtraLight))
        self.hosts.setProperty("class","label_cons")

        self.ssh_key_label= QLabel("SSH Key",self)
        self.ssh_key_label.setFont(QFont("Serif",14,QFont.Weight.ExtraLight))
        self.ssh_key_label.setProperty("class","label_cons")

        self.new_server_password=QLineEdit()
        self.new_server_password.setStyleSheet("border: 1px solid rgb(123, 156, 222);\n border-radius:5px")
        self.new_server_password.setFixedHeight(55)
        self.new_server_password.setFixedWidth(350)
        self.new_server_password.setPlaceholderText(" Password")
        self.new_server_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.new_server_password.setProperty("class","server_input")

        self.choose_file=QPushButton("Choose File")
        self.choose_file.setFont(QFont("Serif",16,QFont.Weight.ExtraLight))
        self.choose_file.setProperty("class","cancel")
        self.choose_file.setFixedHeight(45)
        self.choose_file.setFixedWidth(350)
        self.choose_file.clicked.connect(self.showFileDialog)
        

        self.type_of_code=QComboBox()
        self.type_of_code.setFixedHeight(100)
        self.type_of_code.setFixedWidth(350)
        self.type_of_code.setStyleSheet(" QComboBox::drop-down {border-width: 0px;} QComboBox::down-arrow {image: url(noimg); border-width: 0px;}")
        self.type_of_code.setProperty("class","combo_tins")
        self.type_of_code.addItems(["Type of MPI Code","C","C++"])
        self.type_of_code.setFont(QFont("Serif",14,QFont.Weight.ExtraLight))

        self.number_of_ranks=QLineEdit()
        self.number_of_ranks.setStyleSheet("border: 1px solid rgb(123, 156, 222);\n border-radius:5px")
        self.number_of_ranks.setFixedHeight(55)
        self.number_of_ranks.setFixedWidth(350)
        self.number_of_ranks.setPlaceholderText(" Number of ranks")
        self.number_of_ranks.setValidator(QIntValidator())
        self.number_of_ranks.setProperty("class","server_input")

        self.ssh_key=QComboBox()
        self.ssh_key.setFixedHeight(100)
        self.ssh_key.setFixedWidth(350)
        self.ssh_key.setStyleSheet(" QComboBox::drop-down {border-width: 0px;} QComboBox::down-arrow {image: url(noimg); border-width: 0px;}")
        self.ssh_key.setProperty("class","combo_tins")
        self.ssh_key.addItems(["Type of ssh key","RSA","DSA"])
        self.ssh_key.setFont(QFont("Serif",14,QFont.Weight.ExtraLight))
        
        self.client_ip=QLineEdit()
        self.client_ip.setStyleSheet("border: 1px solid rgb(123, 156, 222);\n border-radius:5px")
        self.client_ip.setFixedHeight(55)
        self.client_ip.setFixedWidth(350)
        self.client_ip.setPlaceholderText(" Client IP Address")
        self.client_ip.setProperty("class","server_input")

        self.main_user_account_password=QLineEdit()
        self.main_user_account_password.setStyleSheet("border: 1px solid rgb(123, 156, 222);\n border-radius:5px")
        self.main_user_account_password.setFixedHeight(55)
        self.main_user_account_password.setFixedWidth(350)
        self.main_user_account_password.setPlaceholderText(" Main user account password")
        self.main_user_account_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.main_user_account_password.setProperty("class","server_input")

        ip_address="(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
        regex_ip=QRegularExpression("^" + ip_address + "\\." + ip_address + "\\." + ip_address + "\\." + ip_address + "$")
        ipValidator=QRegularExpressionValidator(regex_ip, self) 
        self.client_ip.setValidator(ipValidator)

        self.exit=QPushButton("Cancel",self)
        self.exit.setProperty("class","cancel")
        self.exit.setFixedHeight(45)
        self.exit.setFixedWidth(350)
        self.exit.setFont(QFont("Serif",16,QFont.Weight.ExtraLight))
        

        

        self.server=QPushButton("Establish Connection",self)
        self.server.setProperty("class","continued")
        self.server.setFont(QFont("Serif",16,QFont.Weight.ExtraLight))
        self.server.setFixedHeight(45)
        self.server.setFixedWidth(350)
        self.server.clicked.connect(self.proceed)

        self.load=loading_screen()
        self.load.hide()
        
        self.gbox.addWidget(self.fill_form,0,0)
        self.gbox.addWidget(self.name_server,1,0)
        self.gbox.addWidget(self.new_server_user,2,0)
        
        self.gbox.addWidget(self.ip_client,1,1)
        self.gbox.addWidget(self.client_ip,2,1)

        self.gbox.addWidget(self.connect_password,3,0)
        self.gbox.addWidget(self.new_server_password,4,0)

        self.gbox.addWidget(self.mpi_file,3,1)
        self.gbox.addWidget(self.choose_file,4,1)
    
        self.gbox.addWidget(self.main_password,5,0)
        self.gbox.addWidget(self.main_user_account_password,6,0)

        self.gbox.addWidget(self.mpi_code,5,1)
        self.gbox.addWidget(self.type_of_code,6,1)

        self.gbox.addWidget(self.hosts,7,0)
        self.gbox.addWidget(self.number_of_ranks,8,0)

        self.gbox.addWidget(self.ssh_key_label,7,1)
        self.gbox.addWidget(self.ssh_key,8,1)
        
        self.gbox.addWidget(self.exit,9,0)
        self.gbox.addWidget(self.server,9,1)

        self.gbox.setRowStretch(7, 0)
        self.setLayout(self.gbox)
    
        try:
            self.exit.clicked.connect(self.close)
            self.exit.clicked.connect(self.load.hide)
        except:
            pass

 

    fileName="Choose File"
    def showFileDialog(self):
        global fileName
        try:
            home_dir = str(Path.home())
            mpich_file=QFileDialog.getOpenFileName(self, 'Open file', home_dir)
            file_name = os.path.basename(str(mpich_file))
            file_name=file_name.split(",")[0]
            file_name=file_name[:-1]
            self.choose_file.setText(file_name)
            if ".c++" in file_name:
                self.type_of_code.setCurrentText("C++")
                self.choose_file.setStyleSheet("background-color:#004ADB;\n color: white;")
            elif ".c" in file_name:
                self.type_of_code.setCurrentText("C")
                self.choose_file.setStyleSheet("background-color:#004ADB;\n color: white;")
            else:
                self.choose_file.setText("Choose File")
                self.invalid_file()
                pass 
            
        except:
            fileName=file_name
        fileName=file_name
       
   

    def invalid_file(self):
        msg=QMessageBox(self)
        msg.setWindowTitle("Invalid File")
        msg.setText("The file you chose has an invalid file format")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setStandardButtons(QMessageBox.StandardButton.Retry)
        msg.exec()
    
    def proceed(self):
        global fileName

        def report(self,text):
            report=QMessageBox(self)
            report.setWindowTitle("Incomplete Details")
            report.setText(f"{text}")
            report.setIcon(QMessageBox.Icon.Critical)
            report.setStandardButtons(QMessageBox.StandardButton.Ok)
            report.exec()

        if len(self.new_server_user.text())==0:
            report(self,text="Name of new user is empty")

        elif len(self.new_server_password.text())==0:
            report(self,text="Please input a password")

        elif self.type_of_code.currentText()=="Type of MPI Code":
            report(self,text="Please choose the type of MPI Code")

        elif self.ssh_key.currentText()=="Type of ssh key":
            report(self,text="Please specify ssh key")

        elif len(self.number_of_ranks.text())==0:
            report(self,text="Please input number of ranks")

        elif len(self.client_ip.text())==0:
            report(self,text="Please input Client IP Address")

        elif self.client_ip.text().count(".") < 3:
            report(self,text="Incomplete Client IP Address")
        else:
            try:
                msg=QMessageBox(self)
                msg.setWindowTitle("Review Details")
                msg.setText("These details will be used to create the MPI cluster. Proceed?")
                msg.setInformativeText(f"Name of user : {self.new_server_user.text()}\nChosen file : {fileName}\nType of MPI Code : {self.type_of_code.currentText()}\nType of ssh key : {self.ssh_key.currentText()}\nNumber of ranks : {self.number_of_ranks.text()}\nClient IP Address : {self.client_ip.text()}")
    
                msg.setIcon(QMessageBox.Icon.Information)
                msg.setStandardButtons(QMessageBox.StandardButton.No|QMessageBox.StandardButton.Yes)
                button=msg.exec()
                if button==QMessageBox.StandardButton.Yes:
                    self.load.show()
                    # new_user_process=subprocess.Popen(f"sudo adduser {self.new_server_user.text()}").communicate()[0]
                    # new_user_process.stdin.write(f"{self.main_user_account_password.text()}").communicate()[0]
                    # new_user_process.stdin.close()

                    # try: 
                    #     host_name=socket.getfqdn()
                    #     ip=socket.gethostbyname(host_name)
                    # except:
                    #     ip="Disconnected"
                    # if ip=="Disconnected":
                    #     self.disconnected()


                    # "{ip}"
                    # process=subprocess.Popen(f'bash setup.sh "{self.new_server_user.text()}" "{self.new_server_password.text()}" "{self.main_user_account_password.text()}" "{fileName}" "{self.ssh_key.currentText()}" "{self.type_of_code.currentText()}" "{self.client_ip.text()}"',shell=True)
     
                    # process.communicate()[0]
                    
                    
                    
            
                elif button==QMessageBox.StandardButton.No:
                    self.load.hide()

            except:
                incomplete=QMessageBox(self)
                incomplete.setWindowTitle("Incomplete Details")
                incomplete.setText("File not uploaded")
                incomplete.setIcon(QMessageBox.Icon.Critical)
                incomplete.setStandardButtons(QMessageBox.StandardButton.Ok)
                incomplete.exec()   
     
    def server1(self):  
        self.server01=MainServerPage()                                         
        self.server01.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServerorClient.Window()
    sys.exit(app.exec())