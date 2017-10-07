# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 20:54:28 2017

@author: Dom
"""

'''
Zadanie 1 
Napisać program umożliwiający znalezienie maksimum funkcji dopasowania jednej 
zmiennej określonej dla liczb całkowitych w zadanym zakresie przy pomocy 
elementarnego algorytmu genetycznego (reprodukcja z użyciem nieproporcjonalnej 
ruletki, krzyżowanie proste, mutacja równomierna). Program powinien umożliwiać 
użycie różnych funkcji dopasowania, populacji o różnej liczebności oraz różnych 
parametrów operacji genetycznych (krzyżowania i mutacji). Program powinien 
zapewnić wizualizację wyników w postaci wykresów średniego, maksymalnego 
i minimalnego przystosowania dla kolejnych populacji oraz wykresu funkcji 
w zadanym przedziale. 

Program przetestować dla funkcji f(x)= -0.1x^2 + 4x + 7 dla x= -1, O, ... 41 
'''

import sys
 
#from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
#from PyQt5.QtGui import QIcon
 
 
#from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.figure import Figure
#import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene
from PyQt5 import QtCore
from Window import Ui_MainWindow
from ApplicationLogic import ApplicationLogic

import seaborn as sns
from plots import PlotCanvas

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.al = ApplicationLogic(self, population_size=90, function=lambda x: -0.1*x**2 + 4*x + 7)
        self.next_step_btn.clicked.connect(self.al.next_step)
        
        self.scene = QGraphicsScene()
        self.canvas.setScene(self.scene)
        self.canvas.setSceneRect(0,0,self.canvas.frameSize().width(),self.canvas.frameSize().height())
        self.canvas.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff);
        self.canvas.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff);
        
        sns.set()
        sns.set_style('whitegrid')
        self.function_plot = PlotCanvas(self.frame, width=self.frame.width()/100, height=self.frame.height()/100)
        self.function_plot.move(0,0)
        
        self.history_plot = PlotCanvas(self.frame_2, width=self.frame_2.width()/100, height=self.frame_2.height()/100)
        self.history_plot.move(0,0)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    x = MainWindow()
    x.show()

    sys.exit(app.exec_())
