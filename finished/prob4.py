def is_palindrome( num ):
    """Checks to see if n is a palindrome."""

    s = str(num)
    for n in range( len(s) ):
        if( not s[n] == s[len(s)-n-1] ):
            return False
    return True

digits = 1000
maxpal = 1
for n in range( digits, 0, -1 ):
    for m in range( digits, 0, -1 ):
        if( is_palindrome( n*m ) ):
            maxpal = max( maxpal, n*m )
print('Maximum palindrom = %d\n' % maxpal )
