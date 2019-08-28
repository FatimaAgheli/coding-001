from Card import Card

class PokerHand():
    '''
        PokerHand class
    '''

    def __init__(self, board, playerHand):
        '''
            board: list of at least 3 Card objects, and up to 5 Card objects, representing a board in Texas Hold'em Poker
            playerHand: list of 2 Card objects, representing a player's hidden cards
            - both values above can accept a string (e.g. 'As Ah') or a list of cards
        '''
        if isinstance(board, str):
            # TODO:  self.board = 
            # self.playerHand = 
            pass
        else:
            self.board = board
            self.playerHand = playerHand

        cards = self.board + self.playerHand
        self.ranking = PokerHand.calculate_score(cards)

    @staticmethod
    def calculate_score(cards):
        '''
            Takes a list of Card objects and return score, using poker_score function
        '''
        # TODO: use the poker_score() function - note that the input variables cards is not what the poker_score() function
        # expects. Need to convert to appropriate data
        pass

    def get_best_ranking(self):
        return self.ranking

    def get_board(self):
        return self.board
    
    def get_playerHand(self):
        return self.playerHand

    def get_best_ranking_cards_description(self):
        # TODO: return description of best ranking cards. See https://en.wikipedia.org/wiki/List_of_poker_hands
        # for rules on how to describe a poker rank hand (e.g. 6s 6h 6d Kh Kd best hand will 
        # return 'Full house, sixes over kings')
        return ''

    def __str__(self):
        return self.get_best_ranking_cards_description()

    def __repr__(self):
        return f'{self.__class__.__name__}({str(self.board), str(self.playerHand)})'
