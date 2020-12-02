from simulatedAnnealingAlgorithm import annealing
from geneticResultFunction import geneticResult
from randomSearchAlgorithm import randomSearch

print("The results of Random Search:        ", randomSearch())
print("The results of Simulated Annealing:  ", annealing())
print("The results of Genetic Algorithm:    ", geneticResult)
print('\n')
print("Where the first component is the minimum of the function, the other 2 are "
      "coordinates of the point at which this minimum is attained")