from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit,QVBoxLayout,QHBoxLayout,QComboBox,QFileDialog,QLabel
from PyQt6.QtGui import QColor,QMovie,QIntValidator,QRegularExpressionValidator,QGuiApplication,QFont
import sys
import os
import ServerorClient
from pathlib import Path
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt,QRegularExpression
import socket
import subprocess
import pwd



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
        self.move(qr.center())

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
        
        self.setProperty("class","main")
        self.fill_form=QLabel("Fill form below to establish connection")
        self.fill_form.setStyleSheet("margin-bottom: 20")
        self.fill_form.setFont(QFont("Serif",20,QFont.Weight.DemiBold))
        self.fill_form.setProperty("class","label_fill")
        
        self.vbox=QVBoxLayout()
        self.vbox.setAlignment(Qt.AlignmentFlag.AlignAbsolute)

        self.vbox.addStretch()
        self.vbox.setSpacing(0)
        
        
        self.new_client_user=QLineEdit()
        self.new_client_user.setStyleSheet("border: 1px solid rgb(123, 156, 222);\n border-radius:5px;margin-bottom:15")
        self.new_client_user.setFixedHeight(55)
        self.new_client_user.setFixedWidth(650)
        self.new_client_user.setPlaceholderText("Username of Client PC")
        self.new_client_user.setProperty("class","server_input")

        self.ip_client=QLabel("Client IP Address",self)
        self.ip_client.setStyleSheet("margin-bottom: 5")
        self.ip_client.setFont(QFont("Serif",12,QFont.Weight.ExtraLight))
        self.ip_client.setProperty("class","label_cons")

       

        self.mpi_file=QLabel("MPI File",self)
        self.mpi_file.setStyleSheet("margin-bottom: 5")
        self.mpi_file.setFont(QFont("Serif",12,QFont.Weight.ExtraLight))
        self.mpi_file.setProperty("class","label_cons")


        self.client_user_name=QLabel("Client Username",self)
        self.client_user_name.setStyleSheet("margin-bottom: 5")
        self.client_user_name.setFont(QFont("Serif",12,QFont.Weight.ExtraLight))
        self.client_user_name.setProperty("class","label_cons")

        self.hosts=QLabel("Hosts",self)
        self.hosts.setStyleSheet("margin-bottom: 5")
        self.hosts.setFont(QFont("Serif",12,QFont.Weight.ExtraLight))
        self.hosts.setProperty("class","label_cons")


        self.space1=QLabel("    ",self)
        self.space2=QLabel("    ",self)

        self.new_server_password=QLineEdit()
        self.new_server_password.setStyleSheet("border: 1px solid rgb(123, 156, 222);\n border-radius:5px")
        self.new_server_password.setFixedHeight(55)
        self.new_server_password.setFixedWidth(650)
        self.new_server_password.setPlaceholderText(" Password")
        self.new_server_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.new_server_password.setProperty("class","server_input")

        self.choose_file=QPushButton("Choose File")
        self.choose_file.setStyleSheet("margin-bottom:15")
        self.choose_file.setFont(QFont("Serif",16,QFont.Weight.ExtraLight))
        self.choose_file.setProperty("class","cancel")
        self.choose_file.setFixedHeight(55)
        self.choose_file.setFixedWidth(650)
        self.choose_file.clicked.connect(self.showFileDialog)
        
        self.type_of_code=QComboBox()
        self.type_of_code.setFixedHeight(55)
        self.type_of_code.setFixedWidth(650)
        self.type_of_code.setStyleSheet(" QComboBox::drop-down {border-width: 0px;} QComboBox::down-arrow {image: url(noimg); border-width: 0px;}")
        self.type_of_code.setProperty("class","combo_tins")
        self.type_of_code.addItems(["Type of MPI Code","C","C++"])
        self.type_of_code.setFont(QFont("Serif",12,QFont.Weight.ExtraLight))

        self.number_of_ranks=QLineEdit()
        self.number_of_ranks.setStyleSheet("border: 1px solid rgb(123, 156, 222);\n border-radius:5px;\n margin-bottom:15")
        self.number_of_ranks.setFixedHeight(55)
        self.number_of_ranks.setFixedWidth(650)
        self.number_of_ranks.setPlaceholderText(" Number of ranks")
        self.number_of_ranks.setValidator(QIntValidator())
        self.number_of_ranks.setProperty("class","server_input")


        
        self.client_ip=QLineEdit()
        self.client_ip.setStyleSheet("border: 1px solid rgb(123, 156, 222);\n border-radius:5px;\n margin-bottom:15")
        self.client_ip.setFixedHeight(55)
        self.client_ip.setFixedWidth(650)
        self.client_ip.setPlaceholderText(" Client IP Address")
        self.client_ip.setProperty("class","server_input")


        ip_address="(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
        regex_ip=QRegularExpression("^" + ip_address + "\\." + ip_address + "\\." + ip_address + "\\." + ip_address + "$")
        ipValidator=QRegularExpressionValidator(regex_ip, self) 
        self.client_ip.setValidator(ipValidator)

        self.exit=QPushButton("Cancel",self)
        self.exit.setProperty("class","cancel")
        self.exit.setFixedHeight(40)
        self.exit.setFixedWidth(150)
        self.exit.setFont(QFont("Serif",16,QFont.Weight.ExtraLight))
        

        

        self.server=QPushButton("Connect",self)
        self.server.setProperty("class","continued")
        self.server.setFont(QFont("Serif",16,QFont.Weight.ExtraLight))
        self.server.setFixedHeight(40)
        self.server.setFixedWidth(150)
        self.server.clicked.connect(self.proceed)
        
        self.hbox=QHBoxLayout()
        self.hbox.addWidget(self.exit)
        self.hbox.addWidget(self.server)

        self.load=loading_screen()
        self.load.hide()
        
        self.vbox.addWidget(self.fill_form)

        self.vbox.addWidget(self.ip_client)
        self.vbox.addWidget(self.client_ip)

        self.vbox.addWidget(self.client_user_name)
        self.vbox.addWidget(self.new_client_user)

        self.vbox.addWidget(self.mpi_file)
        self.vbox.addWidget(self.choose_file)

        self.vbox.addWidget(self.hosts)
        self.vbox.addWidget(self.number_of_ranks)
    

        self.vbox.addWidget(self.space1)

        self.vbox.addLayout(self.hbox)

        self.vbox.addStretch(0)
        self.setLayout(self.vbox)
    
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


        if len(self.number_of_ranks.text())==0:
            report(self,text="Please input number of ranks")

        if len(self.client_ip.text())==0:
            report(self,text="Please input Client IP Address")

        if self.client_ip.text().count(".") < 3:
            report(self,text="Incomplete Client IP Address")
        else:
            try:
                msg=QMessageBox(self)
                msg.setWindowTitle("Review Details")
                msg.setText("These details will be used to create the MPI cluster. Proceed?")
                msg.setInformativeText(f"Chosen file : {fileName}\nNumber of ranks : {self.number_of_ranks.text()}\nClient IP Address : {self.client_ip.text()}")
    
                msg.setIcon(QMessageBox.Icon.Information)
                msg.setStandardButtons(QMessageBox.StandardButton.No|QMessageBox.StandardButton.Yes)
                button=msg.exec()
                if button==QMessageBox.StandardButton.Yes:
                    self.load.show()

                    #wait for client PC to connect
                    try:
                        subprocess.Popen("rm -d test",shell=True).communicate()[0]
                    except:
                        print("No default directory")
                    subprocess.Popen("cd ..;cd ..;mkdir test",shell=True).communicate()[0]
                    
                    with open("/etc/exports","w") as f:
                        pc_name="iamdveloper"
                        f.write(f"\n#/home/{pc_name}/default *(rw,sync,no_root_squash,no_subtree_check)")
                    subprocess.Popen("exportfs -a",shell=True).communicate()[0]
                    
                    
                    
                    
            
                elif button==QMessageBox.StandardButton.No:
                    self.load.hide()

            except:
                incomplete=QMessageBox(self)
                incomplete.setWindowTitle("Incomplete Details")
                incomplete.setText("An Error occured")
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