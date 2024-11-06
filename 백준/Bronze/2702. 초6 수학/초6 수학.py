nn=int(input())

for i in range(nn):

  a, b=map(int, input().split())
  temp=0

  if a<b:
    temp=b
    b=a
    a=temp

  min=b
  max=a

  for i in range(b,-1,-1):
    if a%i==0 and b%i==0:
      min=i #최대 공약수
#      print('min값:', min)
#      print('max값:',int((a*b)/min))
      print(int((a*b)/min), min)
      break
    
