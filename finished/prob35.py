import numpy as np

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

def get_permutations(s):
    """Returns a list of all the permutations of string s."""
  
    if( len( s ) ==  1 ):
        perms = s[0]
    else:
        perms = ''
    for n in range( len(s)-1 ):
        perms += s[n] + get_permutations( s[:n] + s[n+1:] )
    return ''.join(perms)

def is_circ(p):
    for s in get_permutations(p):
        if( not is_prime(s) ):
            return False
    return True

def eval_string(x):
    return np.dot( x[::-1], 10**np.arange(len(x)) )

s = 'abc'
print('string s = ', s )
perms = get_permutations(s)
print( perms )

'''
N = 100
primes      = get_primes(N)
circ_primes = []

for p in primes:
    if( is_circ(p) ):
        circ_primes.append(p)
print( circ_primes )
'''

