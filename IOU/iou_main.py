from IOU import *
from sample import *
from visualizer import Visualizer

def main():
    iou = IOU(gt_boxes, pred_boxes)
    iou_list = iou.calculate_iou()

    vis = Visualizer()
    vis.draw_bboxes(iou_list)


if __name__ == "__main__":
    main()