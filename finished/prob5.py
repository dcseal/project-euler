def gcd(a,b):
    while( not (b==0) ):
        t = b
        b = a % t
        a = t
    return a

def lcm(a,b):
    """Returns the least common multiple of a pair of numbers."""
    return (a*b) / gcd(a,b)


N   = 20
num = 1
for n in range(2,N): 
    num = lcm(num,n)
print('num = %d\n' % num )
