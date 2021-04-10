import pygame
import sys
from player import Player 
from interface import *

# Game Loop
def main():
    Player_GUI(1, "Player 1").draw_player()
    Player_GUI(2, "Player 2").draw_player()
    Player_GUI(3, "Player 3").draw_player()
    Player_GUI(4, "Player 4").draw_player()
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