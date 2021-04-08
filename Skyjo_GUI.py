import pygame
import sys

pygame.font.init()

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREY = (240, 240, 240)
DARK_GREEN = (80, 180, 80)

# Screen parameters
screen_width = 1920
screen_height = int(screen_width / (16/9))

WIN = pygame.display.set_mode(
    [screen_width, screen_height])  # Create the window
WIN.fill(DARK_GREEN)  # colour for representation


# Player class: For now this is just for UI. No game logic exist yet
class Player:

    def __init__(self, player_num, name):
        self.player_num = player_num  # player number: 1, 2, 3 or 4
        self.name = name


        self.padding = 0.03 * screen_width # Padding in pixels
        padded_screen = {"width": screen_width - 2 * self.padding, 
                        'height': screen_height - 2 * self.padding}

        self.size = [padded_screen["width"] / 3,
                     padded_screen["height"] / 3]
                        
        self.coordinate = {
            1: (screen_width/3 + self.padding / 2,
                screen_height/3 * 2),

            2: (screen_width/3 * 2,
                screen_height/3 + self.padding / 2),

            3: (screen_width/3 + self.padding / 2,
                self.padding),

            4: (self.padding,
                screen_height/3 + self.padding / 2)
        }

        # Gaps between cards on player's surface
        self.v_gap = 0.05 * self.size[1]
        self.h_gap = 0.05 * self.size[0]

        self.score = 0

        self.surface = pygame.Surface(self.size)
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
                                                 10 + self.padding + card.surface.get_height() * y + self.v_gap * y])
        border = pygame.Rect((24, self.padding + 10),
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
