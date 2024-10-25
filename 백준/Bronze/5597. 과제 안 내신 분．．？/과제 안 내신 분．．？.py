a=[]
e=[]
for b in range(28):
    a.append(int(input()))
a.sort()

for c in range(1,31):
  for d in range(len(a)):
    if c == a[d]:
      break
    if d == len(a)-1 and c != a[d]:
      e.append(c)  
for q in range(len(e)):
  print(e[q])      