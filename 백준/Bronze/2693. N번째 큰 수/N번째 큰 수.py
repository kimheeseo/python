n=int(input()) # 테스트 케이스의 수
for i in range(n):
  a=list(map(int, input().split()))
  a.sort()
  print(a[-3])