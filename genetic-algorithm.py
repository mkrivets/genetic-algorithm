import numpy as np


class Chromosome:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def fitness(self):
        return -self.X * (np.sin(np.sqrt(abs(self.X)))) + self.Y * np.cos(np.sqrt(abs(self.Y)))

    def get_info(self):
        return self.X, self.Y, self.fitness()

    def gene_X_mutation(self):
        self.X = self.X + np.random.uniform(-1,1)

    def gene_Y_mutation(self):
        self.Y = self.Y + np.random.uniform(-1,1)



class Population:
    def __init__(self, number):
        self.number = number
        self.chromosomeList = []

    def add_chromosome(self, chromosome):
        self.chromosomeList.append(chromosome)

    def get_chromosomes(self):
        return self.chromosomeList

    def worst_chromosome(self):
        maxFitness = self.chromosomeList[0].fitness()
        worst = self.chromosomeList[0]
        for ch in self.chromosomeList:
            if ch.fitness() > maxFitness:
                maxFitness = ch.fitness()
                worst = ch
        return worst

    def selection(self):
        self.chromosomeList.remove(self.worst_chromosome())

    # def crossover


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
afterSelection = pop0.get_chromosomes()
for i in afterSelection:
    print(i.get_info())

