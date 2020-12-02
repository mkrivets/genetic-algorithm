from geneticAlgorithm import *

accuracy = 0.001
previousBestFitness = 100  # random, it doesn't matter
ch = Chromosome(0, 0)
previousBestChromosome = ch  # random, it doesn't matter

# initial population
pop = Population(0)
pop.set_random_chromosomeList(ch.xMin, ch.xMax, ch.yMin, ch.yMax)
pop.selection()
currentBestFitness = pop.best_chromosome_after_selection().fitness()
currentBestChromosome = pop.best_chromosome_after_selection()
pop.crossover()
pop.mutations()
chromosomeListActual = pop.get_chromosomeList()

k = 0
while (abs(currentBestFitness - previousBestFitness) > accuracy):
    previousBestFitness = currentBestFitness
    previousBestChromosome = currentBestChromosome
    k += 1
    pop = Population(k)
    pop.add_chromosomeList(chromosomeListActual)
    pop.selection()
    currentBestFitness = pop.best_chromosome_after_selection().fitness()
    currentBestChromosome = pop.best_chromosome_after_selection()
    pop.crossover()
    pop.mutations()
    chromosomeListActual = pop.get_chromosomeList()

geneticResult = currentBestFitness

print("The extremum (minimum) of our function is:", geneticResult)
print("The coordinates in which we reach the minimum: ({0}, {1})".format(currentBestChromosome.X,
                                                                         currentBestChromosome.Y))
print("The number of the population: ", k)
