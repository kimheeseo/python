n = int(input())
numbers = list(map(int, input().split()))

# 수열이 1부터 n까지의 숫자를 정확히 포함하는지 확인
if sorted(numbers) == list(range(1, n + 1)):
    print("TAK")
else:
    print("NIE")