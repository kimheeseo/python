on = []
people = 0

for _ in range(4):
    a, b = map(int, input().split())
    people += b # 탄 사람 수
    people -= a # 내린 사람 수
    on.append(people)

print(max(on))