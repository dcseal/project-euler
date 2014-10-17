class Card(object):

    cardvals = {'2':2, '3':3,  '4':4,  '5':5,  '6':6,  '7':7,  '8':8, '9':9, \
                'T':10, 'J':11, 'Q':12, 'K':13, 'A':14 }

    def __init__(self, c):
        self._card_val = Card.cardvals[c[0]]
        self._suit     = c[1]

    def __cmp__(self,other):
        (rank1,rank2) = (self._card_val, other._card_val )
        if( rank1 != rank2 ):
            return( cmp(rank1,rank2) )
        else:
            #print('warning: undefined behavior when comparing suits')
            # TODO - undefined behavior here ...
            return cmp(self._suit,other._suit)

    # ass ton of comparison operaters that need be defined (overloaded)
#   def __eq__(self,other):
#       return( self._card_val == other._card_val )
#   def __ne__(self,other):
#       return( self._card_val != other._card_val )
#   def __lt__(self,other):
#       return self._card_val < other._card_val
#   def __gt__(self,other):
#       return self._card_val > other._card_val
#   def __le__(self,other):
#       return self._card_val <= other._card_val
#   def __ge__(self,other):
#       return self._card_val >= other._card_val


    def print_card(self):

        carddict = {2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', \
                8:'8', 9:'9', 10:'T', 11:'J', 12:'Q', 13:'K', 14:'A' }
        return('%c%c' % (carddict[self._card_val], self._suit) )

class PokerHand(object):

    hand_type_dict = {\
        'Straight Flush'  : 8, \
        'Four of a Kind'  : 7, \
        'Full House'      : 6, \
        'Flush'           : 5, \
        'Straight'        : 4, \
        'Three of a Kind' : 3, \
        'Two Pair'        : 2, \
        'One Pair'        : 1, \
        'High Card'       : 0 }

    def __init__(self, hand ):
        self.hand = hand

        self._cards = [ Card(c) for c in hand ]

        # sort cards in decreasing order:
        self._cards.sort()
        self._cards.reverse()

        self._hand_type = self.define_hand_type()

    def define_hand_type(self):

        if( self._is_straight() and self._is_flush() ):
            return 'Straight Flush'

        if( self._has_quad() ):
            return 'Four of a Kind'

        if( self._has_full_house() ):
            return 'Full House'

        if( self._is_flush() ):
            return 'Flush'

        if( self._is_straight() ):
            return 'Straight'

        if( self._has_triple() ):
            return 'Three of a Kind'

        if( self._has_two_pair() ):
            return 'Two Pair'

        if( self._has_pair() ):
            return 'One Pair'

        return 'High Card'

        # Royal Flush = best straight flush.  This will get fleshed out ...

    def __cmp__(self,other):

        (h1,h2) = (self._hand_type, other._hand_type)

        # check for easy solution first:
        if( h1 != h2 ):
            return ( PokerHand.hand_type_dict[h1] - PokerHand.hand_type_dict[h2])

        # annoying case, need to check for largest card in the hand:
        else:

            # check for hands with a unique identity for 'largest' card:
            if( self._hand_type == 'Four of a Kind' or \
                self._hand_type == 'Full House' or \
                self._hand_type == 'Three of a Kind' ):
                return self._big_card - other._big_card

            # single pair 
            if( self._hand_type == 'One Pair' ):
                p1 = self._has_pair()
                p2 = other._has_pair()
                if(p1!=p2):
                    return p1-p2
                
                n=0
                while( self._cards[n]._card_val != p1 ):
                    n += 1
                return self._cards[n]._card_val - other._cards[n]._card_val


            # simply search for the largest card in hand 
            # (this takes care of two pair as well!)
            n=0
            while( self._cards[n]._card_val == other._cards[n]._card_val ):
                n += 1
            return cmp(self._cards[n], other._cards[n] )


    def print_hand(self):
        print([c.print_card() for c in self._cards])

    def _is_flush(self):
        """Test to see if hand is a flush."""

        for c in self._cards:
            if( not (c._suit == self._cards[0]._suit ) ):
                return False
        return True

    def _is_straight(self):
        cards = self._cards
        for n in range( len( self._cards )-1 ):
            if( not( cards[n+1]._card_val-cards[n]._card_val == -1 ) ):
                return False
        return True

    def _has_pair(self):
        """Returns the value of the largest pair the card owner has."""

        cards = self._cards
        for n in range( len( self._cards )-1 ):
            if( cards[n+1]._card_val - cards[n]._card_val == 0 ):
                return cards[n]._card_val
        return 0

    def _has_two_pair(self):
        """Determines if the hand has two pair."""

        cards = self._cards
        for n in range( 3 ):
            for m in range(n+2,len(cards)-1):
                if( cards[n]._card_val == cards[n+1]._card_val and \
                    cards[m]._card_val == cards[m+1]._card_val ):
                    return True
        return False

    ## -- Hands with a unique value for their 'largest' card -- ##

    def _has_full_house(self):
        """Returns the value of the three of a kind in the full house."""

        cards = self._cards

        # case 1: three of a kind is the larger of two cards
        if( cards[0]._card_val == cards[1]._card_val and \
            cards[1]._card_val == cards[2]._card_val ):
            if( cards[3]._card_val == cards[4]._card_val ):
                self._big_card = cards[0]._card_val
                return cards[0]._card_val

        # case 2: three of a kind is the smaller of two cards
        if( cards[0]._card_val == cards[1]._card_val ):
            if( cards[2]._card_val == cards[3]._card_val and \
                cards[3]._card_val == cards[4]._card_val ):
                self._big_card = cards[2]._card_val
                return cards[2]._card_val

        return 0



    def _has_triple(self):
        """Returns the unique value of triple, if it exists."""

        cards = self._cards
        for n in range( len( self._cards )-2 ):
            if( cards[n  ]._card_val == cards[n+1]._card_val and \
                cards[n+1]._card_val == cards[n+2]._card_val ):
                self._big_card = cards[n]._card_val
                return cards[n]._card_val
        return 0

    def _has_quad(self):
        """Returns the unique value of four of a kind, if it exists."""

        cards = self._cards
        for n in range( len( self._cards )-3 ):
            if( cards[n  ]._card_val == cards[n+1]._card_val and \
                cards[n+1]._card_val == cards[n+2]._card_val and \
                cards[n+2]._card_val == cards[n+3]._card_val ):
                self._big_card = cards[n]._card_val
                return cards[n]._card_val
        return 0
        
def test_compare( h1, h2 ):
    if( h1._hand_type != h2._hand_type ):
        return True

    for (c1,c2) in zip( h1._cards, h2._cards ):
        if( c1._card_val != c2._card_val ):
            return True
    return False

# read in poker file:
filename = 'poker.txt'
f = open( filename, 'r' )

h1 = 0
for line in f.readlines():

    s = line.rsplit()

    p1 = PokerHand( s[:5] )
    p2 = PokerHand( s[5:] )

    assert( test_compare(p1,p2) )
    if( p1 > p2 ):
        h1 = h1+1

f.close()


print(h1)
