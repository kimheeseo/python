a=[]
b,c=map(int,input().split())

for i in range(1,c+1):
  for j in range(i):
    a.append(i)
    
print(sum(a[b-1:c]))