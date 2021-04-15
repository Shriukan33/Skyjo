import pygame
from random import shuffle


class Card:

    def __init__(self, value: int) -> None:
        self.size = [(40/1280) * pygame.display.get_window_size()[0], (62/960) * pygame.display.get_window_size()[1]]
        self.value = value
        self.surface = pygame.Surface(self.size)

    def draw_card(self, player: pygame.Surface, pos: tuple[float, float], x: int, y: int):
        player.blit(
            self.surface, [
                pos[0] + self.size[0] * x,
                pos[1] + self.size[1] * y
            ]
        )


class Deck:
    NUMBER_OF_MINUS_2 = 5
    NUMBER_OF_MINUS_1_TO_TWELVE = 10
    NUMBER_OF_ZEROES = 15

    def __init__(self) -> None:
        self.cards = []
        self.build()
        self.shuffle_deck()

    def build(self) -> None:
        for _ in range(self.NUMBER_OF_MINUS_2):
            self.cards.append(Card(-2))
        for _ in range(self.NUMBER_OF_ZEROES):
            self.cards.append(Card(0))
        for _ in range(self.NUMBER_OF_MINUS_1_TO_TWELVE):
            self.cards.append(Card(-1))
            for k in range(1,  13):
                self.cards.append(Card(k))

    def draw_card(self) -> Card:
        return self.cards.pop()

    def shuffle_deck(self):
        shuffle(self.cards)
