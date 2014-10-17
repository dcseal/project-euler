def gcd(m,n):
    # this hinges on the fact that:
    #   gcd(m,n) = gcd(n,r) whenever m = nq + r
    #

    m = abs(m)
    n = abs(n)

    r = m%n
    while( r != 0 ):
        (n,r) = divmod(m,n)
        m = n
    return n 

