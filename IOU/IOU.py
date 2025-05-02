import numpy as np
from sample import *

class IOU:
    def __init__(self, gt_bboxes, pred_bboxes):
        self.gt_bboxes = gt_bboxes
        self.pred_bboxes = pred_bboxes

    def calculate_iou(self):
        filtered_bboxes = self.matching_bboxes(self.gt_bboxes, self.pred_bboxes)

    def matching_bboxes(self, gt_bboxes, pred_bboxes):
        bboxes_matrix = self.create_bboxes_matrix(gt_bboxes[:, :4], pred_bboxes[:, :4])
        class_matrix = self.create_class_matrix(gt_bboxes[:, 4], pred_bboxes[:, 4])
        filtered_bboxes = self.filter_by_class(bboxes_matrix, class_matrix)
        return filtered_bboxes

    def create_bboxes_matrix(self, gt, pred):
        gt_bboxes = gt[:, np.newaxis, :]
        pred_bboxes = pred[np.newaxis, :]

        x1 = np.maximum(gt_bboxes[..., 0], pred_bboxes[..., 0])
        y1 = np.maximum(gt_bboxes[..., 1], pred_bboxes[..., 1])
        x2 = np.minimum(gt_bboxes[..., 2], pred_bboxes[..., 2])
        y2 = np.minimum(gt_bboxes[..., 3], pred_bboxes[..., 3])

        inter_x = np.abs(x2 - x1)
        inter_y = np.abs(y2 - y1)

        inter_area = inter_x * inter_y

        gt_area = (gt_bboxes[..., 2] - gt_bboxes[..., 0]) * (gt_bboxes[..., 3] - gt_bboxes[..., 1])
        pred_area = (pred_bboxes[..., 2] - pred_bboxes[..., 0]) * (pred_bboxes[..., 3] - pred_bboxes[..., 1])

        union_area = gt_area + pred_area - inter_area

        iou_score = inter_area / union_area

        return iou_score



    def create_class_matrix(self, gt, pred):
        gt_classes = gt[:, np.newaxis]
        pred_classes = pred[np.newaxis, :]

    def filter_by_class(self, bboxes_matrix, class_matrix):
        return None

if __name__ == "__main__":
    test_iou = IOU(gt_boxes, pred_boxes)
    test_iou.calculate_iou()


