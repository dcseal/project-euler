import math

def gcd(a,b):
    while( not (b==0) ):
        t = b
        b = a % t
        a = t
    return a

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

#N = 100
N      = 600851475143
primes = get_primes( int(math.sqrt(N) ) )

num = 600851475143
for p in primes:
    while( num%p == 0 ):
        bigp = p
        num  = num/p
        # print('p = %d, num = %d' % (p, num) )

print('Num = %d, Biggest prime divisor = %d' % (N, bigp) )


