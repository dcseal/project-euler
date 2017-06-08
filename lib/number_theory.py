#!/usr/bin/env python
'''This module is supposed to describe commonly used operations from number
theory'''

def gcd(a,b):
    """ Returns the gcd of two numbers using the Euclidean algorithm."""

    x = abs( a )
    y = abs( b )
    while( y != 0 ):
        (q,r) = divmod(x,y)
        x = y
        y = r
    return x

def extended_gcd(a, b):
    """Return the coefficients in 
        gcd(a,b) = lx * a + ly * b 
    from the euclidean algorithm.
    """
    (x,lx) = (0,1)
    (y,ly) = (1,0)
    while( b != 0 ):
        (q,r)   = divmod(a,b)
        (a, b)  = (b, r )
        (x, lx) = (lx - q*x, x)
        (y, ly) = (ly - q*y, y)       
    return (lx, ly)


def get_inv(a,m):
    """Returns ainv in Z / mZ if ainv exists.  Otherwise returns 0.  This means
    that a * ainv \congruent 1 (mod m)."""

    d = gcd(m,a)
    if( not ( d == 1 ) ):
        return 0

    (ainv,junk) = extended_gcd(a,m)
    return ainv

def find_root(M,n):
    """This function returns a integer value x, such that x**n <= M <
    (x+1)**n"""

    high = 1
    while( (high)**3 < M ):
        high = 2*high
    low = high/2

    while low < high:
        mid = (low + high) / 2
        if low < mid and mid**n < M:
            low = mid
        elif high > mid and mid**n > M:
            high = mid
        else:
            return mid
    return mid + 1

def solve_system(avec,mvec):
    """This function solves the system x \congruent avec[k] mod mvec[k], where
    avec and mvec are specified by a list of integers, using the constructive 
    proof of the chinese remainder theorem.  The solution is written in terms 
    of x mod (prod(m))."""

    # quick error check
    for i in range( len(mvec) ):
        for j in range(i+1,len(mvec)):
            if( gcd( mvec[i], mvec[j] ) != 1 ):
                print 'the system is not relatively prime, returning garbage'
                return 0

    if( len(mvec) != len(avec) or len(avec) < 2 ):
        print 'bad system being presented.  returning garbage'
        return 0

    n = len( avec )
    assert( n == len(mvec) )

    # Compute the big product we're going to mod out by
    m = 1
    for k in range(n):
        m = mvec[k]*m

    # Compute each of the M[k]'s, M[k] = m / m[k], and their inverses
    M = []
    yvec = []
    for k in range(n):
        tmp = 1
        for j in range(n):
            if( j == k ):
                continue
            tmp = tmp * mvec[j]

        M.append(tmp)
        yvec.append( get_inv(M[k],mvec[k]) )

    # solution is \sum y[k] * M[k] * a[k], where M[k] = prod(m) / m[k].
    x = 0
    for k in range( n ):
        x = (x + yvec[k]*(M[k])*avec[k]) % m
    return x

def is_prime(n,primes):

    import math

    n = abs(n)
    sqrtn = math.sqrt(n)
    for p in primes:
        if( p > sqrtn ):
            return True
        if( n%p == 0 ):
            return False
    return True

def prime_sieve(N):
    """Returns a list of all primes smaller than N.
    
    TODO - rewrite this to use a prime sieve.
    """

    return 0

if __name__=='__main__':
    '''This simply tests the solve_system problem ... more tests should surely
    be written'''

    m = [5,7,9]
    a = [0,0,0]
    assert( solve_system(a,m) == 0 )

    a = [1,1,1]

    x = solve_system(a,m)
    for n in range( len(a) ):
        assert( x%m[n] == a[n] )

    m = [3,5,8]
    a = [1,3,0]
    x = solve_system(a,m)
    for n in range( len(a) ):
        assert( x%m[n] == a[n] )

    m = [3,5,7,11,13,45]
    a = [1,1,1,1,1,1]
    x = solve_system(a,m)
    if( x > 0 ):
        for n in range( len(a) ):
            print x
            print m[n]
            print a[n]
            assert( x%m[n] == a[n] )

    m = [3,5,7,11,13]
    a = [1,1,1,1,1]
    x = solve_system(a,m)
    if( x > 0 ):
        for n in range( len(a) ):
            assert( x%m[n] == a[n] )

    from random import randint
    a = []
    for n in range( len(m) ):
        a.append( randint(0,2**30) % m[n] )
    x = solve_system(a,m)

    print x
    for n in range( len(a) ):
        assert( x%m[n] == a[n] )

