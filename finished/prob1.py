import numpy as np

N = 1000

x = np.arange(0, N,  3)
y = np.arange(0, N,  5)
z = np.arange(0, N, 15)

total = np.sum( x ) + np.sum(y) - np.sum( z )

print('Sum of all the numbers: ', total)
