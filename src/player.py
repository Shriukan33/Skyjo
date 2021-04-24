import pygame
from card import Deck


class Player:

    player_list = []

    PADDING_RATE = 0.05

    def __init__(self, player_num: int, name: str, screen_width: int, screen_height: int, deck) -> None:
        self.player_list.append(self)
        self.player_num = player_num
        self.name = name

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.score = 0

        self.padding = self.PADDING_RATE * self.screen_width
        self.size = [
            self.screen_width / 3 * (1 - 2*self.PADDING_RATE),
            self.screen_height / 3 * (1 - 2*self.PADDING_RATE)
        ]

        # Coordinates of players on Screen
        self.coordinate = {
            1: (self.screen_width/3 + self.padding / 4,
                self.screen_height/3 * 2),

            2: (self.screen_width/3 * 2,
                self.screen_height/3 + self.padding / 4),

            3: (self.screen_width/3 + self.padding / 4,
                self.padding / 2),

            4: (self.padding / 2,
                self.screen_height/3 + self.padding / 4)
        }

        # Gaps between cards on player's surface
        self.v_gap = 0.05 * self.size[1]
        self.h_gap = 0.10 * self.size[0]

        self.surface = pygame.Surface(self.size)        # Creating Surface object for player

        self.hand = []              # This is being used for test now
        self.public_hand = []       # No use for now
        self.build(deck)

    def center_card_area(self, card_size) -> tuple[float, float]:
        width = (self.size[0] - 4 * card_size[0] - 3 * self.h_gap)/2
        height = (self.size[1] - 3 * card_size[1] - 2 * self.v_gap)/2
        return width, height

    def build(self, deck: Deck) -> None:
        """
        Build the hand by taking out cards from deck
        """
        for _ in range(3):
            temp = []
            for _ in range(4):
                temp.append(deck.draw_card())
            self.hand.append(temp)

    def draw(self, window: pygame.Surface) -> None:
        size = [(40/1280) * pygame.display.get_window_size()[0], (62/960) * pygame.display.get_window_size()[1]]
        pos = self.center_card_area(size)
        for y in range(3):
            for x in range(4):
                self.hand[y][x].draw_card(self.surface, (pos[0] + self.h_gap * x, pos[1] + self.v_gap * y), x, y)

        window.blit(self.surface, self.coordinate[self.player_num])

    def set_background(self, color: tuple[int, int, int]) -> None:
        "Set color of the player surface"
        self.surface.fill(color)
