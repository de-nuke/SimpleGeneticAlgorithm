# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 16:28:49 2017

@author: Dom
"""

from GeneticAlgorithm import Population
from random import randrange as rand
from collections import deque
from PyQt5.QtCore import QThread, pyqtSignal
import matplotlib.pyplot as plt
import math
from settings import *


''' end of const '''


def x_range(a,b):
    return range(a, b+1)


def no_change(values_list):
    """
    :param values_list:
    :return: TRUE if every element in the given list is the same
    """
    was_change = False
    for i in range(1,len(values_list)):
        if values_list[i] != values_list[i-1]:
            was_change = True
            break
    return not was_change


class AutoStep(QThread):
    def __init__(self, al):
        QThread.__init__(self)
        self.al = al
        self.main_window = al.main_window
        self.population = al.population
        self.x_range = al.x_range
        self.isRunning = False
        self.mode = 'ENDLESS'

    def __del__(self):
        self.terminate()
        
    def stop(self):
        self.isRunning = False
        
    def activate(self, mode):
        self.isRunning = True
        self.mode = mode
        
    def reset(self):
        self.main_window.log_label.setText('Iteration no. ' + str(self.al.counter))
        
    def run(self):
        while True:
            if self.isRunning:
                self.population.reproduct().cross().mutate()
                self.al.counter += 1
                self.main_window.log_label.setText('Iteration no. ' + str(self.al.counter))

                if self.population.maximum > self.al.all_time_max:
                    self.al.all_time_max = self.population.maximum
                    self.al.all_time_max_x = self.population.maximum_x_for(self.al.all_time_max)

                self.main_window.max_all_time_label.setText(str(self.al.all_time_max) + " for x = " + str(self.al.all_time_max_x))
                self.main_window.current_max.setText(str(round(self.population.maximum*10000)/10000))
                self.main_window.current_max_for.setText(str(self.population.maximum_x))
                
                self.main_window.current_avg.setText(str(round(self.population.average*10000)/10000))
                
                self.main_window.current_min.setText(str(round(self.population.minimum*10000)/10000))
                self.main_window.current_min_for.setText(str(self.population.minimum_x))
                
                self.al.avg_history.append(round(self.population.average*10000)/10000)
                self.al.max_history.append(round(self.population.maximum*10000)/10000)
                self.al.min_history.append(round(self.population.minimum*10000)/10000)

                if self.main_window.draw_plots.checkState():
                    self.main_window.function_plot.plot_function(self.x_range, self.population.function, self.population.int_pop)
                    self.main_window.history_plot.plot_history(
                        self.al.max_history,
                        self.al.avg_history,
                        self.al.min_history,
                        self.al.counter - DEQUE_SIZE,
                        self.al.counter)
                    self.main_window.pie_plot.plot_pie(self.population)
                
                if len(self.al.avg_history) > 2000:
                    self.al.avg_history = []
                    self.al.max_history = []
                    self.al.min_history = []
                if self.mode == 'SINGLE_STEP':
                    self.isRunning = False

                # STOP CONDITION
                self.al.maximum_history.append(self.population.maximum)
                if self.al.counter > 1000:
                    if no_change(self.al.population.population):
                        if no_change(self.al.maximum_history):
                            self.main_window.clear_btn.clicked.emit()
                            self.main_window.found_max.setText(str(self.population.maximum))
                            self.main_window.found_max_for.setText(str(self.population.maximum_x))
                            self.main_window.function_plot.plot_function(self.x_range, self.population.function,self.population.int_pop)
                            self.main_window.history_plot.plot_history(
                                self.al.max_history,
                                self.al.avg_history,
                                self.al.min_history,
                                self.al.counter - DEQUE_SIZE,
                                self.al.counter)
                            self.main_window.pie_plot.plot_pie(self.population)

                
class ApplicationLogic(object):
    def __init__(self, main_window):
        self.main_window = main_window
        self.maximum_history = deque([], MAX_HIST_SIZE)
        self.population = Population()
        self.avg_history = [] # deque([], DEQUE_SIZE)
        self.max_history = [] # deque([], DEQUE_SIZE)
        self.min_history = [] # deque([], DEQUE_SIZE)
        self.counter = 0
        self.last_dumped_index = 0
        self.x_range = x_range(X_START, X_END)
        self.thread = AutoStep(self)
        self.all_time_max = -999
        self.all_time_max_x = X_START - 9
#        self.thread2 = PieChart(self)
        self.main_window.clear_btn.clicked.connect(self.thread.stop)
#        self.main_window.clear_btn.clicked.connect(self.thread2.stop)
        
        
    def next_step(self):
        if not self.thread.isRunning:
            self.thread.start()
        self.thread.activate('SINGLE_STEP')

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
        self.validateInput()
        self.avg_history.append(self.population.average)
        self.max_history.append(self.population.maximum)
        self.min_history.append(self.population.minimum)
        points = self.population.int_pop
        self.main_window.function_plot.plot_function(self.x_range, self.population.function, points )
        self.main_window.history_plot.plot_history(
            self.max_history,
            self.avg_history,
            self.min_history,
            self.counter - DEQUE_SIZE,
            self.counter)
        self.main_window.pie_plot.plot_pie(self.population)
        
        self.main_window.current_max.setText(str(round(self.population.maximum*10000)/10000))
        self.main_window.current_max_for.setText(str(self.population.maximum_x))
        self.main_window.current_avg.setText(str(round(self.population.average*10000)/10000))
        self.main_window.current_min.setText(str(round(self.population.minimum*10000)/10000))
        self.main_window.current_min_for.setText(str(self.population.minimum_x))
        
    def reset(self):
        self.main_window.clear_btn.clicked.emit()
        self.main_window.next_step_btn.setDisabled(False)
        self.population = Population()
        self.avg_history = [] # deque([], DEQUE_SIZE)
        self.max_history = [] # deque([], DEQUE_SIZE)
        self.min_history = [] # deque([], DEQUE_SIZE)
        self.main_window.history_plot.clearData()
        self.main_window.function_plot.clearData()
        self.main_window.pie_plot.clearData()
        self.main_window.next_step_btn.setDisabled(True)
        self.main_window.start_auto_btn.setDisabled(True)
        self.main_window.apply_btn.setDisabled(False)
        self.main_window.reset_btn.setDisabled(True)
        self.main_window.pop_size.setDisabled(False)
        self.main_window.cross_prob.setDisabled(False)
        self.main_window.mutate_prob.setDisabled(False)
        self.main_window.current_max.setText('')
        self.main_window.current_max_for.setText('')
        self.main_window.current_avg.setText('')
        self.main_window.current_min.setText('')
        self.main_window.current_min_for.setText('')
        self.main_window.max_all_time_label.setText('0')
        self.maximum_history = deque([], MAX_HIST_SIZE)
        self.main_window.found_max.setText("----")
        self.main_window.found_max_for.setText("----")

        self.all_time_max = 0
        self.all_time_max_x = 0
        self.thread.counter = 0
        self.counter = 0
        self.thread.reset()
        
    def stop(self):
        self.main_window.clear_btn.setDisabled(True)
        self.main_window.next_step_btn.setDisabled(False)
        self.main_window.reset_btn.setDisabled(False)
        self.main_window.start_auto_btn.setDisabled(False)

    def start_auto(self):
        self.main_window.clear_btn.setDisabled(False)
        self.main_window.next_step_btn.setDisabled(True)
        self.main_window.start_auto_btn.setDisabled(True)
        self.main_window.reset_btn.setDisabled(True)
        if not self.thread.isRunning:
            self.thread.start()
        self.thread.activate('ENDLESS')
#        if not self.thread2.isRunning:
#            self.thread2.start()
#        self.thread2.activate('ENDLESS')
#        
    def show_more_history(self):
        
        if self.main_window.avg_check.checkState():
            plt.plot(self.avg_history, color='c')
        if self.main_window.max_check.checkState(): 
            plt.plot(self.max_history, color='g')
        if self.main_window.min_check.checkState():
            plt.plot(self.min_history, color='r')
        plt.show()

    def validateInput(self):
        v = self.main_window.pop_size.value()
        if v % 2 != 0:
            self.main_window.pop_size.setValue(v - 1)