import pygame
import sys


class App:
    """
    Inherit this class and make changes run, build or init methods to make your own app.
    Finally call execute function to run the program.
    """
    def __init__(self, width: int) -> None:
        """
        Initialize the window here
        """
        self.aspect_ratio = 4 / 3
        self.width = width
        self.height = int(self.width / self.aspect_ratio)
        self.window = pygame.display.set_mode([self.width, self.height])

    def build(self) -> None:
        """
        This function will run only once before the loop
        """
        pass

    def loop(self) -> None:
        """
        This function will run on a loop
        """
        pass

    def execute(self, FPS=60) -> None:
        "Call this to run the program"
        self.build()
        clock = pygame.time.Clock()

        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.loop()
            pygame.display.update()
