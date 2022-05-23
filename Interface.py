from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QMainWindow
from PyQt6.QtGui import QIcon,QFont,QColor
import sys


class ChooseWindow(QWidget,QColor):  
    def __init__(self):
        super().__init__()                                     
        self.setWindowTitle("New Screen")

class Window(QWidget,QColor):
    def __init__(self):
        super().__init__()
        self.main_window()
    
    def main_window(self):
        self.label_start = QLabel("Establish an MPI cluster within a LAN with ease", self)
        self.label_start.setFont(QFont("Arial",20))
        self.vbox=QVBoxLayout()
        self.setWindowTitle("PMPI Server")
        self.setGeometry(450,200,600,500)
        self.btn_start=QPushButton("Get Started",self)
        self.btn_start.setStyleSheet('background-color: green')
        self.vbox.addWidget(self.label_start)
        self.vbox.addWidget(self.btn_start)
        self.setLayout(self.vbox)
        self.btn_start.clicked.connect(self.window2)
        self.show()

    def window2(self):  
        self.w=ChooseWindow()
        self.setGeometry(450,200,600,500)                                          
        self.w.show()
        self.hide()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())


 