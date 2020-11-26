import numpy as np
from algorithm import *

ch1 = Chromosome(30, 10)
ch2 = Chromosome(10, 0)
ch3 = Chromosome(-20, 7.5)
ch4 = Chromosome(-25, 10)

pop0 = Population(0)
pop0.add_chromosome(ch1)
pop0.add_chromosome(ch2)
pop0.add_chromosome(ch3)
pop0.add_chromosome(ch4)

pop0.selection()
afterSelection = pop0.get_chromosomeList()
for i in afterSelection:
    print(i.get_info())
print()

pop0.best_to_worst_order()
newOrder = pop0.get_chromosomeList()
for i in newOrder:
    print(i.get_info())
print()

print(pop0.best_chromosome_after_selection().get_info(), '\n')

pop0.crossover()
afterCrossover = pop0.get_chromosomeList()
for i in afterCrossover:
    print(i.get_info())
print()

pop0.mutations()
afterMutations = pop0.get_chromosomeList()
for i in afterMutations:
    print(i.get_info())
print()

pop0.set_random_chromosomeList(-30,30,-10,10)
afterRand = pop0.get_chromosomeList()
for i in afterRand:
    print(i.get_info())
print()