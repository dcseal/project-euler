def fib(n):
    return fib(n-1) + fib(n-2)

MAX_N = 4e6

tmp1 = 1;  tmp2 = 2;  f = 0
s    = 2

while( f < MAX_N ):

    # find the next term in the sequence:
    f    = tmp1 + tmp2
    tmp1 = tmp2
    tmp2 = f

    if( not f % 2 ):
        s += f

print( ' sum = %d ' % s )
