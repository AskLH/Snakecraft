import pygame

screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width / gridsize
grid_height = screen_height / gridsize

def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x+y)%2 == 0:
                r = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface,(168,154,142), r)
            else:
                rr = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface, (136, 140, 141), rr)