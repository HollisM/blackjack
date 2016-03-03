import random
from math import *
class Card(object):
    suit_names= ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names= [None, 2, 3, 4, 5, 6 ,7 , 8, 9, 10,'Ace', 'Jack', 'Queen', 'King']
    values= {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'Jack':10,
              'Queen':10, 'King':10, 'Ace':11}

    def __init__(self, suit=0, rank=2):
        self.suit= suit
        self.rank= rank
        self.value= self.rank_names[self.rank]
        ##Anna haleped me with the ranking stuff but we couldn't figure out why
        ## it wasn't working from the error message. 
        
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])
    def __repr__(self):
        return self.__str__()
    
    def __cmp__(self, other):
        """Compares this card to other, first by suit, then rank.
        Returns positive # if this>other ; neg< other ; 0 if this= other
        """
        t1 = self.suit, self.rank
        t2= other.suit, other.rank
        return cmp(t1, t2) 
    
    
class Deck(object):   
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(14):
                card= Card(suit, rank)
                self.cards.append(card)
    def __str__(self):
        res =[]
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def add_card(self, card):
        self.cards.append(card)
        
    def remove_card(self, card):
        self.cards.remove(card)

    def pop_card(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
class Hand(Deck):
    def __init__(self):
        self.cards= []
    def hand_value(self):
        total_hand_value=0
        for card in self.cards:
            total_hand_value+= card.value
            if total_hand_value>21:
                return 'Bust', total_hand_value
            if total_hand_value==21:
                return 'Blackjack!', total_hand_value
            return total_hand_value
        
    
class Playa(object):
    def __init__(self):
        self.myhands= [Hand()]
        self.bankroll= 500
        self.bet= 10
        
class Dealer(object):
    def __init__(self):
        self.hishand= Hand()
##    if total_hand_value>=17:
##        print 'Dealer:' , freddy.hishand.cards[1]
##    if total_hand_value<= 16:
##        deck.move_cards(freddy.hishand, 1)
##        print 'Dealer:' , freddy.hishand.cards[1]
##    if total_hand_value== 21:
##        print 'Dealer, YOU LOSE!!'
##        pass
        
    
    
deck= Deck()
deck.shuffle()
bob= Playa()
freddy= Dealer()
deck.move_cards(bob.myhands[0], 2)
deck.move_cards(freddy.hishand, 1)
print 'Myhand:' , bob.myhands[0]
print 'Dealer:', freddy.hishand.cards[0]
play = 'silly'
while play != "stay":
    play = raw_input('Do you want to hit, stay, split, or doubledown?')
    if play  == 'hit':
        deck.move_cards(bob.myhands[0],1)
        print 'Myhand:', bob.myhands[0]
        print 'Your hand value is:', bob.myhands[0].hand_value()
    if play== "stay":
        deck.move_cards(freddy.hishand, 1)
        print 'Dealer:' , freddy.hishand.cards[1]
    
    
print 'Myhand:', bob.myhands[0]

##I need to make the classes:
    #Player(bet,hand, bankroll) methods: hit, stay, split, double down
    #Dealer(hand) methods: hit and stay with rules 
