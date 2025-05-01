import numpy as np

# Ground Truth: [x_min, y_min, x_max, y_max, class_id]
gt_boxes = np.array([
    [50, 50, 150, 150, 1],   # 사람
    [30, 30, 100, 100, 2],   # 자동차
    [200, 200, 300, 300, 1], # 사람
])

# prediction: [x_min, y_min, x_max, y_max, class_id]
pred_boxes = np.array([
    [55, 55, 145, 145, 1],   # 사람 (매칭될 것) 
    [25, 25, 105, 105, 2],   # 자동차 (매칭될 것)
    [190, 190, 310, 310, 2], # 자동차 (클래스 불일치)
    [205, 205, 295, 295, 1], # 사람 (매칭될 것)
])