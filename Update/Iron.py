import pygame
import random


screen_width = 480
screen_height = 480
image = pygame.image.load()
gridsize = 20
grid_width = screen_width / gridsize
grid_height = screen_height / gridsize

class Iron():
    def __init__(self):
        self.position = (0,0)
        self.color = (166, 164, 151)
        self.randomize_position()


    def randomize_position(self):
        self.position = (random.randint(0, grid_width-1)*gridsize, random.randint(0, grid_height-1)*gridsize)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        surface.blit(self.image,r)
        pygame.draw.rect(surface, (0, 0, 0), r, 1)