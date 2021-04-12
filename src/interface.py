import pygame
from pathlib import Path

pygame.font.init()

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREY = (240, 240, 240)
DARK_GREEN = (80, 180, 80)

# CONSTANTS
FPS = 60
ASPECT_RATIO = 4/3
PADDING_RATE = 0.05

# Screen Setup
screen_width = 1000
screen_height = int(screen_width / ASPECT_RATIO)

WIN = pygame.display.set_mode(
    [screen_width, screen_height]
)
WIN.fill(DARK_GREEN)

# Assets
pygame.display.set_caption("Skyjo")
icon = pygame.image.load(Path("./assets/skyjo_icon.png"))
pygame.display.set_icon(icon)

# Cards
CARD_SIZE = [(40/1280) * screen_width, (62/960) * screen_height]

# Fonts
NAME_FONT = pygame.font.SysFont('Comic Sans MS', 20)
NAME_COLOR = BLACK
SCORE_FONT = pygame.font.SysFont('Comic Sans MS', 20)
SCORE_COLOR = BLACK


class PlayerUI:

    def __init__(self, player_num, name) -> None:
        self.player_num = player_num                            # player number: 1, 2, 3 or 4
        self.name = name

        self.score = 0                                          # Score displayed on screen

        self.padding = PADDING_RATE * screen_width              # 5% on each side of the screen is padded
        self.size = [screen_width / 3 * (1 - 2*PADDING_RATE),
                     screen_height / 3 * (1 - 2*PADDING_RATE)]

        # Coordinates of players on Screen
        self.coordinate = {
            1: (screen_width/3 + self.padding / 4,
                screen_height/3 * 2),

            2: (screen_width/3 * 2,
                screen_height/3 + self.padding / 4),

            3: (screen_width/3 + self.padding / 4,
                self.padding / 2),

            4: (self.padding / 2,
                screen_height/3 + self.padding / 4)
        }

        # Gaps between cards on player's surface
        self.v_gap = 0.05 * self.size[1]
        self.h_gap = 0.10 * self.size[0]

        self.surface = pygame.Surface(self.size)        # Creating Surface object for player
        # Background color for players
        self.surface.fill(LIGHT_GREY)

    def center_card_area(self) -> tuple[float, float]:
        width = (self.size[0] - 4 * CARD_SIZE[0] - 3 * self.h_gap)/2
        height = (self.size[1] - 3 * CARD_SIZE[1] - 2 * self.v_gap)/2
        return width, height

    def draw_player(self) -> None:
        name_text = NAME_FONT.render(self.name, True, NAME_COLOR)
        score_text = SCORE_FONT.render(
            "Score: {}".format(self.score), True, SCORE_COLOR
        )

        card = Card()
        center_width, center_height = self.center_card_area()
        for y in range(3):
            for x in range(4):
                self.surface.blit(
                    card.surface, [
                        center_width + card.surface.get_width() * x + self.h_gap * x,
                        center_height + card.surface.get_height() * y + self.v_gap * y
                    ]
                )
        border = pygame.Rect(
            (center_width, center_height),
            (card.size[0] * 4 + self.h_gap * 3, card.size[1] * 3 + self.v_gap * 2)
        )
        # pygame.draw.rect(self.surface, BLACK, border, 1)

        self.surface.blit(
            name_text, (self.size[0] / 2 - name_text.get_width() / 2, 0)
        )
        self.surface.blit(
            score_text, (self.size[0] / 2 - score_text.get_width() / 2, border.bottomright[1])
        )

        WIN.blit(self.surface, self.coordinate[self.player_num])


class Card:

    def __init__(self) -> None:
        self.size = CARD_SIZE
        # create surface instance of pygame for card
        self.surface = pygame.Surface(self.size)
