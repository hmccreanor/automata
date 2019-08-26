'''
Pretty basic automata engine
Takes in a 2d matrix of 1s and 0s
Should be able to draw matrix to screen
Moving/scaling should also be implemented

The way I plan on implementing scaling is for there to be the concept of a canvas
Only a slice of the canvas is displayed at any given time.
Scaling/moving across the image will just correspond to changing the parameters of our slicing function
'''

import cv2
import numpy as np

window_size = (640, 480)
canvas_size = [640, 480]

def canvas_slice(c, top_left_coords, slice_dims):
    return c[top_left_coords[1] : top_left_coords[1] + slice_dims[1], top_left_coords[0] : top_left_coords[0] + slice_dims[0]]

frame_coord = np.array([0, 0])
frame_dims = np.array([100, 100])

cells = np.random.randint(2, size = canvas_size).astype(float)

while True:

    cv2.imshow("Cells", cv2.resize(canvas_slice(cells, frame_coord, frame_dims), window_size, interpolation = cv2.INTER_NEAREST))

    key = chr(cv2.waitKey(1000) & 0xFF)

    if key == "x":
        break
    elif key == "a":
        if frame_coord[0] > 0:
            frame_coord[0] -= 1
    elif key == "d":
        if frame_coord[0] < canvas_size[0]:
            frame_coord[0] += 1
    elif key == "s":
        if frame_coord[1] < canvas_size[1]:
            frame_coord[1] += 1
    elif key == "w":
        if frame_coord[1] > 0:
            frame_coord[1] -= 1
    elif key == "q":
        frame_dims *= 2
    elif key == "e":
        frame_dims //= 2

cv2.destroyAllWindows()
