# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:17:37 2020

@author: gr8ar
"""

from PyQt5.QtWidgets import * 
from PyQt5 import QtCore 
from PyQt5.QtGui import * 
import sys 
  
  
class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() 
  
        # changing the background color to yellow 
        self.setStyleSheet("background-color: yellow;") 
  
        # set the title 
        self.setWindowTitle("Color") 
  
        # setting  the geometry of window 
        self.setGeometry(0, 0, 400, 300) 
  
        # creating a label widget 
        self.label = QLabel("Yellow", self) 
  
        # moving position 
        self.label.move(100, 100) 
  
        # setting up border 
        self.label.setStyleSheet("border: 1px solid black;") 
  
  
  
        # show all the widgets 
        self.show() 
  
  
# create pyqt5 app 
App = QApplication(sys.argv) 
  
# create the instance of our Window 
window = Window() 
  
# start the app 
sys.exit(App.exec()) 