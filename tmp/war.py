#!/usr/bin/env python

import random
from copy import copy
from collections import deque

def pretty_print( hand ):
    """This function prints the contents of a hand to standard output"""

    # Dictionary describing card values
    dt = {}
    for n in range(9):
        dt[ n ] = str( n+2 )
    dt[9]  = 'Jack'
    dt[10] = 'Queen'
    dt[11] = 'King'
    dt[12] = 'Ace'

    dt[8]  = 'T'
    dt[9]  = 'J'
    dt[10] = 'Q'
    dt[11] = 'K'
    dt[12] = 'A'

    for c in hand:
        print '%s ' % (dt[c]), 
    print


def main():
    """Main program.

    This program plays the card game war against two players."""

    # user options
    debug = False
    shuff = True
    total_num_cards = 52
    num_suits       = 4

    # Create all the cards in the deck
    suit = range( int( total_num_cards / num_suits ) )
    deck = []
    for n in range( num_suits ):
        deck.extend( suit )
    random.shuffle( deck )

    # Create the two hands of cards
    A = deque()
    B = deque()

    # create a forced position, this gives a 'huge' number of fights
#   deck = []
#   A =  deque([8, 4, 2, 7, 8, 1, 9, 2, 5, 3, 9, 10, 2, 6, 6, 10, 0, 5, 5, 2, 9, 1, 7, 9, 12, 1])
#   B =  deque([7, 12, 8, 8, 11, 4, 1, 3, 10, 3, 5, 6, 3, 10, 11, 11, 0, 4, 11, 6, 0, 4, 12, 0, 7, 12])

    A0 = copy( A )
    B0 = copy( B )
    assert( A0 == A and B0 == B )

    has_cards = True
    while( has_cards ):

        try: 
            A.append( deck.pop() )
            B.append( deck.pop() )

        except IndexError:
            has_cards = False

    print 'Before popping a card, the hands look like:'

    print "\tA's hand has all the cards:"
    pretty_print( A )
    print "\tB's hand has all the cards:"
    pretty_print( B )

    numwars = 0
    
    minA    = len(A)
    minB    = len(B)

    maxfights = 500000
    numfights = 0
    while( len(A) > 0 and len(B) > 0  ):

        if( (A == A0 and B == B0) or ( A == B0 and B == A0 ) ):
            if( numfights > 0 ):
                print 'you die'
                break

        if( numfights % 2 == 0 ):
            A0 = copy( A )
            B0 = copy( B )
            print '  numfights = %1.3e, minA = %d, minB = %d' % (numfights, minA, minB) 

        # new fight, reset the buffer
        buf = []
        numfights = numfights + 1

        minA = min( len(A), minA )
        minB = min( len(B), minB )

        assert ( len(A) + len(B) == total_num_cards )
        while( 1 ):

            try:
                a = A.popleft()
                b = B.popleft()
            except IndexError:
                'somebody needs to be declared a winner!'
                break

            buf.extend( [a, b] )
            if( shuff ):
                random.shuffle( buf )

            if( a == b ):

                numwars = numwars + 1
                for n in range(3):

                    try:
                        a = A.popleft()
                        b = B.popleft()
                    except IndexError:
                        'somebody needs to be declared a winner!'
                        break

                    buf.append( a )
                    buf.append( b )

                if( debug ):
                    print 'War!  The buffer has the cards', buf

            elif( a < b ):
                if( debug ):
                    print 'extending B with', buf
                B.extend( buf )
                break

            else:
                if( debug ):
                    print 'extending A with', buf
                A.extend( buf )
                break

    minA = min( len(A), minA )
    minB = min( len(B), minB )

    if( numfights >= maxfights ):
        print 'numfights = %d was huge!' % numfights
        pretty_print( A )
        pretty_print( B )

    if( len(A) > 0 and len(B) == 0 ):
        print '************ A wins! *********'
    elif( len(B) > 0 and len(A) == 0 ):
        print '************ B wins! *********'
    else:
        print 'nobody is a winner!'
        pretty_print( A )
        pretty_print( B )

    print '\tThere were %d wars and %d fights.' % (numwars, numfights)
    print '\tMinimum cards A had were %d ' % minA
    print '\tMinimum cards B had were %d ' % minB

if __name__ == '__main__':
    main()
