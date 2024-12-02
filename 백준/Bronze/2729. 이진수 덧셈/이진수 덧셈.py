n=int(input()) # 테스트 케이스의 수
for i in range(n):
  a,b=map(str,input().split())
  a=int(a,2)
  b=int(b,2)
#10진수로 바꿨다가 계산 후 다시 변경  
  c=a+b
  print(bin(c)[2:])