import math

def is_prime(n,primes):

    n = abs(n)
    sqrtn = math.sqrt(n)
    for p in primes:
        if( p > sqrtn ):
            return True
        if( n%p == 0 ):
            return False
    return True

def get_primes(N):
    """Returns a list of all primes smaller than N."""

    primes = []
    for n in range(2, N ):
        if( is_prime(n, primes) ):
            primes.append(n)
    return primes

N = 10001
primes = [2]
while( len(primes) < N ):
    primes = get_primes( 2*primes[len(primes)-1] )

print('The %dth prime = %d ' % (N, primes[N-1]) )

