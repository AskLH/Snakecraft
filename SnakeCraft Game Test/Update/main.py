import pygame
import sys
import random
#from Orea import Ore
from Diamond import Diamond
from Gold import Gold
from Iron import Iron
from Coal import Coal
from Screen import drawGrid

class Snake():
    def __init__(self):
        self.length = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (17, 24, 47)

        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x,y = self.direction
        new = (((cur[0]+(x*gridsize))%screen_width), (cur[1]+(y*gridsize))%screen_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw(self,surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (0, 0, 0), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)




screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize

up = (0,-1)
down = (0,1)
left = (-1,0)
right = (1,0)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake()

    list = [Diamond, Gold, Iron, Coal, Coal, Coal, Coal, Iron, Iron, Gold]
    Ore = random.choice(list)
    ore = Ore()

    myfont = pygame.font.SysFont("monospace",16)

    while (True):
        clock.tick(10)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        if snake.get_head_position() == ore.position:
            snake.length += 1
            snake.score += 1
            del ore
            Ore = random.choice(list)
            ore = Ore()
        snake.draw(surface)
        ore.draw(surface)
        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(snake.score), 1, (0,0,0))
        screen.blit(text, (5,10))
        pygame.display.update()
main()