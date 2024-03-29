from asyncio.subprocess import PIPE
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
import time
import pexpect


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
    pc_name=socket.gethostname() 
    def __init__(self):    
        global ip 
        super().__init__() 
        try: 
            host_name=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            host_name.connect(("8.8.8.8",80))
            ip=host_name.getsockname()[0]
            host_name.close()
        except:
            ip="Disconnected"
        if ip=="Disconnected":
            self.disconnected() 

        self.setWindowTitle(f"Server PC : {ip}")
        self.main_window() 
    
           
       
    def disconnected(self):
        msg=QMessageBox(self)
        msg.setWindowTitle("Network Disconnected")
        msg.setText("A network error occured")
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
        

        self.ip_client=QLabel("Client IP Address",self)
        self.ip_client.setStyleSheet("margin-bottom: 5")
        self.ip_client.setFont(QFont("Serif",12,QFont.Weight.ExtraLight))
        self.ip_client.setProperty("class","label_cons")

       

        self.mpi_file=QLabel("MPI File",self)
        self.mpi_file.setStyleSheet("margin-bottom: 5")
        self.mpi_file.setFont(QFont("Serif",12,QFont.Weight.ExtraLight))
        self.mpi_file.setProperty("class","label_cons")

        self.hosts=QLabel("Ranks",self)
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
        global fileName,lines,path_to_code
        try:
            home_dir = str(Path.home())
            mpich_file=QFileDialog.getOpenFileName(self, 'Open file', home_dir)
            path_to_code=os.path.dirname(mpich_file[0])
            file_name = os.path.basename(str(mpich_file))
            file_name=file_name.split(",")[0]
            file_name=file_name[:-1]
            with open(mpich_file[0]) as f:
                lines = f.readlines()
                  
            if "MPI_Init" not in str(lines) and "MPI_Finalize" not in str(lines):
                self.invalid_file()
            if "cpp" in file_name:
                self.choose_file.setStyleSheet("background-color:#004ADB;\n color: white;\n margin-bottom:15")
            elif "c" in file_name:
                self.choose_file.setStyleSheet("background-color:#004ADB;\n color: white;\n margin-bottom:15")
            elif len(file_name)==0:
                self.invalid_file()
            else:
                self.invalid_file()
                pass 
            self.choose_file.setText(file_name)
            
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
        self.choose_file.setStyleSheet("margin-bottom:15")
        self.choose_file.setFont(QFont("Serif",16,QFont.Weight.ExtraLight))
        self.choose_file.setProperty("class","cancel")
        self.choose_file.setFixedHeight(55)
        self.choose_file.setFixedWidth(650)
        self.choose_file.setText("Choose File")
    
    
    
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
                msg.setInformativeText(f"Chosen file : {fileName}\nNumber of ranks : {self.number_of_ranks.text()}\nClient IP Address : {self.client_ip.text()}\n\nThis would create a deafult folder |mpichdefault|. Any instance of a folder with the same name will be deleted")
    
                msg.setIcon(QMessageBox.Icon.Information)
                msg.setStandardButtons(QMessageBox.StandardButton.No|QMessageBox.StandardButton.Yes)
                button=msg.exec()
                if button==QMessageBox.StandardButton.Yes:
                    try:
                        s.close()
                    except:
                        pass
                    check()
                    if check:
                        self.close()
                        try:
                            with open("/etc/exports","a") as f:
                                f.write(f"\n/home/{info}/mpichdefault *(rw,sync,no_root_squash,no_subtree_check)")
                                
                            work=subprocess.Popen("cd ..;cd ..;mkdir mpichdefault",shell=True,stderr=PIPE,stdout=PIPE)
                            stdout,stderr=work.communicate()[0] 
                            print("Finished writing")
                        except:
                            print("Overwriting directory with mpichdefault")
                            subprocess.Popen("cd ..;cd ..;rm -r mpichdefault;mkdir mpichdefault",shell=True).communicate()[0]

                            subprocess.Popen("exportfs -a",shell=True).communicate()[0]
                            time.sleep(3)
                            if "cpp" in fileName:
                                    subprocess.Popen(f"cd {path_to_code};cp {fileName} /home/{info}/mpichdefault",shell=True).communicate()[0]
                                    subprocess.Popen(f"cd /home/{info}/mpichdefault;mpic++ {fileName} -o job.exe",shell=True).communicate()[0]
                            elif "c" in fileName:
                                    subprocess.Popen(f"cd {path_to_code};cp {fileName} /home/{info}/mpichdefault",shell=True).communicate()[0]
                                    subprocess.Popen(f"cd /home/{info}/mpichdefault;mpicc -o job.exe {fileName}",shell=True).communicate()[0]
                            print("Everything Works")
                            output=QMessageBox(self)
                            output.setWindowTitle("Setup Complete")
                            output.setText(f"Run the code below in the command line to send the job to the client PC\nmpirun -np {self.number_of_ranks.text()} -hosts {self.client_ip.text()},{ip} ./job.exe\n")
                            client_ip=self.client_ip.text()
                            output.setIcon(QMessageBox.Icon.Information)
                            output.setStandardButtons(QMessageBox.StandardButton.Ok|QMessageBox.StandardButton.Close)
                            final=output.exec()  
                            if final==QMessageBox.StandardButton.Close:
                                try:
                                    s.close()
                                except:
                                    pass
                                send(client_ip)
                                reset_everything_server()
                                
                            elif final==QMessageBox.StandardButton.Ok:
                                subprocess.Popen("cd ..;cd ..;cd mpichdefault;gnome-terminal -- su joshua",shell=True)
                                output=QMessageBox(self)
                                output.setWindowTitle("Done Already?")
                                output.setText(f"Click the button below if you are done running the code")
                                output.setIcon(QMessageBox.Icon.Information)
                                output.setStandardButtons(QMessageBox.StandardButton.Ok)
                                final=output.exec() 
                                if final==QMessageBox.StandardButton.Ok:
                                    try:
                                        s.close()
                                    except:
                                        pass
                                    send(client_ip)
                                    reset_everything_server()
                            
                elif button==QMessageBox.StandardButton.No:
                    print("There is a problem")
                    

            except Exception as e:
                print(e)
                incomplete=QMessageBox(self)
                incomplete.setWindowTitle("Error")
                incomplete.setText("Something bad happened 😞")
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




def check():
        global info,s
        try:
            print
            s=socket.socket()
            port=65030
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
            incomplete.setText("The Server PC failed to connect to the client PC")
            incomplete.setIcon(QMessageBox.Icon.Critical)
            incomplete.setStandardButtons(QMessageBox.StandardButton.Ok)
            incomplete.exec() 
            s.close()
        return True 

def send(host):
            global s
            s=socket.socket()
            port=65040
            s.connect((host,port))
            s.send("Info".encode())
            print("sent")
            s.close()

def reset_everything_server():
    subprocess.Popen(f"sed -i '$d' /etc/exports",shell=True).communicate()[0]
    time.sleep(1)
    subprocess.Popen(f"cd ..;cd ..;rm -r mpichdefault;cd .ssh;rm id_rsa;rm id_rsa.pub",shell=True).communicate()[0]
    sys.exit()
