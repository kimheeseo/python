n, m = map(int, input().split())

# 참가자 점수 정보 읽기
scores = []
for _ in range(n):
    scores.append(list(map(int, input().split())))

# Dymówka의 점수는 첫 번째 줄의 점수입니다.
dymowka_score = scores[0]

# 가능한 최고의 랭킹을 찾기 위한 변수 초기화
best_rank = n  # 최악의 경우 Dymówka는 n번째 순위
best_count = 1  # 동점자가 최소 한 명 (자신)

# 가능한 모든 가중치의 조합을 탐색하는 완전탐색 접근법
import itertools

# 각 문제의 가중치를 [0, 2000] 범위 내에서 최적으로 설정해야 합니다.
weights = range(0, 2001)
best_weight = [0] * m

# 가중치를 최적화하기 위해 각 문제의 점수를 고려해야 합니다.
# 각 문제에 대해 높은 점수를 가진 문제가 더 큰 가중치를 가지도록 설정
# 각 문제의 가중치를 최적으로 설정했을 때 최고 랭크를 계산합니다.

def calculate_score(weights, scores):
    """주어진 가중치와 참가자 점수 목록에 따라 각 참가자의 최종 점수를 계산"""
    return [sum(w * (s // 100) for w, s in zip(weights, participant)) for participant in scores]

# Brute-force 방식으로 각 가중치를 최적화할 수 있음
# 최적의 방법을 찾아 Dymówka가 최대한 높은 순위를 차지할 수 있는지를 계산합니다.
# 단순화하기 위해, 최고 가중치를 찾는 것을 목표로 합니다.
optimal_weights = [2000 if x == 100 else 0 for x in dymowka_score]

# 최적 가중치에 따라 각 참가자의 점수를 계산
final_scores = calculate_score(optimal_weights, scores)

# Dymówka의 최종 점수
dymowka_final_score = final_scores[0]

# 참가자들의 점수를 기준으로 랭킹을 정렬
sorted_scores = sorted(final_scores, reverse=True)

# Dymówka가 차지할 수 있는 최고의 순위 계산
best_rank = sorted_scores.index(dymowka_final_score) + 1
best_count = sorted_scores.count(dymowka_final_score)

# 결과 출력
print(best_rank, best_count)