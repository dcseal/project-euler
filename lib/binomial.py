# binomial coeffient using Pascals triangle
def binom(n,k):
    """Computes the value of nchoosek(n,k)."""

    if( k < 0 or k > n ):
        return 0

    tmp = 1
    for i in range(1,k+1):
        tmp *= (n-(k-i)) / float( i )
    return int(tmp)

def binomial_modp(n,k,p):

