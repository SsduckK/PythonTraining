import numpy as np

class IOU:
    def __init__(self, gt_bboxes, pred_bboxes):
        self.gt_bboxes = gt_bboxes
        self.pred_bboxes = pred_bboxes

    def calculate_iou(self):
        filtered_bboxes = self.matching_bboxes(self.gt_bboxes, self.pred_bboxes)

    def matching_bboxes(self, gt_bboxes, pred_bboxes):
        bboxes_matrix = self.create_bboxes_matrix(gt_bboxes, pred_bboxes)
        filtered_bboxes = self.filter_by_class(bboxes_matrix)
        return filtered_bboxes

    def create_bboxes_matrix(self, gt_bboxes, pred_bboxes):
        return None

    def filter_by_class(self, bboxes_matrix):
        return None
