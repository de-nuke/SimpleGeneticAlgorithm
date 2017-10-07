# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 16:28:49 2017

@author: Dom
"""

from GeneticAlgorithm import Population
from utils import Circle
from random import randrange as rand
from collections import deque

def f(x):
    return -0.1*x**2 + 4*x + 7


class ApplicationLogic(object):
    def __init__(self, main_window, population_size=None, function=None):
        self.main_window = main_window
        
        if not population_size and not function:
            self.population = Population()
        elif not population_size and function:
            self.population = Population(function=function)
        elif not function and population_size:
            self.population = Population(population_size=population_size)
        else:
            self.population = Population(population_size, function)
            
        self.avg_history = deque([], 20)
        self.max_history = deque([], 20)
        self.min_history = deque([], 20)
        
        self.x_range = range(-1, 42)
            
    def next_step(self):
        
        self.population.reproduct().cross().mutate()
        
        self.avg_history.append(self.population.average)
        self.max_history.append(self.population.maximum)
        self.min_history.append(self.population.minimum)
        
        #self.main_window.log_label.setText(self.population.dump())
#        w = self.main_window.canvas.width()
#        h = self.main_window.canvas.height()
#        circle = Circle(
#                x=rand(0, w), 
#                y=rand(0, h), 
#                r=10, 
#                fill_color=(0, 255, 0)
#        )
        #self.main_window.scene.addItem(circle)
        points = self.population.int_pop
        self.main_window.function_plot.plot_function(self.x_range, self.population.function, points )
        
        
        ''' to bardzo spowalnia! szczegolnie clear'''
        self.main_window.history_plot.plot_history(self.max_history, self.avg_history, self.min_history)
    
        
