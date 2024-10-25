d=[]
for i in range(5):
  j=int(input())
  d.append(j) 
d.sort()  

print(round(sum(d)/5))
print(int(d[2]))