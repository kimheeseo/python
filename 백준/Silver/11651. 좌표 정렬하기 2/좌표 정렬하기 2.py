a = int(input())
d=[]

for i in range(a):
  [a,b]=map(int, input().split())
  d.append([b,a])
d.sort()

for i in d:
  print(i[1],i[0])