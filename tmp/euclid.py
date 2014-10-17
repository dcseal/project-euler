def gcd(m,n):
    """Direct implementation of the euclidean algorithm.  This is based on the
    fact that whenever m = nq + r, then gcd(m,n) = gcd(n,r).  The reason this
    method works is that in each iteration, the pair of numbers get smaller.
    That is, since r is smaller than m, the pair (n,r) will be smaller.
    """

    if( m < 0 ):
        m = -m
    if( n < 0 ):
        n = -n

    while( not (n == 0 ) ):

        tmp = n
        n   = m % n
        m   = tmp

    return m

def extended_gcd(a,b):
    """Reverse the steps in the Euclidean algorithm.  This method starts with
    the last two rows in your table, and reverses each step by adding in
    remainders every step of the way.
    
    This routine returns (lastx,lasty) in the equation
    
        gcd(a,b) = lastx * a + lasty * b.
    """

    x = 0
    lastx = 1
    y = 1
    lasty = 0
    while( not (b==0) ):
        q = a / b
        (a,b) = (b, a%b)
        (x,lastx) = (lastx - q*x, x )
        (y,lasty) = (lasty - q*y, y )

    return (lastx, lasty)

if __name__=='__main__':
   
    # This should at least pass these tests
    bignum = 100
    for n in range(2,bignum):
        for m in range(2,bignum):
            (k,l) = extended_gcd(m,n)
            assert( k*m + l*n == gcd(m,n) )

    # compute the inverse for 19 and 141
    (junk, inv19) = extended_gcd(141,19)
    assert( 19*inv19 % 141 == 1 )
    print 'the inverse for 19 in Z_{141} = ', inv19
    print 19*inv19


