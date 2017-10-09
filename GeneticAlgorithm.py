# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 22:09:59 2017

@author: Dom
"""
from numpy.random import choice
import random
from utils import neg_char, b
import numpy as np

def tmp_fun(x):
    return -0.1 * x**2 + 4 * x + 7
    #return x**2

def _should_cross(cross_probability):
    return choice([True, False], 1, p=[cross_probability, 1-cross_probability])[0]


class Population(object):
    '''
    population - set of binary numbers
    creature - one number from "population" set
    gene - one bit in in binary number (creature)
    
    '''
    def __init__(self, population_size=0, crossing_probability=1, mutation_probability=0.1, function=lambda x: x):
        self.population = np.array([b(random.randrange(-1, 42)) for x in range(population_size)])
        self.function = function
        self.size = population_size
        self.int_pop = [int(x,2) for x in self.population]
        self.creature_size = len(self.population[0]) if len(self.population) else 0
        self.crossing_probability = crossing_probability
        self.mutation_probability =  mutation_probability
         
        
    def reproduct(self):
        roulette, expected_num_of_copies = {}, {}
        n = self.size
        self.int_pop = [int(x,2) for x in self.population]
        
        values = [self.function(creature) for creature in self.int_pop]
        for i, creature in enumerate(self.population):
            roulette[creature] = values[i] / sum(values)
            expected_num_of_copies[creature] = roulette[creature] * n   
        self.population = choice(self.population, n, p=[roulette[creature] for creature in self.population]) 
        
        return self
    
    def cross(self, crossing_probability=None):
        l = self.creature_size
        pairs = [] #list of 2-item tuples
        
        crossing_probability = crossing_probability if crossing_probability else self.crossing_probability
        tmp_items = list(self.population.copy())
        
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
                if self.function(int(new_1, 2)) > 0 :
                    crossed.append(new_1)
                else:
                    crossed.append(old_1)
                if self.function(int(new_2, 2)) > 0:
                    crossed.append(new_2)
                else:
                    crossed.append(old_2)
            else:
                crossed.append(old_1)
                crossed.append(old_2)
                
        self.population = np.array(crossed)
        self.int_pop = [int(x,2) for x in self.population]
        return self
    
    def mutate(self, mutation_probability=None, mutation_type = 'NEGATION'):
        '''
        Assuming that mutation is a negation of random bit
        '''
        mutation_probability = mutation_probability if mutation_probability else self.mutation_probability
        
        do_mutation = choice([True, False], 1, p=[mutation_probability, 1-mutation_probability])[0]
        if do_mutation:
            if mutation_type == 'NEGATION':
                creature_index = random.randrange(0,self.size)
                old_creature = self.population[creature_index]
                position = random.randrange(0,self.creature_size)
                gene_to_mutate = old_creature[position]
                new_gene = neg_char(gene_to_mutate)
                new_code = old_creature[:position] + new_gene + old_creature[position+1:]
                if int(new_code, 2) <= 41 and int(new_code, 2) >= -1:
                    self.population[creature_index] = new_code
                    
        self.int_pop = [int(x,2) for x in self.population]            
        return self
    
    def dump(self):
        return str(self.population)

    @property
    def minimum(self):
        return min([self.function(creature) for creature in self.int_pop])
    
    @property
    def maximum(self):
        return max([self.function(creature) for creature in self.int_pop])
    
    @property
    def average(self):
        values = [self.function(creature) for creature in self.int_pop]
        return sum(values)/ len(values)

    def setFunction(self, f):
        self.function = f







#def reproducted(initial_set, function=tmp_fun):
#    roulette, expected_num_of_copies = {}, {}
#    n = len(initial_set)
#
#    values = [function(int(code, 2)) for code in initial_set]
#    for i, code in enumerate(initial_set):
#        roulette[code] = values[i] / sum(values)
#        expected_num_of_copies[code] = roulette[code] * n
#        
#    new_set = choice(initial_set, n, p=[roulette[code] for code in initial_set])
#        
#    return list(new_set)
#
#def crossed(repr_set, crossing_probability=0.01):
#    l = len(repr_set[0])
#    pairs = [] #list of 2-item tuples
#    
#    tmp_items = repr_set.copy()
#    
#    def pop_random(items):
#         idx = random.randrange(0, len(items))
#         return items.pop(idx)
#     
#    while len(tmp_items) > 1:
#        r1 = pop_random(tmp_items)
#        r2 = pop_random(tmp_items)
#    
#        pairs.append((r1,r2))
#
#    
#    crossed = []
#    for old_1, old_2 in pairs:
#        if _should_cross(crossing_probability):
#            k = random.randrange(1,l)
#            new_1, new_2 = old_1[:k] + old_2[k:], old_2[:k] + old_1[k:]
#            crossed.append(new_1)
#            crossed.append(new_2)
#        else:
#            crossed.append(old_1)
#            crossed.append(old_2)
#    return crossed
#
#def mutated(crossed_set, mutation_probability=0.001, mutation_type='NEGATION'):
#    '''
#    Assuming that mutation is a negation of random bit
#    '''
#    if choice([True, False], 1, p=[mutation_probability, 1-mutation_probability])[0]:
#        if mutation_type == 'NEGATION':
#            code_index = random.randrange(0,len(crossed_set))
#            old_code = crossed_set[code_index]
#            position = random.randrange(0,len(old_code))
#            gene_to_mutate = old_code[position]
#            new_gene = neg_char(gene_to_mutate)
#            new_code = old_code[:position] + new_gene + old_code[position+1:]
#        crossed_set[code_index] = new_code
#    return crossed_set
#    