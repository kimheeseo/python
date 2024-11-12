import sys
input=sys.stdin.readline
passenger = 0
max_passenger = 0

for _ in range(10):
    out_train, in_train  = map(int, input().split()) 
    passenger += in_train - out_train 
    max_passenger = max(passenger, max_passenger) 
# append 한 다음에, max값을 도출하거나, max_passenger의 값으로 설정한 다음에,
# for문을 통해, 최댓값 구하기
print(max_passenger)