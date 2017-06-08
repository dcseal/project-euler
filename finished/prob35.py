import numpy as np
import math

def is_prime(n,primes):
    """Check if a number is prime."""

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

def is_circ(p):
    """Check if a prime p is a circular prime.  It is assumed that p is of
    type int when it is passed in here."""

    perms = get_circ_permutations(str(p))
    for s in perms:
        if( not is_prime( int(s), primes ) ):
            return False
    return True

def get_circ_permutations(s):
    """Returns a list of all the 'circular' permutations of s."""

    perms = []
    for n in range( len(s) ):
        perms.append( s[n:] + s[:n] )
    return perms

def get_permutations(s):
    """Returns a list of all the permutations of string s. (Not use for this
    code, but I could see how this could be useful in the future!)"""

    import itertools
    perms = [''.join(r) for r in itertools.permutations(str(s))]
    return list( set( perms ) )

    """
    if( len( s ) ==  1 ):
        perms = s[0]
    else:
        perms = ''
    for n in range( len(s)-1 ):
        perms += s[n] + get_permutations( s[:n] + s[n+1:] )
    return ''.join(perms)
    """

'''
def eval_string(x):
    return np.dot( x[::-1], 10**np.arange(len(x)) )

s = 'abc'
print('string s = ', s )
perms = get_permutations(s)
print( perms )
'''

# testing code (for the suggested test case that they gave)
N = 100
primes      = get_primes(N)
circ_primes = []

for p in primes:
    if( is_circ( p ) ):
        circ_primes.append(p)
print( circ_primes )

# Code segment for the actual problem that they give
N = 1000000
primes = get_primes(N)
circ_primes = []
for p in primes:
    if( is_circ( p ) ):
        circ_primes.append(p)
print('There are %d circular primes smaller than %d\n' % (len(circ_primes), N))

# print( is_circ(197) )

