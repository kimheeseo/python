a=int(input())
q=[]

for i in range(a):
  q=[]
  b=int(input())
  for i in [25, 10, 5, 1]:
    q.append(b//int(i))
    b=b%int(i)
  for i in q:
    print(i, end=" ")