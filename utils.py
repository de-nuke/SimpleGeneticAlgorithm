# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 21:34:51 2017

@author: Dom
"""

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