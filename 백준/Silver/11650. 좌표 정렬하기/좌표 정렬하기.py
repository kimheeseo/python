a=int(input())
d=[]

for i in range(a):
  [b,c]=map(int, input().split())
  d.append([b,c])
d=sorted(d)
for i in d:
  print(i[0], i[1])