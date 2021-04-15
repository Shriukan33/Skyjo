from modules.base import App
from player import Player
import os
if os.name == "nt":
    import ctypes
    ctypes.windll.user32.SetProcessDPIAware()


class Game(App):

    def __init__(self, width: int) -> None:
        super().__init__(width)

    def build(self) -> None:
        self.window.fill((255, 255, 255))
        Player(1, "name", self.width, self.height)
        Player(2, "name", self.width, self.height)
        Player(3, "name", self.width, self.height)
        Player(4, "name", self.width, self.height)

    def loop(self) -> None:
        for player in Player.player_list:
            player.set_color((240, 240, 240))
            player.draw(self.window)


if __name__ == "__main__":
    game = Game(1280)
    game.execute()
