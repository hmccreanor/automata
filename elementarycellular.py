'''
Implementation of several cellular automata found on the Wolfram MathWorld website

Rules are loaded in from an external .txt rulesfile, where we assume that the rules are encoded in a standard form.
If this is the case (and we assume it to be so), then each rule can just be encoded as a single byte

The standard form is as follows:
    - Each bit b[i] is the response of the automata to pattern p[i]
    - The index of the row is the rule number i.e row 2 is the encoding of rule 2

The pattern array is as follows:
[[1, 1, 1],
 [1, 1, 0],
 [1, 0, 1],
 [1, 0, 0],
 [0, 1, 1],
 [0, 1, 0],
 [0, 0, 1],
 [0, 0, 0]]

'''

import numpy as np
from viewer import CanvasViewer
import sys

rule_to_apply = int(sys.argv[1]) - 1

rules = {}

patterns = [(1, 1, 1),
            (1, 1, 0),
            (1, 0, 1),
            (1, 0, 0),
            (0, 1, 1),
            (0, 1, 0),
            (0, 0, 1),
            (0, 0, 0)]

for i in range(256):
    rules[i] = {} # Instantiate rule
    rule = list(map(int, "{0:{fill}8b}".format(i, fill = 0)))
    for j, pattern in enumerate(patterns):
        rules[i][pattern] = rule[j]


'''
rules = {30: {(1, 1, 1): 0,
              (1, 1, 0): 0,
              (1, 0, 1): 0,
              (1, 0, 0): 1,
              (0, 1, 1): 1,
              (0, 1, 0): 1,
              (0, 0, 1): 1,
              (0, 0, 0): 0}}
'''

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
    if row_id < 16 - 1:
        canvas[row_id + 1, :] = apply_rule(rule_to_apply, canvas[row_id])
        row_id += 1

    viewer.canvas = canvas
    viewer.draw()
    exit = viewer.respondToKeys(1000)

