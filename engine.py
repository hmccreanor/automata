'''
Pretty basic automata engine
Takes in a 2d matrix of 1s and 0s
Should be able to draw matrix to screen
Moving/scaling should also be implemented
'''

import numpy as np
import pygame

pygame.init()

size = [640, 480]

screen = pygame.display.set_mode(size)

test_matrix = np.random.randint(2, size = size[::-1])
print(test_matrix)

playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    screen.fill((255, 255, 255))

    for y in range(test_matrix.shape[0]):
        for x in range(test_matrix.shape[1]):
            if test_matrix[y][x] == 0:
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x, y, 1, 1))
            else:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, 1, 1))

    pygame.display.flip()
