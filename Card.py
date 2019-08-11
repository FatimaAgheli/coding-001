class Card():
    '''
        Playing Card Class
    '''
    suits = ('d', 'c', 'h', 's')
    ranks = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')

    def __init__(self, cardInput):
        '''
            Ask for a card number (from 0 representing 2 of diamonds to 51 representing Ace of spades) 
            Will also accept a string to make it easier to set to a specific card
            Standard card string is rank in uppercase then suit in lowercase: e.g. As, 8d 
        '''
        # the 0 assignment is simply a stub... you are expected to change the line below
        self.cardNumber = 0

    def get_suit(self):
        '''
            Returns suit of the card
        '''
        return ''

    def get_rank(self):
        '''
            Returns rank of the card
        '''
        return ''

    def get_rank_value(self):
        '''
            Returns rank of the card as a number. 2 to 14 (14 represents the Ace)
        '''

    def __str__(self):
        return f'{self.get_rank()}{self.get_suit()}'

    def __repr__(self):
        return f'{self.__class__.__name__}({str(self)!r})'

    def __eq__(self, other):
        if type(other) is type(self):
            return self.cardNumber == other.cardNumber
        return NotImplemented

    def __hash__(self):
        return hash(self.cardNumber)
