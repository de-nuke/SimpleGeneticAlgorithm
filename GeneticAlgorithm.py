# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 22:09:59 2017

@author: Dom
"""
from numpy.random import choice
import random
from utils import neg_char

def tmp_fun(x):
    #return -0.1 * x**2 + 4 * x + 7
    return x**2

def _should_cross(cross_probability):
    return choice([True, False], 1, p=[cross_probability, 1-cross_probability])[0]


def reproducted(initial_set, function=tmp_fun):
    roulette, expected_num_of_copies = {}, {}
    n = len(initial_set)

    values = [function(int(code, 2)) for code in initial_set]
    for i, code in enumerate(initial_set):
        roulette[code] = values[i] / sum(values)
        expected_num_of_copies[code] = roulette[code] * n
        
    new_set = choice(initial_set, n, p=[roulette[code] for code in initial_set])
        
    return list(new_set)

def crossed(repr_set, crossing_probability=0.01):
    l = len(repr_set[0])
    pairs = [] #list of 2-item tuples
    
    tmp_items = repr_set.copy()
    
    def pop_random(items):
         idx = random.randrange(0, len(items))
         return items.pop(idx)
     
    while len(tmp_items) > 1:
        r1 = pop_random(tmp_items)
        r2 = pop_random(tmp_items)
    
        pairs.append((r1,r2))

    
    crossed = []
    for old_1, old_2 in pairs:
        if _should_cross(crossing_probability):
            k = random.randrange(1,l)
            new_1, new_2 = old_1[:k] + old_2[k:], old_2[:k] + old_1[k:]
            crossed.append(new_1)
            crossed.append(new_2)
        else:
            crossed.append(old_1)
            crossed.append(old_2)
    return crossed

def mutated(crossed_set, mutation_probability=0.001, mutation_type='NEGATION'):
    '''
    Assuming that mutation is a negation of random bit
    '''
    if choice([True, False], 1, p=[mutation_probability, 1-mutation_probability])[0]:
        if mutation_type == 'NEGATION':
            code_index = random.randrange(0,len(crossed_set))
            old_code = crossed_set[code_index]
            position = random.randrange(0,len(old_code))
            gene_to_mutate = old_code[position]
            new_gene = neg_char(gene_to_mutate)
            new_code = old_code[:position] + new_gene + old_code[position+1:]
        crossed_set[code_index] = new_code
    return crossed_set
    











