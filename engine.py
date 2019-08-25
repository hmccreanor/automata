'''
Pretty basic automata engine
Takes in a 2d matrix of 1s and 0s
Should be able to draw matrix to screen
Moving/scaling should also be implemented
'''

import cv2
import numpy as np

size = [640, 480]

while True:
    cells = np.random.randint(2, size = size).astype(float)

    cv2.imshow("Cells", cells)

    if cv2.waitKey(50) & 0xFF == ord("q"):
        break


cv2.destroyAllWindows()
