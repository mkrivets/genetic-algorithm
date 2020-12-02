import numpy as np

accuracy = 0.01
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


def Func(x, y):
    return -x * (np.sin(np.sqrt(abs(x)))) + y * np.cos(np.sqrt(abs(y)))


def randomSearch():
    currentX = np.random.uniform(xMin, xMax)
    currentY = np.random.uniform(yMin, yMax)
    currentFunc = Func(currentX, currentY)
    previousFunc = 0

    while (abs(currentFunc - previousFunc) > accuracy):
        previousX = currentX
        previousY = currentY
        previousFunc = currentFunc
        searchingCandidate = True
        while (searchingCandidate):
            testX = newX(previousX)
            testY = newY(previousY)
            if (Func(testX, testY) < previousFunc):
                currentX = testX
                currentY = testY
                currentFunc = Func(currentX, currentY)
                searchingCandidate = False

    return currentFunc, currentX, currentY
