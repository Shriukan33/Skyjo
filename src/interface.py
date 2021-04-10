import pygame
from player import Player
from cards import *
from pathlib import Path


pygame.font.init()
# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREY = (240, 240, 240)
DARK_GREEN = (80, 180, 80)

# Screen parameters
FPS = 60
pygame.display.set_caption("Skyjo GUI")
icon = pygame.image.load(Path("./assets/skyjo_icon.png"))
pygame.display.set_icon(icon)
aspect_ratio = [16/9, 4/3]
screen_width = 1280
screen_height = int(screen_width / aspect_ratio[1])
WIN = pygame.display.set_mode(
    [screen_width, screen_height])  # Create the window
WIN.fill(DARK_GREEN)  # Background colour
PADDING_RATE = 0.05

# Assets
CARD_SIZE = [40, 62]

# FONTS
NAME_FONT = pygame.font.SysFont('Comic Sans MS', 20)
NAME_COLOR = BLACK
SCORE_FONT = pygame.font.SysFont('Comic Sans MS', 20)
SCORE_COLOR = BLACK

def draw_screen():

    WIN.fill(DARK_GREEN)
    for player in Player.player_list:
        Player_GUI.draw_player(player)
    
    pygame.display.update()

class Player_GUI(Player):

    def __init__(self, player_num, name):
        super().__init__(player_num, name)

        self.padding = PADDING_RATE * screen_width # 3% on each side of the screen is padded
        self.size = [screen_width / 3 * (1 - 2*PADDING_RATE),
                     screen_height / 3 * (1 - 2*PADDING_RATE)]
                        
        self.coordinate = {
            1: (screen_width/3 + self.padding / 4 ,
                screen_height/3 * 2),

            2: (screen_width/3 * 2,
                screen_height/3 + self.padding / 4),

            3: (screen_width/3 + self.padding / 4,
                self.padding / 2 ),

            4: (self.padding /2,
                screen_height/3 + self.padding / 4)
        }

        # Gaps between cards on player's surface
        self.v_gap = 0.05 * self.size[1]
        self.h_gap = 0.10 * self.size[0]

        self.surface = pygame.Surface(self.size)
        self.surface.fill(LIGHT_GREY) # Background color for players

    def center_card_area(self):
        width = (self.size[0] - 4 * CARD_SIZE[0] - 3 * self.h_gap)/2
        height = (self.size[1] - 3 * CARD_SIZE[1] - 2 * self.v_gap)/2
        return width, height

    def draw_player(self):
        name_text = NAME_FONT.render(self.name, True, NAME_COLOR)
        score_text = SCORE_FONT.render(
            "Score: {}".format(self.score), True, SCORE_COLOR)

        card = Card()
        center_width, center_height = self.center_card_area()
        for y in range(3):
            for x in range(4):
                self.surface.blit(card.surface, [center_width + card.surface.get_width() * x + self.h_gap * x,
                                                 center_height + card.surface.get_height() * y + self.v_gap * y])
        border = pygame.Rect((center_width, center_height),
                             (card.size[0] * 4 + self.h_gap * 3, card.size[1] * 3 + self.v_gap * 2))
        pygame.draw.rect(self.surface, BLACK, border, 1)

        self.surface.blit(
            name_text, (self.size[0] / 2 - name_text.get_width() / 2, 0))
        self.surface.blit(
            score_text, (self.size[0] / 2 - score_text.get_width() / 2, border.bottomright[1]))

        WIN.blit(self.surface, self.coordinate[self.player_num])



class Card:

    card_list = []
    def __init__(self):
        self.card_list.append(self)
        self.size = CARD_SIZE
        # create surface instance of pygame for card
        self.surface = pygame.Surface(self.size)