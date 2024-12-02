condos = []
for i in range(int(input())):
    l, p = map(int, input().split())
    condos.append([l, p])
condos.sort()
cost = 10001
result = 0
for i in condos:
    temp = i[1]
    if temp < cost:
        cost = temp
        result += 1
print(result)

# 해당 문제 풀이법은 우선 바닷가에서 가까운 것을 찾기위해서 sort를 한 다음에
# 가격이 저렴한 것을 찾아야하니까, if temp<cost:를 통해, 짧으면서 가격이 저렴한 것을 찾는다.