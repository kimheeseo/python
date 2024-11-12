num=int(input())

for num2 in range(num):
  a=int(input())

  b=a**2
  a=str(a)
  b=str(b)
  q=len(a)
  cnt=0
  cntt=0
  for i in range(len(b)-len(a),len(b)):
    if a[cnt] !=b[i]:
      print('NO')
      break
    else:
      cntt=cntt+1
      cnt=cnt+1
    if cntt==len(a):
      print('YES')
      break
