# File created by: JT Wilcox 
# creates pygame
import pygame 
from pygame.sprite import Sprite
from os import path
from math import floor
pygame.init()
# dimensions of the screen
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
# indicates where the countdown should start from
counter, text = 7, '7'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
# font size and shape
font = pygame.font.SysFont('Arial', 100)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT: 
            # subracts one every second
            counter -= 1
            # if the timer is less than 1 it will print this
            text = str(counter).rjust(3) if counter > 0 else 'You lost :('
        if e.type == pygame.QUIT: 
            run = False
# color is background
    screen.fill((255, 255, 255))
    # location of the text
    screen.blit(font.render(text, True, (0, 0, 0)), (185, 175))
    pygame.display.flip()
    clock.tick(60)