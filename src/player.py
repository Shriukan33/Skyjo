import numpy as np
from cards import *

class Player:

    player_list = []
    def __init__(self, player_num, name):
        self.player_list.append(self) # List to cycle through instances of Player
        self.player_num = player_num  # player number: 1, 2, 3 or 4
        self.name = name
        self.score = 0  # Score displayed on screen
        self.hand = []  # Actual cards in hand
        self.public_hand = [] # Cards visible to the player mix of hidden and revealed cards
        self._base_hand() # Not implemented yet, builds a base hand of 12 cards
        self.finished = False # Is True once you revealed all your cards
        self.finished_first = False


    def __repr__(self):
        return str(self.name)

    def _base_hand(self):
        """
        Will deal 12 cards to the player.
        """
        for _ in range(12):
            self.hand.append(deck.draw())
        self.hand = np.array(self.hand).reshape(3,4) # Might be used later on to check for column completion

