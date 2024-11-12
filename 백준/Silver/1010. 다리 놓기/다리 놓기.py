import sys
input=sys.stdin.readline
# 해당 방법이 MCN을 사용하는 이유: 강 서쪽의 N개가 M개 중 어떤 것과 연결할지를 나타내니까.

def factorial(N):
    if N > 1:
        return (N * factorial(N-1))
    else:
        return 1

T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    print (factorial(M) //  (factorial(M-N) * factorial(N)))