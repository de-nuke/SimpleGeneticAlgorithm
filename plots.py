# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 19:57:11 2017

@author: Dom
"""

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QSizePolicy
import numpy as np

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
        
    def plot_history(self, max_history, avg_history, min_history, left_x, right_x):
        self.ax.cla()
        style = '-' if len(max_history) > 1 else '*'
        self.ax.plot(max_history, 'g'+style, linewidth=6)
        self.ax.plot(avg_history, 'c'+style, linewidth=3)
        self.ax.plot(min_history, 'r'+style, linewidth=0.8)
        self.ax.set_title('Maximum, average and miniumum fitness')
        self.ax.set_xbound(left_x, right_x)
        self.draw()
        
    def plot_pie(self, population):
        def make_autopct(total, n):
            def my_autopct(pct):
                val = int(round(pct*total/100.0))
                if n <= 5:
                    return '{p:.2f}%\n({v:d}/{t:d})'.format(p=pct,v=val,t=int(total))
                elif n < 20:
                    return '{p:d}%'.format(p=int(pct))
                else:
                    return ''
            return my_autopct
        
        self.ax.cla()
        explode = []
        labels = []
        data = []
        times = []
        for x in set(population.int_pop):
            explode.append(0.1)
            labels.append(str(x) + ' x' + str(population.int_pop.count(x)))
            times.append(population.int_pop.count(x))
        
        explode = tuple(explode)
        values = [population.function(creature) for creature in set(population.int_pop)]
        sum_values = sum([population.function(creature) for creature in population.int_pop])
        data = [(value / 1) * times[i] for i, value in enumerate(values)]
        patches, texts, autotexts = self.ax.pie(data, autopct=make_autopct(sum_values, len(data)), shadow = True, explode=explode, labels=labels)
        for t in texts:
            t.set_fontsize(14 if len(data) < 35 else 10) 
        for at in autotexts:
            at.set_fontsize(10)
        self.ax.set_aspect('1')
        self.draw()
        