a,b=map(int, input().split())
cc=[]
tmp=[]

for i in range(a):
  cc.append(i+1)

for i in range(b):
  q,w=map(int, input().split())

  tmp=(cc[q-1])
  cc[q-1]=cc[w-1]
  cc[w-1]=tmp

for i in range(a):
  print(cc[i],end=' ')