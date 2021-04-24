import pygame
from random import shuffle
from pathlib import Path


class Card:

    hidden_image = pygame.image.load(Path("./assets/hidden.png"))

    def __init__(self, value: int) -> None:
        self.size = [(40/1280) * pygame.display.get_window_size()[0], (62/960) * pygame.display.get_window_size()[1]]
        self.value = value
        self.hidden = True
        self.surface = pygame.Surface(self.size)

    def draw_card(self, player: pygame.Surface, pos: tuple[float, float], x: int, y: int) -> None:
        self.set_background()
        player.blit(
            self.surface, [
                pos[0] + self.size[0] * x,
                pos[1] + self.size[1] * y
            ]
        )

    def set_background(self) -> None:
        if self.hidden:
            self.surface.blit(self.hidden_image, (0, 0))


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

    def shuffle_deck(self) -> None:
        shuffle(self.cards)
