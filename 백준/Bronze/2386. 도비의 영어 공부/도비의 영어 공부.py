cnt=0
while 1:
  cnt=0
  a=input()
  if a == '#':
    break
  so=a[0]
  alpha=a[2:-1]
  for i in alpha.lower():
    if so==i:
      cnt=cnt+1    
  print(a[0], cnt)      