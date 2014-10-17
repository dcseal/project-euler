from poker import Card, PokerHand

# test a hand with two identical Straight flushes:
filename = 'straight_flush.txt'
f = open( filename, 'r' )
for line in f.readlines():

    s = line.rsplit()
    assert( len(s) == 10 )
    p1 = PokerHand( s[:5] )
    p2 = PokerHand( s[5:] )

    print('p1 = ')
    p1.print_hand()
    print(p1._hand_type)

    print('p2 = ')
    p2.print_hand()
    print(p2._hand_type)

    assert( p1._hand_type == 'Straight Flush' and p2._hand_type == 'Straight Flush' )
    print( 'p1 < p2 returns:' )
    print( p1 < p2 )


f.close()

# test two hands with four of a kind:
# test a hand with two identical Straight flushes:
filename = 'four_of_a_kind.txt'
f = open( filename, 'r' )
for line in f.readlines():

    s = line.rsplit()
    assert( len(s) == 10 )
    p1 = PokerHand( s[:5] )
    p2 = PokerHand( s[5:] )

    print('p1 = ')
    p1.print_hand()
    print(p1._hand_type)

    print('p2 = ')
    p2.print_hand()
    print(p2._hand_type)

    assert( p1._hand_type == 'Four of a Kind' and p2._hand_type == 'Four of a Kind' )
    print( 'p1 < p2 returns:' )
    print( p1 < p2 )


f.close()

# test two hands with two-pair each
filename = 'two_pair.txt'
f = open( filename, 'r' )
for line in f.readlines():

    s = line.rsplit()
    assert( len(s) == 10 )
    p1 = PokerHand( s[:5] )
    p2 = PokerHand( s[5:] )

    print('p1 = ')
    p1.print_hand()
    print(p1._hand_type)

    print('p2 = ')
    p2.print_hand()
    print(p2._hand_type)

    assert( p1._hand_type == 'Two Pair' and p2._hand_type == 'Two Pair' )
    print( 'p1 < p2 returns:' )

    bol = p1 < p2
    assert( bol )


f.close()


