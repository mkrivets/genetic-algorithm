import numpy as np

min = 100
minX = 0
minY = 0
func = lambda m, k: (-m * (np.sin(np.sqrt(abs(m)))) + k * np.cos(np.sqrt(abs(k))))
for i in np.arange(-30, 30.1, 0.1):
    for j in np.arange(-10, 10.1, 0.1):
        if func(i, j) < min:
            min = func(i, j)
            minX = i
            minY = j
print(min, minX, minY)
