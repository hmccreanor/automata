import pygame
import sys
import math
import numpy as np

def rule_map(n):
    binary = bin(n)[2:]
    leading_zeros = (8 - len(binary)) * "0"
    binary = leading_zeros + binary
    patterns = ["111", "110", "101", "100", "011", "010", "001", "000"]
    return dict(zip(patterns, binary))

def apply_rule(row, rule):
    padded_row = np.append(np.insert(row, 0, 0), 0)
    patterns = [str(padded_row[i - 1]) + str(padded_row[i]) + str(padded_row[i + 1]) for i in range(1, len(padded_row) - 1)]
    new_row = [rule[pattern] for pattern in patterns]
    return new_row

rule_number = int(sys.argv[1])
rule = rule_map(rule_number)

window_dims = (495, 500)

state = np.zeros((100, 99)).astype(int)

pygame.init()

screen = pygame.display.set_mode(window_dims)

alive = pygame.Color(0, 0, 0)

cell = pygame.Rect(0, 0, 5, 5)

current_row = 0

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
            elif event.key == pygame.K_r:
                state = np.zeros((100, 99)).astype(int)
                playing = False

        if not playing:
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicking = True
                pos = pygame.mouse.get_pos()
                x = math.floor(pos[0] / 5) 
                y = math.floor(pos[1] / 5)
                state[y][x] = 0 if state[y][x] == 1 else 1
            elif event.type == pygame.MOUSEBUTTONUP:
                clicking = False
            elif event.type == pygame.MOUSEMOTION:
                if clicking:
                    pos = pygame.mouse.get_pos()
                    x = math.floor(pos[0] / 5) 
                    y = math.floor(pos[1] / 5)
                    if x != last_clicked_x or y != last_clicked_y:
                        state[y][x] = 0 if state[y][x] == 1 else 1
                        last_clicked_x = x
                        last_clicked_y = y

 
    # Update state
    if current_row != state.shape[0] - 1 and playing:
        state[current_row + 1] = apply_rule(state[current_row], rule)
        current_row += 1
    elif current_row == state.shape[0] - 1 and playing:
        current_row = 0
        playing = False

    screen.fill((255, 255, 255))

    # Draw horizontal lines
    for y in range(state.shape[0]):
        pygame.draw.line(screen, (0, 0, 0), (0, y * 5), (window_dims[0], y * 5))

    # Draw vertical lines
    for x in range(state.shape[1]):
        pygame.draw.line(screen, (0, 0, 0), (x * 5, 0), (x * 5, window_dims[1]))

    # Draw cells
    for y in range(state.shape[0]):
        for x in range(state.shape[1]):
            if state[y][x] == 1:
                pygame.draw.rect(screen, alive, cell.move(x * 5, y * 5))



    pygame.display.flip()
