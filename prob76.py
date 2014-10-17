from lib.binomial import binom

def num_solns( n, k ):
    """Sum = n, we're allowed to use grouping up to and including k."""

    if( n < 2 or k < 1 ):
        return 0
    if( k == 1 ):
        return 1

    tmp = 0
    for m in range( n ):

        # select m units to group: 
        tmp += num_solns( n - m*k, k-1 )

    return tmp
