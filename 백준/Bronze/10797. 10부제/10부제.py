import sys
input=sys.stdin.readline

n = int(input())
car = list(map(int, input().split()))
print(car.count(n))