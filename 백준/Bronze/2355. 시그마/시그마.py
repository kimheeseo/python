a, b = map(int, input().split())

# a와 b의 대소 관계를 정리
start = min(a, b)
end = max(a, b)

# 합계 계산
bb = end * (end + 1) // 2
aa = (start - 1) * start // 2
print(bb - aa)