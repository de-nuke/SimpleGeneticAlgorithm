# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 21:34:51 2017

@author: Dom
"""

from PyQt5.QtWidgets import QGraphicsEllipseItem
from PyQt5 import QtGui
from PyQt5 import QtCore

def b(value, num_of_digits=6):
    return ("{:0"+str(num_of_digits)+"b}").format(value)

def neg_char(c):
    '''
    c should be '0' or '1'. 
    '0' -> '1'
    '1' -> '0'
    
    If c is neither '0' nor '1', functions return unchanged c
    '''
    
    if c is '0' or c is '1':
        return str(abs(1-int(c)))
    else:
        return c
    
def radius(creature, minimum, maximum):
    min_radius = 5
    max_radius = 30
    radius_range = max_radius - min_radius
    
    creature_range = maximum - minimum
    
    x = creature_range / radius_range
    
    
    
    return int(creature, 2)

def color(x, z, y):
        return (0, int(x, 2)+150, 0)
    
class Circle(QGraphicsEllipseItem):
    def __init__(self, x, y, r=10, fill_color=(255,255,255), border_color=(0,0,0)):
        super(Circle, self).__init__(x, y, r,r)
        self.setPen(QtGui.QPen(QtGui.QColor(*border_color), 2, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap))
        self.setBrush(QtGui.QBrush(QtGui.QColor(*fill_color), style=QtCore.Qt.SolidPattern))

        
        