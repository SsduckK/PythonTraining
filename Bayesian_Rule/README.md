# Bayes Rule

---

- 아래 두 가지를 통해 사건 B가 관측되었을 떄 A가 일어났을 확률을 계산 : P(A|B)
  - 사건 A가 일어났을 때 사건 B가 일어날 확률 : P(B|A)
  - 사건 A가 일어날 확률 : P(A)
- 조건부 확률의 역에 대해서 다루는 개념으로 이해해도 좋다.

$$P(A|B) = {P(B|A) \cdot P(A) \over P(B)} $$

- P(A) = 사건 A가 발생 했을 사전 확률
- P(B) = 사건 B가 발생 했을 전체 확률
- P(A|B) = 사건 B가 발생 했을 때 A가 발생 했을 확률 : 우리가 원하는 값
- P(B|A) = 사건 A가 발생 했을 때 B가 발생 했을 확률 : 관측한 정보

## 사전 확률, 전체 확률

### 1. 사전 확률(Prioir Probability)
   - P(A) 를 사전 확률이라 할 경우, A가 발생 하기 전 A에 대한 정보
   - B를 관측하기 전 A가 발생할 가능성에 대한 추정

### 2. 정규화 상수(Evidence)
- Bayes Rule 에서 분모 역할
- 전체 확률이 1이 되도록 정규화 하는 값
- B가 일어날 전체 확률

## 암 검사 예제
- Bayes 정리를 이해하는데 주로 활용되는 암검사 예제
---
- 1,000명 중 1명이 암에 걸린다. -> P(Cancer) = 0.001
- 암 환자가 검사 받으면, 99% 확률로 양성이 나온다. -> P(Positive|Cancer) = 0.99
- 건강한 사람(암 환자가 아님)은 5% 확률로 오진이 발생해 양성이 나온다. -> P(Positive|ㄱCancer) =0.05

- **이때 검사 결과가 양성일 떄 실제로 암일 확률은?? -> P(Cancer|Positive)**

$$P(Cancer|Positive) = {P(Positive|Cancer) \cdot P(Cancer) \over P(Positive)}$$

- P(Cancer) = 0.001
- P(ㄱCancer) = 0.999
- P(Positive|Cancer) = 0.99
- P(Positive|ㄱCancer) = 0.05

- 전체 확률(정규화 상수) P(Positive) 계산
$$P(Positive) = P(Positive|Cancer) \cdot P(Cancer) + P(Positive|ㄱCancer) \cdot P(ㄱCancer)$$
$$=0.99\cdot0.001 + 0.05\cdot0.999 = 0.05094$$

- P(Positive) 로부터 식 대입
$$P(Cancer|Positive) = {0.99 \times 0.001 \over 0.05094} = 0.0194$$
- 약 1.94%

|           | **실제 암 (1명)** | **실제 비암 (999명)** | **합계**  |
| --------- | ------------- | ---------------- | ------- |
| **양성 판정** | 0.99명 (TP)    | 49.95명 (FP)      | 50.94명  |
| **음성 판정** | 0.01명 (FN)    | 949.05명 (TN)     | 949.06명 |
| **합계**    | 1명            | 999명             | 1000명   |


