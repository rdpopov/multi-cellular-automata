import pygame
import numpy as np
from random import random as random
from random import seed as seed

# cell triple of integers in this format (a,x,y)
# a : either 0 or 1
# x,y: represen a direction vector 

seed(42069)
dd = (800, 800)
cellsx = 10
cellsy = 10
CW = dd[0] // cellsx
CH = dd[1] // cellsy
COLOR = 0x1f1f1f


def dir_vect(cell,cx,cy):
    cntr = (cx + CW//2, cy + CH // 2)
    end = (cntr[0] + CW//2 * cell[0],cntr[1] + CH//2 * cell[1])
    return cntr, end


def render_cell(s, grid, cx, cy):
    if np.all(grid[cx][cy]):
        r = pygame.Rect(cx * CW, cy * CH, CW, CH)
        pygame.draw.rect(s, COLOR, r)
        cntr,end = dir_vect(grid[cx][cy],cx * CW, cy * CH)
        pygame.draw.line(s, 0xffffff, cntr,end )

def random_dir():
    if random() > 0.5:
        return np.array([0,0])
    x = random()
    if random() > 0.5:
        x = -x
    y = (1 - x**2) ** 0.5
    if random() > 0.5:
        y = -y
    return np.array([x,y])



def gen_grid(sz,init=True):
    rows = sz[0] // CW
    cols = sz[1] // CH
    if init:
        return [list(map(lambda x: random_dir(), rows*[0])) for i in range(cols)]
    else:
        return [list(map(lambda x: np.array([0, 0]), rows*[0])) for i in range(cols)]


def main():

    pygame.init()

    # dd = (80, 80)
    screen = pygame.display.set_mode(dd)
    clock = pygame.time.Clock()
    running = True

    grid = gen_grid(dd)
    # print(grid)
    for x in range(cellsx//2):
        for y in range(cellsy//2):
            render_cell(screen, grid,x+3,y+3)

    while running:
        # pygame.draw.rect(screen,255,pygame.Rect(20,20,20,20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(60)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
