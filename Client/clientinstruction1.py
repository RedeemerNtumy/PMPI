from asyncio.subprocess import PIPE
from time import time
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QLineEdit,QLabel,QHBoxLayout
from PyQt6.QtGui import QColor,QRegularExpressionValidator,QGuiApplication,QFont
import sys
import socket
from Server.serverinstruction1 import loading_screen
import ServerorClient
from PyQt6.QtCore import QRegularExpression,Qt
from PyQt6.QtWidgets import QMessageBox
import asyncio
import subprocess
import os
import time


class MainClientPage(QWidget,QColor):  
    pc_name=socket.gethostname()
    def __init__(self):
        super().__init__()     
        try: 
            global host_name
            host_name=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            host_name.connect(("8.8.8.8",80))
            ip=host_name.getsockname()[0]
            host_name.close()
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
        msg.setText("A netowrk error occured")
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


        self.ip_server=QLabel("Server IP Address",self)
        self.ip_server.setStyleSheet("margin-bottom: 5")
        self.ip_server.setFont(QFont("Serif",12,QFont.Weight.ExtraLight))
        self.ip_server.setProperty("class","label_cons")
        
       

        self.server_ip=QLineEdit()
        self.server_ip.setFixedHeight(55)
        self.server_ip.setFixedWidth(650)
        self.server_ip.setProperty("class","server_input")
        self.server_ip.setStyleSheet("border: 1px solid rgb(123, 156, 222);\n border-radius:5px;\nmargin-bottom:15")
        self.server_ip.setPlaceholderText(" Server IP Address")


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
        
        self.vbox.addWidget(self.ip_server)
        self.vbox.addWidget(self.server_ip,alignment=Qt.AlignmentFlag.AlignCenter)
        
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

        # if len(self.server_username.text())==0:
        #     report(self,text="Name of server username is empty")

        if len(self.server_ip.text())==0:
            report(self,text="Please input Server IP Address")

        elif self.server_ip.text().count(".") < 3:
            report(self,text="Incomplete Server IP Address")
        else:
            
            msg=QMessageBox(self)
            msg.setWindowTitle("Review Details")
            msg.setText("These details will be used to create the MPI cluster. Proceed?")
            msg.setInformativeText(f"Name of user : {self.server_username.text()}\nServer IP Address : {self.server_ip.text()}")
    
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.No|QMessageBox.StandardButton.Yes)
            button=msg.exec()
            if button==QMessageBox.StandardButton.Yes:
                try:
                    info=self.server_ip.text()
                    name=os.environ['SUDO_USER']
                    send(info,name)
                    self.close()
                    time.sleep(3)
                    try:
                        work=subprocess.Popen("cd ..;cd ..;mkdir mpichdefault",shell=True,stderr=PIPE,stdout=PIPE)
                        stdout,stderr=work.communicate()[0]
                    except:
                        print("Overwriting directory with mpichdefault")
                        subprocess.Popen(f"cd ..;cd ..;rm -r mpichdefault;mkdir mpichdefault;mount -t nfs {self.server_ip.text()}:home/{self.server_username.text()}/mpichdefault /home/{self.server_username.text()}/mpichdefault ",shell=True).communicate()[0]
                        time.sleep(2)
                        check()
                        if check:
                          subprocess.Popen(f"cd ..;cd ..;umount -f -l /home/joshua/mpichdefault;rm -r mpichdefault;cd .ssh;rm authorized_keys;exit",shell=True).communicate()[0]
                          print("Everything works")
                except:
                    msg=QMessageBox(self)
                    msg.setIcon(QMessageBox.Icon.Critical)
                    msg.setWindowTitle("Critical Error")
                    msg.setText("Could not mount directory")
                

             
           

    def client1(self):  
        self.client01=MainClientPage()                                         
        self.client01.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServerorClient.Window()
    sys.exit(app.exec())

def send(host,name):
            s=socket.socket()
            port=65014
            s.connect((host,port))
            s.send(name.encode())
            print("sent")
            s.close()
      
def waste_time():
    for number in range(1,99999):
        print("Working...please wait")

def check():
        global info
        try:
            print
            s=socket.socket()
            port=65010
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(("",port))
            s.listen(5)
            print("Server Started")
            info=""
            while len(info)==0:
                c,addr=s.accept()
                print("Message received")
                content=c.recv(100).decode()
                info=content
                print(info)
                c.close()
            s.close()  
          
        except Exception as e:
            print(e)
            incomplete=QMessageBox()
            incomplete.setWindowTitle("Broken Connection")
            incomplete.setText("There seems to be a problem")
            incomplete.setIcon(QMessageBox.Icon.Critical)
            incomplete.setStandardButtons(QMessageBox.StandardButton.Ok)
            incomplete.exec() 
            s.close()
        return True 
