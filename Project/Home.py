import cmd
from tkinter.font import BOLD
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout
from PyQt6.QtGui import QFont,QColor
from PyQt6.QtCore import Qt
import sys

from numpy import size
import ServerorClient
import subprocess
import os
import pyautogui


class Window(QWidget,QColor):
    def __init__(self):
        super().__init__()
        self.show()
        self.main_window()
    
    def main_window(self):
        self.label_start = QLabel("The Joy of PMPI", self)
        self.label_start.setFont(QFont("Serif",26,QFont.Weight.DemiBold))
        self.label_start.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_start.setProperty("class","label_start")
       
        self.label_cont=QLabel("A toolkit to help you create an mpi cluster within a lan with ease.",self)
        self.label_cont.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_cont.setFont(QFont("Serif",16,QFont.Weight.ExtraLight))
        self.label_cont.setProperty("class","label_cont")

        self.setProperty("class","main")

        self.vbox=QVBoxLayout()
        self.vbox.addStretch()
        self.vbox.setSpacing(0)
        self.vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vbox.setProperty("class","vbox")
        self.setWindowTitle("PMPI")
        self.setGeometry(350,200,600,500)
        

        self.btn_start=QPushButton("Get Started",self)
        self.btn_start.setFont(QFont("Serif",16,QFont.Weight.ExtraLight))
        self.btn_start.setProperty("class","get_started")

        self.btn_start.setFixedHeight(50)
        self.btn_start.setFixedWidth(380)
        
        self.vbox.addWidget(self.label_start)
        self.vbox.addWidget(self.label_cont)
        self.vbox.addWidget(self.btn_start)

        self.setLayout(self.vbox)

        self.chooseWindow=ServerorClient.ChooseWindow()

        self.btn_start.clicked.connect(self.chooseWindow.serverclient)
        self.btn_start.clicked.connect(self.close)
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    with open("style.css","r") as desktop_design:
        app.setStyleSheet(desktop_design.read())
    sys.exit(app.exec())


 