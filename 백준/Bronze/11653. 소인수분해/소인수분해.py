a=int(input())
d=[]


for i in range(2,a+1):
  while 1:
    if a%i==0:
      d.append(i)
      a=a//i
      print(i)
    else:
      break