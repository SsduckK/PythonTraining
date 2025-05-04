import numpy as np
import cv2


class Visualizer:
    def __init__(self):
        self.image_board = self.load_board()
        self.gt_color = (255, 0, 0)
        self.pred_color = (0, 0, 255)

    @staticmethod
    def load_board():
        board = np.zeros((500, 500, 3))   #TODO Create by image size
        return board

    def draw_bboxes(self, bboxes):
        for box in bboxes:
            gt_box, pred_box, class_id = self.split_bbox_info(box)
            self.image_board = cv2.rectangle(self.image_board,
                                             (gt_box[0], gt_box[1]), (gt_box[2], gt_box[3]),
                                             self.gt_color, 2)
            self.image_board = cv2.rectangle(self.image_board,
                                             (pred_box[0], pred_box[1]), (pred_box[2], pred_box[3]),
                                             self.pred_color, 2)

    def split_bbox_info(self, box):
        gt = box[:4]
        pred = box[4:8]
        class_id = box[-1]

        return gt, pred, class_id


    def visualize(self):
        cv2.imshow("image", self.image_board)
        cv2.waitKey()


def main():
    vis = Visualizer()
    vis.visualize()


if __name__ == "__main__":
    main()
