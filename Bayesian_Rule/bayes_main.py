import numpy as np

# 인구 수
n = 1000

# 확률 설정
p_cancer = 0.001       # 암일 확률
p_positive_given_cancer = 0.99
p_positive_given_healthy = 0.05

# 무작위 인구 생성
# 1은 암, 0은 건강
#np.random.seed(42)  # 재현성
population = np.random.choice([1, 0], size=n, p=[p_cancer, 1 - p_cancer])

# 검사 결과 생성
test_results = []

for person in population:
    if person == 1:  # 암 환자
        result = np.random.choice([1, 0], p=[p_positive_given_cancer, 1 - p_positive_given_cancer])
    else:  # 건강한 사람
        result = np.random.choice([1, 0], p=[p_positive_given_healthy, 1 - p_positive_given_healthy])
    test_results.append(result)

# numpy 배열로 변환
population = np.array(population)
test_results = np.array(test_results)

# 통계 계산
true_positives = np.sum((population == 1) & (test_results == 1))
false_positives = np.sum((population == 0) & (test_results == 1))
total_positives = np.sum(test_results == 1)

# 베이즈 정리 기반 확률 계산
if total_positives > 0:
    posterior = true_positives / total_positives
else:
    posterior = 0

# 출력
print(f"양성자 수: {total_positives}")
print(f"그 중 실제 암 환자 수: {true_positives}")
print(f"P(암 | 양성) ≈ {posterior:.4f} (≈ {posterior*100:.2f}%)")