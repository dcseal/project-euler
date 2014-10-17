import numpy as np

N = 101
x = np.arange(N)
print( sum( x**2 ) )
print( sum(x)**2   )
print('diff = ', sum(x)**2 - sum( x**2 ) ) 
