# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 19:57:11 2017

@author: Dom
"""

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QSizePolicy
class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, width=5, height=4, dpi=100, pie=False):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
        self.ax = self.figure.add_subplot(111)
        if pie:
            self.ax.axis('off')
#            self.figure.tight_layout()
    
    def clearData(self):
        self.ax.cla()
        self.draw()
    
    def plot_function(self, x_data, function, points):
        y = [function(x) for x in x_data]
        y_points = [function(p) for p in points]
        self.ax.cla()
        self.ax.plot(x_data, y, linewidth=0.5)
        self.ax.plot(points, y_points, 'o')
        self.ax.set_title('Fitness function')
        self.draw() 
        
    def plot_history(self, max_history, avg_history, min_history):
        self.ax.cla()
        self.ax.plot(max_history, 'g-', linewidth=6)
        self.ax.plot(avg_history, 'c-', linewidth=3)
        self.ax.plot(min_history, 'r-', linewidth=0.8)
        self.ax.set_title('Maximum, average and miniumum fitness')
        self.draw()
        
    def plot_pie(self, population):
        
        self.ax.cla()
        explode = (0, 0.5, 0, 0)
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
        data = []
        values = [population.function(creature) for creature in set(population.int_pop)]
        data = [value / sum(values) for value in values]
        self.ax.pie(data, autopct="%1.1f%%", shadow = True)
#        self.ax.set_title('Users Per Platform')
        self.ax.set_aspect('1')
        self.draw()
        