import math
import numpy as np
import pygame
import sys
import time

window_dims = (640, 480)
state = np.zeros((48, 64))

pygame.init()

screen = pygame.display.set_mode(window_dims)

dead = pygame.Color(255, 255, 255)
alive = pygame.Color(0, 0, 0)

cell = pygame.Rect(0, 0, 10, 10)

def neighbours(s, x, y):
    n = 0
    for i in range(y - 1, y + 2):    
        for j in range(x - 1, x + 2):
            try:
                n += s[i][j]
            except:
                pass
    
    n -= s[y][x]

    return n

def tick(s):
    next = s.copy()
    for y in range(s.shape[0]):
        for x in range(s.shape[1]):
            n_neighbours = neighbours(s, x, y)

            if s[y][x] == 1 and (n_neighbours < 2 or n_neighbours > 3):
                next[y][x] = 0
            elif s[y][x] == 1 and (n_neighbours == 2 or n_neighbours == 3):
                next[y][x] = 1
            elif s[y][x] == 0 and n_neighbours == 3:
                next[y][x] = 1

    return next

playing = False
clicking = False

last_clicked_x = None
last_clicked_y = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playing = not playing

        if not playing:
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicking = True
                pos = pygame.mouse.get_pos()
                x = math.floor(pos[0] / 10) 
                y = math.floor(pos[1] / 10)
                state[y][x] = 0 if state[y][x] == 1 else 1
            elif event.type == pygame.MOUSEBUTTONUP:
                clicking = False
            elif event.type == pygame.MOUSEMOTION:
                if clicking:
                    pos = pygame.mouse.get_pos()
                    x = math.floor(pos[0] / 10) 
                    y = math.floor(pos[1] / 10)
                    if x != last_clicked_x or y != last_clicked_y:
                        state[y][x] = 0 if state[y][x] == 1 else 1
                        last_clicked_x = x
                        last_clicked_y = y

    if playing:
        state = tick(state)

    screen.fill((255, 255, 255)) 

    # Draw gridlines
    for y in range(state.shape[0]):
        pygame.draw.line(screen, (0, 0, 0), (0, y * 10), (window_dims[0], y * 10))

    for x in range(state.shape[1]):
        pygame.draw.line(screen, (0, 0, 0), (x * 10, 0), (x * 10, window_dims[1]))

    # Draw cells
    for y in range(state.shape[0]):
        for x in range(state.shape[1]):
            if state[y][x] == 1:
                pygame.draw.rect(screen, alive, cell.move(10 * x, 10 * y))
    
    pygame.display.flip()
