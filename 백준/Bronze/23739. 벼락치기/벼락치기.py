import sys

input = sys.stdin.readline

N = int(input().strip())
T = [int(input().strip()) for _ in range(N)]

spent = [0] * N  # 각 챕터에 실제로 투입된 공부 시간
i = 0            # 현재 챕터 인덱스 (0-based)

while i < N:
    t = 30  # 한 블록(30분)
    # 블록 내에서 가능한 만큼 진행
    while t > 0 and i < N:
        if T[i] <= t:
            # 챕터를 블록 내에서 완주
            spent[i] = T[i]
            t -= T[i]
            i += 1
        else:
            # 챕터를 부분 학습하고 블록 종료와 함께 챕터를 '덮고' 다음으로 이동
            spent[i] = t
            t = 0
            i += 1  # 다음 블록은 다음 챕터부터
    # 블록 종료 -> 다음 블록으로

# 절반 이상 공부한 챕터 수
answer = sum(1 for s, ti in zip(spent, T) if s * 2 >= ti)
print(answer)