# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 19:57:11 2017

@author: Dom
"""

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QSizePolicy


class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
 
 
    def plot_function(self, x_data, function, points):
        self.figure.clear()
        y = [function(x) for x in x_data]
        y_points = [function(p) for p in points]
        ax = self.figure.add_subplot(111)
        
        ax.plot(x_data, y, linewidth=0.5)
        ax.plot(points, y_points, 'o')
        ax.set_title('Fitness function')
        self.draw() 
        
    def plot_history(self, max_history, avg_history, min_history):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        
        ax.plot(max_history, 'g-')
        ax.plot(avg_history, 'b-')
        ax.plot(min_history, 'r-')
        ax.set_title('Maximum, average and miniumum fitness')
        self.draw()
        