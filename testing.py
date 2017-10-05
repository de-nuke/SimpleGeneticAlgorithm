# -*- coding: utf-8 -*-

import random
from GeneticAlgorithm import reproducted, crossed, mutated
from utils import b

#Initial set
#I = [b(random.randrange(0, 42)) for _ in range(100)]
#I = [b(_) for _ in range(5)]
I = [b(_) for _ in [13, 24, 8, 19]]

#Reproducted
R = reproducted(I)

#Crossed
C = crossed(R)

#Mutated
print(C)
M = mutated(C, 0.1)
print(M)