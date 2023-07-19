import pygame


class Setup:
    def __init__(self) -> None:
        self.window_size = self.winx, self.winy = 1200, 720
        self.surface = pygame.display.set_mode(self.window_size)
        self.win_title = pygame.display.set_caption('no game future')
        self.fps = 50
        self.ticker = pygame.time.Clock()
        self.color = pygame.Color(0, 0, 55)
    
    def starter(self):
        errors = pygame.init()
        if errors[1] > 0:
            print(errors)
    
    def set_fps(self):
        self.ticker.tick(self.fps)
    
    def set_bg(self):
        self.surface.fill(self.color)
    
    def update(self):
        pygame.display.update()
