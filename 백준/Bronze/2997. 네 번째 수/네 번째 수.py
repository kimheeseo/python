a, b, c = map(int, input().split())
numbers = [a, b, c]
numbers.sort()

# 가능한 공차들을 계산
diffs = [numbers[1] - numbers[0], numbers[2] - numbers[1]]

# 실제 공차 결정
if diffs[0] == diffs[1]:
    diff = diffs[0]
else:
    diff = min(diffs)

# 네 번째 수 찾기
if numbers[1] - numbers[0] != diff:
    fourth = numbers[0] + diff
elif numbers[2] - numbers[1] != diff:
    fourth = numbers[1] + diff
else:
    fourth = numbers[2] + diff

print(fourth)