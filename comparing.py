from simulatedAnnealingAlgorithm import annealing
from geneticResultFunction import genetic
from randomSearchAlgorithm import randomSearch

print("The results of Random Search:        ", randomSearch())
print("The results of Simulated Annealing:  ", annealing())
print("The results of Genetic Algorithm:    ", genetic())
print('\n')
print("Where the first component is the minimum of the function, the other 2 are "
      "coordinates of a point at which this minimum is attained")
print('\n')
print("Comparison table:\n")
print("Random Search\t\t\t\t", "Simulated Annealing\t\t", "Genetic Algorithm")
for i in range(0,10):
      print(f'{randomSearch()[0]:.{12}f}', '\t\t\t', f'{annealing()[0]:.{12}f}', '\t\t\t', f'{genetic()[0]:.{12}f}')

