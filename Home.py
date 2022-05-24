from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout
from PyQt6.QtGui import QFont,QColor
from PyQt6.QtCore import Qt
import sys
import ServerorClient

class Window(QWidget,QColor):
    def __init__(self):
        super().__init__()
        self.show()
        self.main_window()


    
    def main_window(self):
        self.label_start = QLabel("Establish an MPI cluster within a LAN with ease", self)
        self.label_start.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_start.setFont(QFont("Arial",20))
        self.vbox=QVBoxLayout()
        self.setWindowTitle("PMPI Server")
        self.setGeometry(450,200,600,500)
        self.btn_start=QPushButton("Get Started",self)
        self.btn_start.setStyleSheet('background-color: green')
        self.vbox.addWidget(self.label_start)
        self.vbox.addWidget(self.btn_start)
        self.setLayout(self.vbox)
        self.chooseWindow=ServerorClient.ChooseWindow()
        self.btn_start.clicked.connect(self.chooseWindow.serverclient)
        self.btn_start.clicked.connect(self.hide)
         
        
    

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())


 