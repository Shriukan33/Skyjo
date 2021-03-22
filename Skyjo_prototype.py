# skyjo is a tabletop game of cards, you need to build a deck of 12 cards cumulating the lower sum of points among the
# other players. Cards are numeroted from -2 to 12, with 5 x "-2" / 15 x "0" / 130 x "-1" and cards from "1" to "12"
# Your deck is composed initially of 12 cards, disposed in a 3 row 4 columns way. 2 cards are randomly revealed at start.
# Player with highest score starts, top card of main deck is discarded so everyone can see it.
# You build the deck by either picking the top card from discard pile or drawing a new card from deck.
# You can then replace one of your card (wether it's revealed or not) or simply discard the drew card and reveal one you
# already had.
# First player to reveal all 12 cards of his deck ends the game, letting everyone one more turn to play.
# Completing a columns with the same number discards the entire column.
# Lower the total score is, the better. The score is the sum of all numbers on your cards.
# Finishing player must be the one with the lowest score, or doubles his points.
# Game finished when cumulated scores of previous rounds gets to 100.

# TODO
# Implement AI player.
# Notes for AI implementation :
# 1) Make the AI choose a single index number instead of coordinates by flattening its hand.
# Loop to delete columns in 1D arrays (by grouping by 3)
# for card in range(1, len(main), 3):
#     print(main[card - 1:card + 2])
#     ref = main[card - 1]
#     if ref != self.hidden_skin:
    #     if main[card] == ref and main[card + 1] == ref:
    #         print("column of", ref)
    #         test = np.delete(main, [range(card - 1, card + 2)])
    #
# print(test)

from random import shuffle
import numpy as np
import os

# --- Number of each type of cards --- #
NUMBER_OF_MINUS_2 = 5
NUMBER_OF_MINUS_1_TO_TWELVE = 10
NUMBER_OF_ZEROES = 15


class Card:
    def __init__(self, value):
        self.value = value

    def show(self):
        print(self.value)

    def __repr__(self):
        return str(self.value)

    def __add__(self, other):
        if other == []:
            return self.value + 0
        elif self.value == []:
            return 0
        else:
            return self.value + other

    def __radd__(self, other):
        if other == 0:
            return self.value
        if other == []:
            return self.__add__(0)
        else:
            return self.__add__(other)

    def __int__(self):
        return self.value


class IterRegistery(type):
    """This class is used to iter through all instances of Player's class"""
    def __iter__(cls):
        return iter(cls._registery)


class Player(metaclass=IterRegistery):

    _registery = [] # List with all instances of Player class.

    def __init__(self, name):
        self._registery.append(self) # List to track all instances of Player class.
        self.name = name
        self.hand = []  # Will be filled by Card class objects
        self.public_hand = [] # The hand of the player as seen by all player. "X" == hidden card
        self.public_score = 0 # Updated when check_public_score is called, is available to players.
        self.score = 0  # Updated when check_score is called.
        self.base_hand() # Deals 12 cards to the player
        self.hidden_skin = "--"  # Appearance of not revealed cards.
        self.hide_hand() # hides the values of the player with the hidden skin.
        self.revealed = 0   # Counts the number of cards revealed by the player. updated with check public score.
        self.finished_first = False   # True if the player is the first to reveal all his cards.
        self.finished = False  # True once you revealed  all your card, no matter if you finished first or not.

    def __repr__(self):
        return self.name

    def __str__(self):
        return str(self.name)

    def base_hand(self):
        """Deals 12 Card class object to the player, and make it a 3x4 matrix"""
        for card in range(12):
            self.hand.append(deck.draw_card())
        self.hand = np.array(self.hand).reshape(3, 4)

    def show_full_hand(self):
        """Shows a fully revealed version of player's hand"""
        return print("Here is {}'s hand : \n".format(self.name) , self.hand)

    def show_hand(self):
        return print(self.public_hand)

    def check_score(self):
        """Shows the score of a fully revealed hand"""
        self.score = np.sum(self.hand)
        return print("{}'s score is {}\n".format(self.name, self.score))

    def hide_hand(self):
        """Makes the hand hidden for everyone"""
        self.public_hand = np.array([self.hidden_skin for k in range(12)]).reshape(3,4)

    def check_public_score(self):
        """Calculate the score of revealed cards"""
        public_score = 0
        revealed = 0
        row, column = self.public_hand.shape
        for r in range(row):
            for c in range(column):
                if self.public_hand[r, c] != self.hidden_skin:
                    public_score += int(self.public_hand[r, c])
                    revealed += 1
        self.public_score = public_score
        self.revealed = revealed

        return print("{}'s public score is {}.".format(self.name, public_score))

    def reveal(self, row, column):
        """Reveal a card in player's hand given the coordinates"""
        if self.check_coordinates(row, column):
            if self.public_hand[row, column] == self.hidden_skin:
                self.public_hand[row, column] = self.hand[row, column]
                print(self.name, "reveals a", self.hand[row, column], "!")
                self.check_public_score()
                self.show_hand()
            else:
                print("This card is already revealed ! Pick another one.")
                row = int(input("Your coordinates are invalid, please enter a valid row : "))
                column = int(input("Now, please enter a valid column : "))
                self.reveal(row, column)
        else:
            row = int(input("Your coordinates are invalid, please enter a valid row : "))
            column = int(input("Now, please enter a valid column : "))
            self.reveal(row, column)

    def reveal_all(self):
        """Reveals all cards in hand and updates the public score."""
        self.public_hand = self.hand
        self.check_public_score()

    def check_coordinates(self, row, column):
        """Validate the coordinates input from players"""
        len_row, len_col = np.shape(self.hand)
        row = int(row)
        column = int(column)
        if row < 0 or row >= len_row or column < 0 or column >= len_col:
            return False
        else:
            return True

    def deck_swap(self, row, column):
        """Picks the first card on the deck and places it in hand"""
        if self.check_coordinates(row, column):
            print(self.name, "discards a", self.hand[row, column],".")
            discard.cards.append(self.hand[row, column])
            self.hand[row, column] = deck.draw_card()
            self.public_hand[row, column] = self.hand[row, column]
            self.check_public_score()
        else:
            row = int(input("Your coordinates are invalid, please enter a valid row : "))
            column = int(input("Now, please enter a valid column : "))
            self.deck_swap(row, column)

    def discard_swap(self, row, column):
        """Swaps the targeted card with the top card of the  discard pile"""
        if self.check_coordinates(row, column):
            temp = self.hand[row, column]
            print(self.name, "discards a ", temp)
            self.hand[row, column] = discard.cards.pop()
            discard.cards.append(temp)
            self.public_hand[row, column] = self.hand[row, column]
            self.check_public_score()
        else:
            row = int(input("Your coordinates are invalid (out of range), please enter a valid row : "))
            column = int(input("Now, please enter a valid column : "))
            self.discard_swap(row, column)

    def check_column(self):
        """Checks if a column has all its elements the same value. Discards the whole column if so."""
        r, c = np.shape(self.hand)
        for column in range(c):
            match = 0
            if self.public_hand[0, column] != self.hidden_skin:
                reference = self.public_hand[0, column]
            else:
                continue
            for row in range(r):
                if self.public_hand[row, column] != self.hidden_skin:
                    if self.public_hand[row, column] == reference:
                        match += 1
                    else:
                        continue
                else:   # If a card is hidden, next column
                    continue
            if match == 3:
                print("Column number ", column, " is a full column, and will be discarded")
                disc_column = list(range(c))
                cards = disc_column.pop(column) # Deletes the column with a match
                for k in (self.public_hand[:, cards]):
                    discard.cards.append(k)
                self.hand = self.hand[:, disc_column] # Update the hands
                self.public_hand = self.public_hand[:, disc_column]
                break

    def check_finish(self):
        """Checks if player has finished the game first or not."""
        global end_phase
        not_first = False
        if end_phase == False:
            row, column = self.hand.shape
            number_of_cards = row * column
            if self.revealed == number_of_cards: # If the  player has revealed all of his cards in hand
                self.finished = True
                for player in Player: # Check if a players had already finished  the game before
                    if player.finished_first  == True:
                        not_first = True
                if not_first:
                    print(self.name, "has finished ! Final score is :", self.public_score)
                else:
                    self.finished_first = True
                    print(self.name, "has engaged End phase. 1 round remaining for all remaining players")
                    end_phase = True
        else:
            self.reveal_all()
            print(self.public_hand, "\n")
            print("This was", self.name, "'s last round, final score : ", self.public_score)
            self.finished = True
            end = 0
            for player in Player:
                if player.finished == False:
                    end += 1
            if end == 0:
                final_score()


class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        self.shuffle_deck()

    def build(self):
        for card in range(NUMBER_OF_MINUS_2):
            self.cards.append(Card(-2))
        for card in range(NUMBER_OF_ZEROES):
            self.cards.append(Card(0))
        for card in range(NUMBER_OF_MINUS_1_TO_TWELVE):
            self.cards.append(Card(-1))
            for k in range(1,  13):
                self.cards.append(Card(k))

    def average(self):
        return sum(self.cards)/len(self.cards)

    def shuffle_deck(self):
        shuffle(self.cards)

    def show(self):
        print(self.cards)

    def draw_card(self):
        return self.cards.pop()

    def show_top(self):
        print("Top card of deck : ", self.cards[-1])


class Discard_Pile:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        """Uses the first card of the deck to build the initial discard pile"""
        self.cards.append(deck.draw_card())

    def show_top(self):
        return print(self.cards[-1])

    def show(self):
        print(self.cards)


def scoreboard():
    """Displays the scoreboard"""
    for player in Player:
        print(player.name, "'s score is ", player.public_score)


def final_score():
    """Displays the final scoreboard and calculate scores according to rules."""
    # Get the lowest score and its player
    scores = {}
    for player in Player:
        scores[player.name] = player.public_score
    min_score = min(scores, key=scores.get)

    # Find if the first to finish has the lowest score
    double_score = False
    for player in  Player:
        if player.name == min_score:
            if not player.finished_first:
                double_score = True
                break

    # Displays the final scoreboard
    print("Here is  the final scoreboard :")
    for player in Player:
        if double_score:
            if player.finished_first:
                player.public_score *= 2
                print(player.name, "'s score is doubled to", player.public_score)
            else:
                print(player.name, ":", player.public_score)
        else:
            print(player.name, ":",  player.public_score)

    print("\n", min_score, "wins !")
    global game_running
    game_running = False
    os.system("pause")

def show_board():
    """Shows the public hands of all players"""
    for player in Player:
        player.check_public_score()
        print(player.public_hand, "\n")
    os.system("pause")

def choices():
    """Handles the choices of players once they drew a card."""
    while True:
        try:
            choice = input("Do you want to swap it with one of you cards ? (y/n/board) ")
            if choice == "y" or choice == "n":
                break
            else:
                if choice == "board":
                    show_board()
                raise Exception()
        except:
            continue

    return choice


def discard_deck():
    """Takes the first card of the deck and places it in """
    discard.cards.append(deck.cards.pop())


def party_creation():
    """Creates a set of players, from 2 to 8"""
    # Number of players validation
    player_count = 0
    while player_count <= 1 or player_count > 8:
        try:
            player_count = int(input("How many players at the table ? (2 to 8) \n"))
        except ValueError:
            print("Invalid input. Try again !")
            continue

    # Checking if two players have the same name
    for number in range(1,player_count+1):
        while True:
            try:
                name = input("What's the name of player {} ? ".format(number))
                for player in Player:
                    if name == player.name:
                        print("This name is already taken !")
                        raise Exception("This name is already taken !")
                break
            except:
                continue

        player = Player(name)
    print("\nHere is the list of all players : \n")
    for player in Player:
        print(player.name)


# Basic setup, mandatory.
end_phase = False  # True on last round.
game_running = True  # End game condition
deck = Deck()
discard = Discard_Pile()
party_creation()

# Game loop
turn = 0  # turn counter

# Debug / test commands
# for row in range(3):
#     for column in range(1,4):
#         Player._registery[0].reveal(row, column)
# End of Debug commands

while game_running:
    # At each player's turn
    number = 0 # Player's number, to identify them in the Player._registery list

    # Turn number 1 starts with the player which has the highest score after revealing 2 cards.
    if turn == 1:
        max_score = -5 # Lowest possible value is -4 with 2 x -2
        player_number = 0
        for player in Player:
            if player.public_score > max_score:
                number = player_number
                max_score = player.public_score
                player_name = player.name
            player_number += 1
        print("\n{} has the highest score with {} points and will be the first to play.".format(player_name, max_score))

    # General game loop

    for player in Player._registery:

        # Check if this is the correct player's turn. Might be useless as long as the registery is used.
        if player != Player._registery[number]:
            continue

        print("\nIt's {}'s  turn !".format(Player._registery[number].name))
        Player._registery[number].show_hand()
        # At first turn only
        if turn ==  0:
            print("You need to pick 2 cards to reveal. First write the row number (starting at 0), then the column (starting at 0).")
            for k in range(1, 3):
                while True:
                    try:
                        row = int(input("Please enter the line of card {} : ".format(k)))
                        column = int(input("Please enter the column of card {} : ".format(k)))
                        Player._registery[number].reveal(row, column)
                        break
                    except:
                        continue

        # At any other turn, we're checking if the player has finished to play last round.
        if Player._registery[number].finished == False and turn != 0: # If the player didn't play his end phase.
            print("The visible card from discard is a", discard.cards[-1])

            # Choice verification and question "do you pick it ?"
            choice = choices()

            # Case yes : Discard swap
            if choice == 'y':
                print(Player._registery[number].name, "is taking the", discard.cards[-1],".")
                row = int(input("With what card will you swap it ? (row) : "))
                column = int(input("With what card will you swap it ? (column) : "))
                Player._registery[number].discard_swap(row, column)
                Player._registery[number].check_column()
                Player._registery[number].show_hand()
                Player._registery[number].check_finish()
                os.system("pause")

            # Case no : Pick the top card of the deck
            elif choice == "n":
                print(Player._registery[number].name, "doesn't pick the discard and draws from the deck.")
                deck.show_top() # Displays the top card of the deck

                # Choice verification and question "do you pick it ?"
                choice = choices()

                # You pick the top card of the deck after denying the discard's one
                if choice == "y":
                    print(Player._registery[number].name, "is taking the", deck.cards[-1], ".")
                    row = int(input("With what card will you swap it ? (row) : "))
                    column = int(input("With what card will you swap it ? (column) : "))
                    Player._registery[number].deck_swap(row, column)
                    Player._registery[number].check_column()
                    Player._registery[number].show_hand()
                    Player._registery[number].check_finish()
                    os.system("pause")

                # You don't pick the top card of the deck after denying the discard's one
                elif choice == "n":
                    print(Player._registery[number].name, "doesn't take the", deck.cards[-1], " and reveals a card.")
                    row = int(input("Pick the row of the card you're revealing : "))
                    column = int(input("Pick the column of the card you're revealing :  "))
                    Player._registery[number].reveal(row, column)
                    Player._registery[number].check_column()
                    Player._registery[number].check_finish()
                    discard_deck()
                    os.system("pause")

                # # Kill switch of the game
                # game_running = False
                # break

        # Next player counter, reset every turn
        number += 1

    # Turn counter, and scoreboard for players to track progression.
    turn += 1
    scoreboard()


