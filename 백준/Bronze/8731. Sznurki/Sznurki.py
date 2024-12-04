import sys
input=sys.stdin.readline

def max_ropes(n, w, ropes):
    count = 0
    current_sum = 0
    
    for rope in ropes:
        current_sum += rope
        if current_sum >= w:
            count += 1
            current_sum = 0
    return count

# 입력 받기
n, w = map(int, input().split())
ropes = list(map(int, input().split()))

# 결과 출력
result = max_ropes(n, w, ropes)
print(result)