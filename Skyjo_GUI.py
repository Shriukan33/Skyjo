import pygame
import sys

pygame.font.init()

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREY = (240, 240, 240)
DARK_GREEN = (80, 180, 80)

# Screen parameters
screen_width = 1000
screen_height = 700

WIN = pygame.display.set_mode(
    [screen_width, screen_height])  # Create the window
WIN.fill(DARK_GREEN)  # colour for representation


# Player class: For now this is just for UI. No game logic exist yet
class Player:

    def __init__(self, player_num, name):
        self.player_num = player_num  # player number: 1, 2, 3 or 4
        self.name = name

        # Player surface object of pygame
        self.y_offset = 0.2 * screen_height/ 3  # The higher the multiplicator, the more longer player surface is
        self.x_offset = 0.03 * screen_width / 3 # The higher the multiplicator, smaller is the horizontal player surface (reduces from right side)
        self.size = [screen_width / 3 - self.x_offset,
                     screen_height / 3 + self.y_offset]  # The size of player Surface

        self.surface = pygame.Surface(self.size)
        self.coordinate = {
            1: (screen_width / 3 + self.x_offset/2, 
                screen_height / 3 * 2 - self.y_offset - self.x_offset),
            2: (screen_width / 3 * 2 + 0, 
                screen_height / 3),
            3: (screen_width / 3 + self.x_offset/2, self.x_offset),
            4: (self.x_offset, screen_height / 3),
        }
        # Gaps between cards on player's surface
        self.v_gap = 0.02 * self.size[1]
        self.h_gap = 0.13 * self.size[0]

        self.score = 0

        self.surface.fill(LIGHT_GREY) # Background color for players

    # NOTE: Temporary just to show the UI for now
    # this method draw and blits the surface into main window object
    def draw_player(self):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        name_text = font.render(self.name, True, BLACK)
        score_text = font.render(
            "Score: {}".format(self.score), True, BLACK)

        card = Card()
        for y in range(3):
            for x in range(4):
                self.surface.blit(card.surface, [24 + card.surface.get_width() * x + self.h_gap * x,
                                                 10 + self.y_offset + card.surface.get_height() * y + self.v_gap * y])
        border = pygame.Rect((24, self.y_offset + 10),
                             (card.size[0] * 4 + self.h_gap * 3, card.size[1] * 3 + self.v_gap * 2))
        pygame.draw.rect(self.surface, BLACK, border, 1)

        self.surface.blit(
            name_text, (self.size[0] / 2 - name_text.get_width() / 2, 0))
        self.surface.blit(
            score_text, (self.size[0] / 2 - score_text.get_width() / 2, border.bottomright[1]))

        WIN.blit(self.surface, self.coordinate[self.player_num])


class Card:

    def __init__(self):
        self.size = [36, 55]  # Hardcoded size of each card surface
        # create surface instance of pygame for card
        self.surface = pygame.Surface(self.size)


Player(1, "Player 1").draw_player()
Player(2, "Player 2").draw_player()
Player(3, "Player 3").draw_player()
Player(4, "Player 4").draw_player()
pygame.display.update()
# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
