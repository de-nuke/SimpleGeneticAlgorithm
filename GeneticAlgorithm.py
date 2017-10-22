# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 22:09:59 2017

@author: Dom
"""
from numpy.random import choice
import random
from utils import neg_char, to_b, to_dec
import numpy as np

def tmp_fun(x):
    return -0.1 * x**2 + 4 * x + 7
    #return x**2

def _should_cross(cross_probability):
    return choice([True, False], 1, p=[cross_probability, 1-cross_probability])[0]

MUTATION_TYPE = 'NEGATION'

X_START = -1
X_END = 41

OFFSET = -X_START

class Population(object):
    '''
    population - set of binary numbers
    creature - one number from "population" set
    gene - one bit in in binary number (creature)
    
    '''
    def __init__(self, population_size=0, crossing_probability=1, mutation_probability=0.1, function=lambda x: x, mutation_type=MUTATION_TYPE):
        self.population = np.array([to_b(random.SystemRandom().randrange(-1, 42), OFFSET) for x in range(population_size)])
        self.function = function
        self.size = population_size
        self.int_pop = [to_dec(x, OFFSET) for x in self.population]
        self.creature_size = len(self.population[0]) if len(self.population) else 0
        self.crossing_probability = crossing_probability
        self.mutation_probability = mutation_probability
        self.mutation_type = mutation_type
        
    def reproduct(self):
        roulette, expected_num_of_copies = {}, {}
        n = self.size
        self.int_pop = [to_dec(x, OFFSET) for x in self.population]
        
        values = [self.function(creature) for creature in self.int_pop]
        for i, creature in enumerate(self.population):
            roulette[creature] = values[i] / sum(values)
            expected_num_of_copies[creature] = roulette[creature] * n
        probabilities = [roulette[creature] for creature in self.population]
        self.population = choice(self.population, n, p=probabilities) 

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
        
            pairs.append((r1, r2))
        
        crossed = []
        for old_1, old_2 in pairs:
            if _should_cross(crossing_probability):
                k = random.randrange(1,l)
                new_1, new_2 = old_1[:k] + old_2[k:], old_2[:k] + old_1[k:]
                if self.function(to_dec(new_1, OFFSET)) > 0:
                    crossed.append(new_1)
                else:
                    crossed.append(old_1)
                if self.function(to_dec(new_2, OFFSET)) > 0:
                    crossed.append(new_2)
                else:
                    crossed.append(old_2)
            else:
                crossed.append(old_1)
                crossed.append(old_2)
        self.population = np.array(crossed)
        self.int_pop = [to_dec(x, OFFSET) for x in self.population]
        return self

    def mutate(self, mutation_probability=None):
        tmp_pop = self.population.copy()
        mutation_probability = mutation_probability if mutation_probability else self.mutation_probability
        for index, creature in enumerate(tmp_pop):
            # print("Zaczynam mutować: " + creature + ", czyli: " + str(to_dec(creature, OFFSET)))
            new_creature = to_b(X_END + 99, OFFSET)
            # print("Wyszło mi: " + new_creature + ", czyli: " + str(to_dec(new_creature, OFFSET)))
            muted = False
            while to_dec(new_creature, OFFSET) < X_START or to_dec(new_creature, OFFSET) > X_END:
                # print("Robie jeszcze raz")
                new_creature = creature
                for i, gene in enumerate(creature):
                    if random.uniform(0, 1) <= mutation_probability:
                        bit = neg_char(gene)
                        muted = True
                    else:
                        bit = gene
                    new_creature = new_creature[:i] + bit + new_creature[i+1:]
                # if muted:
                    # print("UWAGA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print(creature, ' = ', str(to_dec(creature, OFFSET)), 'muted? ', muted, ' po mutacji: ', new_creature)
                # print("Wyszło mi: " + new_creature + ", czyli: " + str(to_dec(new_creature, OFFSET)))
            # print("Teraz jest dobrze! Idę dalej")
            self.population[index] = new_creature

        self.int_pop = [to_dec(x, OFFSET) for x in self.population]
        return self

    # def mutate(self, mutation_probability=None):
    #     '''
    #     Assuming that mutation is a negation of random bit
    #     '''
    #     mutation_probability = mutation_probability if mutation_probability else self.mutation_probability
    #     do_mutation = choice([True, False], 1, p=[mutation_probability, 1-mutation_probability])[0]
    #     if do_mutation:
    #         if self.mutation_type == 'NEGATION':
    #             creature_index = random.randrange(0,self.size)
    #             old_creature = self.population[creature_index]
    #             position = random.randrange(0,self.creature_size)
    #             gene_to_mutate = old_creature[position]
    #             new_gene = neg_char(gene_to_mutate)
    #             new_creature = old_creature[:position] + new_gene + old_creature[position+1:]
    #             if int(new_creature, 2) <= 41 and int(new_creature, 2) >= -1:
    #                 self.population[creature_index] = new_creature
    #         elif self.mutation_type == 'EXCHANGE':
    #             creature_index = random.randrange(0,self.size)
    #             old_creature = self.population[creature_index]
    #             position1 = random.randrange(0,self.creature_size)
    #             position2 = random.randrange(0,self.creature_size)
    #             while position2 == position1:
    #                 position2 = random.randrange(0,self.creature_size)
    #
    #             gene1 = old_creature[position1]
    #             gene2 = old_creature[position2]
    #             old_creature = old_creature[:position1] + gene1 + old_creature[position1+1:]
    #             new_creature = old_creature[:position2] + gene2 + old_creature[position2+1:]
    #
    #             if int(new_creature, 2) <= 41 and int(new_creature, 2) >= -1:
    #                 self.population[creature_index] = new_creature
    #
    #     self.int_pop = [int(x,2) for x in self.population]
    #     return self
    
    def dump(self):
        return str(self.population)

    @property
    def values(self):
        return [self.function(creature) for creature in self.int_pop]

    @property
    def minimum(self):
        return min(self.values)
    
    @property
    def minimum_x(self):
        return self.int_pop[self.values.index(self.minimum)]
    
    @property
    def maximum(self):
        return max(self.values)
    
    @property
    def maximum_x(self, for_max=None):
        return self.int_pop[self.values.index(self.maximum)]

    def maximum_x_for(self, for_max):
        return self.int_pop[self.values.index(for_max)]

    @property
    def average(self):
        return sum(self.values)/ len(self.values)

    def setFunction(self, f):
        self.function = f

