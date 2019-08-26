import cv2
import numpy as np

class CanvasViewer:

    def __init__(self, canvas, window_size, frame_pos, frame_size):
        self.canvas_size = canvas.shape
        self.canvas = canvas
        self.window_size = tuple(window_size)
        self.frame_pos = np.array(frame_pos)
        self.frame_size = np.array(frame_size)

    def draw(self):
        cv2.imshow("CanvasViewer", cv2.resize(self.getSlice(), self.window_size, interpolation = cv2.INTER_NEAREST))

    def getSlice(self):
        return self.canvas[self.frame_pos[1] : self.frame_pos[1] + self.frame_size[1], self.frame_pos[0] : self.frame_pos[0] + self.frame_size[0]]

    # Returns the boolean variable exit, which, if True, indicates that the exit key has been pressed and the simulation should terminate
    def respondToKeys(self, t):
        key = chr(cv2.waitKey(t) & 0xFF)

        if key == "x":
            cv2.destroyAllWindows()
            return True
        elif key == "a":
            if self.frame_pos[0] > 0:
                self.frame_pos[0] -= 1
        elif key == "d":
            if self.frame_pos[0] < self.canvas_size[0]:
                self.frame_pos[0] += 1
        elif key == "s":
            if self.frame_pos[1] < self.canvas_size[1]:
                self.frame_pos[1] += 1
        elif key == "w":
            if self.frame_pos[1] > 0:
                self.frame_pos[1] -= 1
        elif key == "q":
            self.frame_size *= 2
        elif key == "e":
            self.frame_size //= 2

        return False
