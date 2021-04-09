import pygame
import sys, os

pygame.font.init()

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREY = (240, 240, 240)
DARK_GREEN = (80, 180, 80)

# Screen parameters
FPS = 60
pygame.display.set_caption("Skyjo GUI")
icon = pygame.image.load(os.path.join("Skyjo", "assets", "skyjo_icon.png"))
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
        Player.draw_player(player)
    
    pygame.display.update()


# Player class: For now this is just for UI. No game logic exist yet
class Player:

    player_list = []
    def __init__(self, player_num, name):
        self.player_list.append(self) # List to cycle through instances of Player
        self.player_num = player_num  # player number: 1, 2, 3 or 4
        self.name = name


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

        self.score = 0

        self.surface = pygame.Surface(self.size)
        self.surface.fill(LIGHT_GREY) # Background color for players


    def __repr__(self):
        return str(self.name)

    # NOTE: Temporary just to show the UI for now
    # this method draw and blits the surface into main window object

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


Player(1, "Player 1").draw_player()
Player(2, "Player 2").draw_player()
Player(3, "Player 3").draw_player()
Player(4, "Player 4").draw_player()

# Game Loop
def main():
    clock = pygame.time.Clock() # used to cap framerate

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(Player.player_list[0].size)
                pygame.quit()
                sys.exit()
            
        draw_screen()
         
if __name__ == '__main__':
    main()
