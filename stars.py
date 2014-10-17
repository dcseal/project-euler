from lib.binomial import binom

k = 5
print( sum( [ binom(N+k-1,k) for N in range(k+1) ] ) )


