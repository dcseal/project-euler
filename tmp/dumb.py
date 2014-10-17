
def fast_exp(a,n,m):

    tmp = 1
    for j in range(n):
        tmp = ( tmp * a ) % m

    return tmp


