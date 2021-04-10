from random import shuffle

class Deck:
    """
    Deck class handles original deck building and drawing action.
    """

    def __init__(self):
        self.cards = [] # Deck is represented with a list of numbers from -2 to 12
        self.minus_two = 5 # Number of minus two in build
        self.zeroes = 15 # Number of zeroes in build
        self.other_cards = 10 # # Number of -1 and 1->12 in build
        self._build()  # Populates self.cards

    def _build(self):
        """
        Adds cards as defined in properties to the deck and shuffles it. 
        """
        for _ in range(self.minus_two):
            self.cards.append(-2)
        for _ in range(self.zeroes):
            self.cards.append(0)
        for _ in range(self.other_cards):
            self.cards.append(-1)
            for k in range(1, 13):
                self.cards.append(k)

        shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

class Discard:

    def __init__(self):
        self.cards = []
        self._build()

    def _build(self):
        """
        At game initialization, the discard is composed of the first card of the deck
        Deck has to be initialized first
        """
        self.cards.append(deck.draw())

    def show_top_card(self):
        """
        Top card of discard is visible at any time by players
        """
        return self.cards[-1]

deck = Deck()
discard = Discard()