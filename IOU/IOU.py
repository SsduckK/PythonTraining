import numpy as np
from sample import *

class IOU:
    def __init__(self, gt_bboxes, pred_bboxes, threshold=0.5):
        self.gt_bboxes = gt_bboxes
        self.pred_bboxes = pred_bboxes
        self.threshold = threshold

    def calculate_iou(self):
        filtered_bboxes = self.matching_bboxes(self.gt_bboxes, self.pred_bboxes)
        non_zero_mask = np.all(filtered_bboxes, axis=-1)
        valid_index = np.where(non_zero_mask == True)

        valid_iou_list = []
        for i in range(len(self.gt_bboxes)):
            valid_iou_list.append(filtered_bboxes[valid_index[0][i]][valid_index[1][i]]) # N x 9
            # gt x1, y1, x2, y2, pred x1, y1, x2, y2, class_id

        return valid_iou_list

    def matching_bboxes(self, gt_bboxes, pred_bboxes):
        score_matrix, bboxes_pair = self.create_bboxes_matrix(gt_bboxes[:, :4], pred_bboxes[:, :4])
        class_id_matrix = self.create_class_matrix(gt_bboxes[:, 4], pred_bboxes[:, 4])
        filtered_bboxes = self.filter_by_class(score_matrix, class_id_matrix, bboxes_pair)
        return filtered_bboxes

    def create_bboxes_matrix(self, gt, pred):
        gt_bboxes = gt[:, np.newaxis, :]
        pred_bboxes = pred[np.newaxis, :]

        x1 = np.maximum(gt_bboxes[..., 0], pred_bboxes[..., 0])
        y1 = np.maximum(gt_bboxes[..., 1], pred_bboxes[..., 1])
        x2 = np.minimum(gt_bboxes[..., 2], pred_bboxes[..., 2])
        y2 = np.minimum(gt_bboxes[..., 3], pred_bboxes[..., 3])

        inter_x = np.maximum(0, x2 - x1)
        inter_y = np.maximum(0, y2 - y1)

        inter_area = inter_x * inter_y

        gt_area = (gt_bboxes[..., 2] - gt_bboxes[..., 0]) * (gt_bboxes[..., 3] - gt_bboxes[..., 1])
        pred_area = (pred_bboxes[..., 2] - pred_bboxes[..., 0]) * (pred_bboxes[..., 3] - pred_bboxes[..., 1])

        union_area = gt_area + pred_area - inter_area

        iou_score = inter_area / union_area

        gt_b = np.repeat(gt_bboxes, repeats=4, axis=1)    # (3, 4, 4)
        pred_b = np.repeat(pred_bboxes, repeats=3, axis=0)  # (3, 4, 4)
        
        concatenated_pair = np.concatenate([gt_b, pred_b], axis=-1)  # (3, 4, 8)

        return iou_score, concatenated_pair

    def create_class_matrix(self, gt, pred):
        gt_classes = gt[:, np.newaxis]
        pred_classes = pred[np.newaxis, :]
        matched_class_mask = gt_classes == pred_classes
        class_id_matrix = gt_classes * matched_class_mask

        return class_id_matrix

    def filter_by_class(self, score_matrix, class_id_matrix, bboxes_pair):
        score_mask = score_matrix > self.threshold

        valid_class_matrix = (class_id_matrix * score_mask)
        class_score_filter = score_mask * valid_class_matrix
        valid_bboxes_pair = class_score_filter[..., np.newaxis] * bboxes_pair
        valid_bboxes_pair = np.concatenate([valid_bboxes_pair, valid_class_matrix[..., np.newaxis]], axis=-1)

        return valid_bboxes_pair


if __name__ == "__main__":
    test_iou = IOU(gt_boxes, pred_boxes)
    test_iou.calculate_iou()


