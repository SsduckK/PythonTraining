import numpy as np
import cv2

class Visualizer:
    def __init__(self):
        self.image_board = self.load_board()

    @staticmethod
    def load_board():
        board = np.zeros((500, 500, 3))
        return board

    def visualize(self):
        cv2.imshow("image", self.image_board)
        cv2.waitKey()


def main():
    vis = Visualizer()
    vis.visualize()


if __name__ == "__main__":
    main()
