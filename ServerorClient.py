from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QComboBox,QMessageBox
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
        self.move(qr.center())

    def main_window(self):    
                                   
        self.setWindowTitle("Client or Server")
        self.setProperty("class","main")

        self.device_type=QLabel("Select a device type")
        self.device_type.setFont(QFont("Arial",20,QFont.Weight.DemiBold))
        self.device_type.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.device_type.setProperty("class","label_select")

        self.type_of_device=QComboBox()
        self.type_of_device.setFixedHeight(100)
        self.type_of_device.setFixedWidth(350)
        self.type_of_device.setStyleSheet(" QComboBox::drop-down {border-width: 0px;} QComboBox::down-arrow {image: url(noimg); border-width: 0px;}")
        self.type_of_device.setProperty("class","combo_cont")
        self.type_of_device.addItems(["Click to select","Server","Client"])
        self.type_of_device.setFont(QFont("Arial",14,QFont.Weight.ExtraLight))
        
        

        self.question = QLabel("Would you like this PC to be the Server or the Client?", self)
        self.question.setProperty("class","label_cont")
        self.question.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.question.setFont(QFont("Arial",16,QFont.Weight.ExtraLight))

       

        self.vbox=QVBoxLayout()
        self.vbox.addStretch()
        self.vbox.setSpacing(0)
        self.vbox.setProperty("class","server_client_layout")
        
    
        self.continued=QPushButton("Continue",self)
        self.continued.setFont(QFont("Arial",16,QFont.Weight.ExtraLight))
        self.continued.setProperty("class","continued")
        self.continued.setFixedHeight(40)
        self.continued.setFixedWidth(350)

        self.vbox.addWidget(self.device_type,alignment=Qt.AlignmentFlag.AlignCenter)
        self.vbox.addWidget(self.question,alignment=Qt.AlignmentFlag.AlignCenter)
        self.vbox.addWidget(self.type_of_device,alignment=Qt.AlignmentFlag.AlignCenter)
        self.vbox.addWidget(self.continued,alignment=Qt.AlignmentFlag.AlignCenter)
        self.vbox.setAlignment(Qt.AlignmentFlag.AlignAbsolute)
        self.vbox.addStretch(0)
        
    
        self.setLayout(self.vbox)

        self.chooseWindow1=Server.serverinstruction1.MainServerPage()
        self.chooseWindow2=Client.clientinstruction1.MainClientPage()

        self.continued.clicked.connect(self.proceed)
              

    def serverclient(self):  
        self.serclient=ChooseWindow()                                         
        self.serclient.show()

    def proceed(self):
        if self.type_of_device.currentText()=="Server":
        
            self.chooseWindow1.show()
        elif self.type_of_device.currentText()=="Client":
            
            self.chooseWindow2.show()
            
        else:
            msg=QMessageBox(self)
            msg.setWindowTitle("Review Details")
            msg.setText("Please select the type of device")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Home.Window()
    sys.exit(app.exec())