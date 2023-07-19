import random
import pygame
from .main import Setup


class Skate(Setup):
    def __init__(self) -> None:
        super().__init__()
        self.sksize = (20, 70)
        self.skpos = [50, self.winy // 2]
        self.sk = pygame.Surface(self.sksize)
        self.skrect = self.sk.get_rect()
        self.sk_color = pygame.Color(255, 0, 0)
        self.sk.fill(self.sk_color)
        self.direction = None
        self.sk_speed = 10
    
    def draw(self):
        self.surface.blit(self.sk, self.skpos)
    
    def move(self):
        if self.direction == 'up':
            self.skpos[1] -= self.sk_speed
        
        elif self.direction == 'down':
            self.skpos[1] += self.sk_speed
        
    def extremities(self):
        if self.skpos[1] <= self.sksize[1] / 2:
            self.skpos[1] = self.sksize[1] / 2
        
        elif self.skpos[1] >= self.winy - self.sksize[1] * 1.5:
            self.skpos[1] = self.winy - self.sksize[1] * 1.5
    
    def check_skate_collision(self, ball):
        skate_y_range = range(int(self.skpos[1]), int(self.skpos[1] + self.sksize[1]))
        if ball.ballpos[0] == self.skpos[0] + self.sksize[0] and ball.ballpos[1] in skate_y_range:
            sk_area = self.skpos[1] + self.sksize[1]

            if ball.ballpos[1] < sk_area / 2:
                ball.balldirection = 'dright_up'
            elif ball.ballpos[1] > sk_area / 2:
                ball.balldirection = 'dright_down'
            else:  # ball.ballpos[1] == sk_area / 2
                ball.balldirection = 'right'
    
    def restart_position(self):
        self.skpos = [50, self.winy // 2]

class Machine(Setup):
    def __init__(self) -> None:
        super().__init__()
        self.machinesize = (20, 70)
        self.machinepos = [self.winx - 50, self.winy / 2]
        self.machine_color = pygame.Color(0, 100, 0)
        self.machine = pygame.Surface(self.machinesize)
        self.machine.fill(self.machine_color)
        self.direction = None
        self.machine_speed = 10
    
    def draw(self):
        self.surface.blit(self.machine, self.machinepos)
    
    def move(self):
        if self.direction == 'up':
            self.machinepos[1] -= self.machine_speed
        
        elif self.direction == 'down':
            self.machinepos[1] += self.machine_speed
        
    def extremities(self):
        if self.machinepos[1] <= self.machinesize[1] / 2:
            self.machinepos[1] = self.machinesize[1] / 2
        
        elif self.machinepos[1] >= self.winy - self.machinesize[1] * 1.5:
            self.machinepos[1] = self.winy - self.machinesize[1] * 1.5
    
    def check_machine_collision(self, ball):
        machine_y_range = range(
            int(self.machinepos[1]), 
            int(self.machinepos[1] + self.machinesize[1])
        )
        same_x_pos = ball.ballpos[0] == self.machinepos[0] - self.machinesize[0]
        
        if same_x_pos and ball.ballpos[1] in machine_y_range:
            marea = self.machinepos[1] + self.machinesize[1]

            if ball.ballpos[1] < marea / 2:
                ball.balldirection = 'dleft_up'
            elif ball.ballpos[1] > marea / 2:
                ball.balldirection = 'dleft_down'
            else:  # ball.ballpos[1] == marea / 2
                ball.balldirection = 'left'
    
    def restart_position(self):
        self.machinepos = [self.winx - 50, self.winy / 2]


class Ball(Setup):
    def __init__(self) -> None:
        super().__init__()
        self.ballsize = [20, 20]
        self.ballpos = [self.winx / 2, self.winy /2]
        self.ballobj = pygame.Surface(self.ballsize)
        self.ballrect = self.ballobj.get_rect()
        self.ball_color = pygame.Color(100, 100, 100)
        self.ballobj.fill(self.ball_color)
        self.balldirection = random.choice(['left', 'right'])
        self.ball_speed = 10
        
    def draw(self):
        self.surface.blit(self.ballobj, self.ballpos)
        
    def move(self):
        # sizes
        if self.balldirection == 'right':
            self.ballpos[0] += self.ball_speed
            
        elif self.balldirection == 'left':
            self.ballpos[0] -= self.ball_speed
        
        # diagonals to right
        if self.balldirection == 'dright_up':
            self.ballpos[0] += self.ball_speed
            self.ballpos[1] -= self.ball_speed
        
        elif self.balldirection == 'dright_down':
            self.ballpos[0] += self.ball_speed
            self.ballpos[1] += self.ball_speed
        
        # diagonals to left
        if self.balldirection == 'dleft_up':
            self.ballpos[0] -= self.ball_speed
            self.ballpos[1] -= self.ball_speed
        
        elif self.balldirection == 'dleft_down':
            self.ballpos[0] -= self.ball_speed
            self.ballpos[1] += self.ball_speed
            
    def side_collisions(self):
        if self.ballpos[1] <= 0 and self.balldirection == 'dright_up':
            self.balldirection = 'dright_down'
            
        if self.ballpos[1] >= self.winy - self.ballsize[0] * 2 and self.balldirection == 'dright_down':
            self.balldirection = 'dright_up'
        
        if self.ballpos[1] <= 0 and self.balldirection == 'dleft_up':
            self.balldirection = 'dleft_down'
            
        if self.ballpos[1] >= self.winy - self.ballsize[0] * 2 and self.balldirection == 'dleft_down':
            self.balldirection = 'dleft_up'
    
    def restart_position(self):
        if self.ballpos[0] <= 0 or self.ballpos[0] >= self.winx:
            self.__init__()
            
class Points(Ball, Setup):
    def __init__(self) -> None:
        super().__init__()
        self.machine_points = 0
        self.player_points = 0
        self.font = pygame.font.get_default_font()
        self.font = pygame.font.SysFont(self.font, 20)
        
        
    def register_point(self, ballx, *objs):
        if ballx <= 0:
            self.machine_points += 1
            [o.restart_position() for o in objs]
        
        elif ballx >= self.winx:
            self.player_points += 1
            [o.restart_position() for o in objs]
    
    def show_points(self):
        cor = pygame.Color(255, 255, 255)
        mach = self.font.render(f'Machine points: {self.machine_points}', False, cor)
        play = self.font.render(f'Player points: {self.player_points}', False, cor)
        
        self.surface.blit(mach, (self.winx - 170, 50))
        self.surface.blit(play, (50, 50))