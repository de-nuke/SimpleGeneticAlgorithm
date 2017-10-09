# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 16:28:49 2017

@author: Dom
"""

from GeneticAlgorithm import Population
from utils import Circle, radius, color
from random import randrange as rand
from collections import deque

def f(x):
    return -0.1*x**2 + 4*x + 7


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
        
        self.main_window.history_plot.plot_history(self.max_history, self.avg_history, self.min_history)
    
        
    def apply_parameters(self):
        size = self.main_window.pop_size.value()
        cross_probability = self.main_window.cross_prob.value()
        mutate_probability = self.main_window.mutate_prob.value()
        self.population = Population(size, cross_probability, mutate_probability)
        self.population.setFunction(f)
        self.main_window.start_auto_btn.setDisabled(False)
        self.main_window.next_step_btn.setDisabled(False)
        self.main_window.reset_btn.setDisabled(False)
        self.main_window.apply_btn.setDisabled(True)
        self.main_window.pop_size.setDisabled(True)
        self.main_window.cross_prob.setDisabled(True)
        self.main_window.mutate_prob.setDisabled(True)
        
    def reset(self):
        self.population = Population()
        self.avg_history = deque([], 20)
        self.max_history = deque([], 20)
        self.min_history = deque([], 20)
        self.main_window.history_plot.clearData()
        self.main_window.function_plot.clearData()
        self.main_window.next_step_btn.setDisabled(True)
        self.main_window.start_auto_btn.setDisabled(True)
        self.main_window.apply_btn.setDisabled(False)
        self.main_window.reset_btn.setDisabled(True)
        self.main_window.pop_size.setDisabled(False)
        self.main_window.cross_prob.setDisabled(False)
        self.main_window.mutate_prob.setDisabled(False)