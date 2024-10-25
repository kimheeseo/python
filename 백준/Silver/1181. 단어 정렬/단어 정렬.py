a=int(input())
b=[]
for c in range(a):
  d=input()
  b.append(d)
e=list(set(b))
e.sort()
e=sorted(e,key=len)

for i in range(len(e)):
  print(e[i])