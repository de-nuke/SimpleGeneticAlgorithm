# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 16:28:49 2017

@author: Dom
"""

from GeneticAlgorithm import Population
from utils import Circle, radius, color
from random import randrange as rand
from collections import deque
from PyQt5.QtCore import QThread, pyqtSignal
import matplotlib.pyplot as plt

DEQUE_SIZE = 20

def f(x):
    return -0.1*x**2 + 4*x + 7

#class NextStep(QThread):
#    def __init__(self, al):
#        QThread.__init__(self)
#        self.al = al
#        self.main_window = al.main_window
#        self.population = al.population
#        self.x_range = range(-1, 42)
#        self.isRunning = False
#        
#    def run(self):
#        self.population.reproduct().cross().mutate()
#        self.al.counter += 1
#        self.main_window.log_label.setText('Iteration no. ' + str(self.al.counter))
#        
#        self.al.avg_history.append(round(self.population.average*10000)/10000)
#        self.al.max_history.append(round(self.population.maximum*10000)/10000)
#        self.al.min_history.append(round(self.population.minimum*10000)/10000)
#        
#        self.main_window.function_plot.plot_function(self.x_range, self.population.function, self.population.int_pop)
#        self.main_window.history_plot.plot_history(self.al.max_history[-DEQUE_SIZE:], self.al.avg_history[-DEQUE_SIZE:], self.al.min_history[-DEQUE_SIZE:])
#        
#        if len(self.al.avg_history) > 2000:
#            self.al.avg_history = []
#            self.al.max_history = []
#            self.al.min_history = []

class AutoStep(QThread):
    def __init__(self, al):
        QThread.__init__(self)
        self.al = al
        self.main_window = al.main_window
        self.population = al.population
        self.x_range = range(-1, 42)
        self.isRunning = False
        
        
    def __del__(self):
        self.terminate()
        
    def stop(self):
        self.isRunning = False
        
    def activate(self):
        self.isRunning = True
        
    def run(self):
        while True:
            if self.isRunning:
                self.population.reproduct().cross().mutate()
                self.al.counter += 1
                self.main_window.log_label.setText('Iteration no. ' + str(self.al.counter))
                
                self.al.avg_history.append(round(self.population.average*10000)/10000)
                self.al.max_history.append(round(self.population.maximum*10000)/10000)
                self.al.min_history.append(round(self.population.minimum*10000)/10000)
                
                self.main_window.function_plot.plot_function(self.x_range, self.population.function, self.population.int_pop)
                self.main_window.history_plot.plot_history(self.al.max_history[-DEQUE_SIZE:], self.al.avg_history[-DEQUE_SIZE:], self.al.min_history[-DEQUE_SIZE:])
            
                if len(self.al.avg_history) > 2000:
                    self.al.avg_history = []
                    self.al.max_history = []
                    self.al.min_history = []
                
class ApplicationLogic(object):
    def __init__(self, main_window):
        self.main_window = main_window
#        if not population_size and not function:
#            self.population = Population()
#        elif not population_size and function:
#            self.population = Population(function=function)
#        elif not function and population_size:
#            self.population = Population(population_size=population_size)
#        else:
#            self.population = Population(population_size, function)
            
        self.population = Population()
        self.avg_history = [] # deque([], DEQUE_SIZE)
        self.max_history = [] # deque([], DEQUE_SIZE)
        self.min_history = [] # deque([], DEQUE_SIZE)
        self.counter = 0
        self.last_dumped_index = 0
        self.x_range = range(-1, 42)
        self.thread =  AutoStep(self)
#        self.thread2 = NextStep(self)
        self.main_window.clear_btn.clicked.connect(self.thread.stop)
            
    def next_step(self):
#        self.thread2.start()
        self.population.reproduct().cross().mutate()
        self.counter += 1
        
        self.avg_history.append(self.population.average)
        self.max_history.append(self.population.maximum)
        self.min_history.append(self.population.minimum)
        
#        self.main_window.log_label.setText(self.population.dump())
#        self.main_window.scene.clear()
#        w = self.main_window.canvas.width()
#        h = self.main_window.canvas.height()
        
#        minimum = self.population.minimum
#        maximum = self.population.maximum
    
#        for creature in self.population.population:
#            self.main_window.scene.addItem(
#                Circle(
#                    x=rand(0, w), 
#                    y=rand(0, h), 
#                    r=radius(creature, minimum, maximum),
#                    fill_color=color(creature, minimum, maximum)
#                )
#            )
        
        
        points = self.population.int_pop
        
        self.main_window.function_plot.plot_function(self.x_range, self.population.function, points )
        self.main_window.history_plot.plot_history(self.max_history[-DEQUE_SIZE:], self.avg_history[-DEQUE_SIZE:], self.min_history[-DEQUE_SIZE:])
        self.main_window.pie_plot.plot_pie(self.population)
    
        if len(self.avg_history) > 2000:
            self.avg_history = []
            self.max_history = []
            self.min_history = []
        
            
    def apply_parameters(self):
        size = self.main_window.pop_size.value()
        cross_probability = self.main_window.cross_prob.value()
        mutate_probability = self.main_window.mutate_prob.value()
        self.population = Population(size, cross_probability, mutate_probability)
        self.population.setFunction(f)
        self.thread.population = self.population
#        self.thread2.population = self.population
        self.main_window.start_auto_btn.setDisabled(False)
        self.main_window.next_step_btn.setDisabled(False)
        self.main_window.reset_btn.setDisabled(False)
        self.main_window.apply_btn.setDisabled(True)
        self.main_window.pop_size.setDisabled(True)
        self.main_window.cross_prob.setDisabled(True)
        self.main_window.mutate_prob.setDisabled(True)
        
    def reset(self):
        self.main_window.clear_btn.clicked.emit()
        self.main_window.next_step_btn.setDisabled(False)
        self.population = Population()
        self.avg_history = [] # deque([], DEQUE_SIZE)
        self.max_history = [] # deque([], DEQUE_SIZE)
        self.min_history = [] # deque([], DEQUE_SIZE)
        self.main_window.history_plot.clearData()
        self.main_window.function_plot.clearData()
        self.main_window.next_step_btn.setDisabled(True)
        self.main_window.start_auto_btn.setDisabled(True)
        self.main_window.apply_btn.setDisabled(False)
        self.main_window.reset_btn.setDisabled(True)
        self.main_window.pop_size.setDisabled(False)
        self.main_window.cross_prob.setDisabled(False)
        self.main_window.mutate_prob.setDisabled(False)
        self.thread.counter = 0
        self.counter = 0
        
    def stop(self):
        self.main_window.clear_btn.setDisabled(True)
        self.main_window.next_step_btn.setDisabled(False)
        
    def start_auto(self):
        self.main_window.clear_btn.setDisabled(False)
        self.main_window.next_step_btn.setDisabled(True)
        if not self.thread.isRunning:
            self.thread.start()
        self.thread.activate()
        
    def show_more_history(self):
        
        if self.main_window.avg_check.checkState():
            plt.plot(self.avg_history, color='c')
        if self.main_window.max_check.checkState(): 
            plt.plot(self.max_history, color='g')
        if self.main_window.min_check.checkState():
            plt.plot(self.min_history, color='r')
        plt.show()