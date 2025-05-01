# IOU

---
- IOU(Intersection over Union) 란 GT 박스와 prediction box 의 비교를 통한 Object Detection 의 성능을 검증하는 방법 중 하나이다.
- Object Detection 에서는 주로 GT Box 와 Prediction 사이의 면적을 이용해서 비교한다.

- 참조
  - Jaccard Similarity
    -  A, B 두 집합에 대해서 얼마나 유사한지 나타내는 지표
    - $$
J(A, B) = \frac{|A \cap B|}{|A \cup B|} = \frac{|A \cap B|}{|A| + |B| - |A ∩ B|}
$$