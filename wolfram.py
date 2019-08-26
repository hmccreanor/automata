'''
Implementation of several cellular automata found on the Wolfram MathWorld website
'''

import numpy as np
from viewer import CanvasViewer

rules = {30: {(1, 1, 1): 0,
              (1, 1, 0): 0,
              (1, 0, 1): 0,
              (1, 0, 0): 1,
              (0, 1, 1): 1,
              (0, 1, 0): 1,
              (0, 0, 1): 1,
              (0, 0, 0): 0}}

row_id = 0

def apply_rule(rule, row):
    rule_dict = rules[rule]

    l = 0
    r = 3

    split = np.zeros(len(row))
    row = np.concatenate([[0], row, [0]])

    for i in range(len(row) - 2):
        split[i] = rule_dict[tuple(row[l : r])]

        l += 1
        r += 1

    return split

canvas = np.zeros([16, 31])
canvas[0][15] = 1

viewer = CanvasViewer(canvas, (640, 480), [0, 0], [16, 31])

exit = False

while not exit:
    print(row_id)
    if row_id < 16 - 1:
        canvas[row_id + 1, :] = apply_rule(30, canvas[row_id])
        row_id += 1

    viewer.canvas = canvas
    viewer.draw()
    exit = viewer.respondToKeys(1000)

