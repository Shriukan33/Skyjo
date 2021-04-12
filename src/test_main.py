import sys
from player import Player, draw_screen
from interface import FPS, WIN, DARK_GREEN, pygame


# Game Loop
def main():
    Player(1, "Player 1")
    Player(2, "Player 2")
    Player(3, "Player 3")
    Player(4, "Player 4")
    clock = pygame.time.Clock()  # used to cap framerate

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(Player.player_list[0].size)
                pygame.quit()
                sys.exit()

        draw_screen(WIN, DARK_GREEN)
        pygame.display.update()


if __name__ == '__main__':
    main()
