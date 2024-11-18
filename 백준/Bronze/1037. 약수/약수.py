import sys
input=sys.stdin.readline

n = int(input())
mea = list(map(int, input().split()))
a = min(mea)
b = max(mea)
print(a*b)