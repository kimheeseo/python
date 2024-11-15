a=int(input())

for i in range(a):
  b=list(map(int, input().split()))[1:]
  cnt=sum(b[0:])
  cnt1=0
  for i in range(len(b)):
    if b[i] % 2 ==0:
      cnt1=cnt1+b[i]

  if cnt-cnt1 > cnt1:
    print("ODD")
  elif cnt-cnt1<cnt1:
    print("EVEN")
  elif cnt-cnt1 == cnt1:
    print("TIE")