from turtle import color
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QComboBox
from PyQt6.QtGui import QColor,QFont,QGuiApplication
from PyQt6.QtCore import Qt
import sys
import Home
import Server.serverinstruction1
import Client.clientinstruction1


class ChooseWindow(QWidget,QColor):  
    def __init__(self):
        super().__init__()
        self.main_window()   

    def center(self):
        qr=self.frameGeometry()
        cp=QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def main_window(self):                                  
        self.setWindowTitle("Client or Server")
        self.setProperty("class","main")

        self.device_type=QLabel("Select a device type")
        self.device_type.setFont(QFont("Serif",20,QFont.Weight.DemiBold))
        self.device_type.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.device_type.setProperty("class","label_select")

        self.type_of_device=QComboBox()
        self.type_of_device.setFixedHeight(100)
        self.type_of_device.setStyleSheet(" QComboBox::drop-down {border-width: 0px;} QComboBox::down-arrow {image: url(noimg); border-width: 0px;}")
        self.type_of_device.setProperty("class","combo_cont")
        self.type_of_device.addItems(["Click to select","Server","Client"])
        self.type_of_device.setFont(QFont("Serif",14,QFont.Weight.ExtraLight))
        self.type_of_device.setFixedWidth(350)
        

        self.question = QLabel("Would you like this PC to be the Server or the Client?", self)
        self.question.setProperty("class","label_cont")
        self.question.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.question.setFont(QFont("Serif",16,QFont.Weight.ExtraLight))

       

        self.vbox=QVBoxLayout()
        self.vbox.addStretch()
        self.vbox.setSpacing(0)
        self.vbox.setProperty("class","server_client_layout")
        
    
        self.continued=QPushButton("Continue",self)
        self.continued.setFont(QFont("Serif",16,QFont.Weight.ExtraLight))
        self.continued.setProperty("class","continued")
        self.continued.setFixedHeight(50)
        self.continued.setFixedWidth(350)

        self.vbox.addWidget(self.device_type)
        self.vbox.addWidget(self.question)
        self.vbox.addWidget(self.type_of_device)
        self.vbox.addWidget(self.continued)
        self.vbox.setAlignment(Qt.AlignmentFlag.AlignAbsolute)
        self.vbox.addStretch(0)
        
    
        self.setLayout(self.vbox)

        self.chooseWindow1=Server.serverinstruction1.MainServerPage()
        self.chooseWindow2=Client.clientinstruction1.MainClientPage()

        # self.server.clicked.connect(self.chooseWindow1.server1)
        # self.client.clicked.connect(self.chooseWindow2.client1)           

    def serverclient(self):  
        self.serclient=ChooseWindow()                                         
        self.serclient.show()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Home.Window()
    sys.exit(app.exec())