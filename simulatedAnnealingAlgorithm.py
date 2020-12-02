import numpy as np

Tmin = 1
Tmax = 100  # initial
multiplier = 0.99
xMin = -30
xMax = 30
yMin = -10
yMax = 10


def newX(x):
    randNum = np.random.uniform(xMin, xMax)
    if ((x + randNum >= xMin) and (x + randNum <= xMax)):  # to avoid extending beyond
        x += randNum
    else:
        x -= randNum
    return x


def newY(y):
    randNum = np.random.uniform(yMin, yMax)
    if ((y + randNum >= yMin) and (y + randNum <= yMax)):  # to avoid extending beyond
        y += randNum
    else:
        y -= randNum
    return y

def candidateAcceptance(diffE, t):
    if (diffE <= 0):
        return True
    else:
        p = pow(np.e, (-diffE / t))
        randNum = np.random.uniform(0, 1)
        if (randNum <= p):
            return True
        else:
            return False


def Energy(x, y):
    return -x * (np.sin(np.sqrt(abs(x)))) + y * np.cos(np.sqrt(abs(y)))


def annealing():
    T = Tmax
    currentStateX = np.random.uniform(xMin, xMax)
    currentStateY = np.random.uniform(yMin, yMax)
    currentEnergy = Energy(currentStateX, currentStateY)
    bestStateX = currentStateX
    bestStateY = currentStateY
    bestEnergy = Energy(bestStateX, bestStateY)

    while (T > Tmin):
        searchingCandidate = True
        while (searchingCandidate):
            testStateX = newX(currentStateX)
            testStateY = newY(currentStateY)
            testEnergy = Energy(testStateX, testStateY)
            diffE = testEnergy - currentEnergy
            if candidateAcceptance(diffE, T):
                currentStateX = testStateX
                currentStateY = testStateY
                currentEnergy = Energy(currentStateX, currentStateY)
                T = T * multiplier
                if (currentEnergy < bestEnergy):
                    bestEnergy = currentEnergy
                    bestStateX = currentStateX
                    bestStateY = currentStateY
                searchingCandidate = False

    return bestEnergy, bestStateX, bestStateY
