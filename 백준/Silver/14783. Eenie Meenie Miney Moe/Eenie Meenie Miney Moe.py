def last_cow_standing(N, sequence):
    cows = list(range(1, N+1))
    current = 0
    
    while len(cows) > 1:
        for step in sequence:
            if len(cows) == 1:
                break
            current = (current + step - 1) % len(cows)
            cows.pop(current)
            if current == len(cows):
                current = 0
    
    return cows[0]

# 입력 처리
N, L = map(int, input().split())
sequence = list(map(int, input().split()))

# 결과 계산 및 출력
result = last_cow_standing(N, sequence)
print(result)