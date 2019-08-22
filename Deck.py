import random
import time
from collections import deque
from Card import Card


class Deck():
    '''
        Playing Card Deck Class
    '''

    def __init__(self):
        '''
            auto-shuffles a standard deck of 52 cards
        '''
        # line below is a stub. You need to set correctly what cards should be based on requirements
        # cards = []
        # what are the problems you need to resolve?
        # cards.append(Card('2d'))
        cards = [Card(i) for i in range(0, 52)]
        random.shuffle(cards)

        self.allCards = tuple(cards)
        self.genereatedTime = time.time_ns()
        self.undealtCards = deque(cards)
        self.id = self.genereatedTime
    
    def __str__(self):
        '''
            Returns a string representation of all the remaining cards left in the deck: 
            e.g. {'As', 'Qd', 'Jc'}
        '''
        cards = self.undealtCards
        return str(set(cards))

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id}, {str(self)})'

    def __len__(self):
        '''
            Return number of remaining cards in deck
        '''

        cards = self.undealtCards
        return len(cards)

    def deal(self, numCards=1, **kwargs):
        '''
            deal cards. normally deal from top but if a specific card is needed,
            can use keyword specify_card to specify a specific card to deal and remove that card from deck.
            If no cards left, need to raise IndexError to indicate no more cards
            If numCards > 1, return list of dealt cards
            If numCards ==1, return just dealt card
        '''
        
        if 'specify_card' in kwargs:
            self.undealtCards.remove(kwargs['specify_card'])
            return kwargs['specify_card']

        cards = []
        for _ in range(numCards):
            s = self.undealtCards.popleft()
            cards.append(s)
        return cards if len(cards) > 1 else cards[0]

    def __eq__(self, other):
        if type(other) is type(self):
            return self.id == other.id
        return NotImplemented

    def __hash__(self):
        return hash(self.id)
