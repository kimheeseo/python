import sys
a=int(input()) # 테스트 케이스의 개수

for aa in range(a):
    b,c=map(int, sys.stdin.readline().split())
    print(b+c)