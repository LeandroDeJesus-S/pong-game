import random

import pygame

from setup.main import Setup
from setup.objects import Skate, Machine, Ball, Points

setup = Setup()
setup.starter()

skate = Skate()
machine = Machine()
ball = Ball()
points = Points()

while True:
    setup.set_fps()
    setup.set_bg()
    
    for current_event in pygame.event.get():
        if current_event.type == pygame.QUIT:
            pygame.quit()
            break
        
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            machine.direction = 'down'
        
        elif key[pygame.K_UP]:
            machine.direction = 'up'
        
        else:
            machine.direction = None
        
        if key[pygame.K_s]:
            skate.direction = 'down'
        
        elif key[pygame.K_w]:
            skate.direction = 'up'
        
        else:
            skate.direction = None
    
    skate.draw()
    skate.move()
    skate.extremities()
    
    machine.draw()
    machine.move()
    machine.extremities()
    
    skate.check_skate_collision(ball)
    machine.check_machine_collision(ball)
    
    if ball.ballpos[0] <= 0 or ball.ballpos[0] >= setup.winx:
        machine.restart_position()
        skate.restart_position()
    
    ball.draw()
    ball.move()
    ball.side_collisions()
    
    points.register_point(ball.ballpos[0], ball, machine, skate)
    
    points.show_points()
    
    setup.update()
