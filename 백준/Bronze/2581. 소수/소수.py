a=int(input())
b=int(input())
c=[]

for i in range(a, b+1):
    if i<2:
        continue
    if i ==2:
        c.append(i)
        continue
    for j in range(2, i):
        if i % j ==0:
            break
        if j == i-1:
            c.append(j+1)  

if not c:
    print(-1)
else:
    print(sum(c))
    print(min(c))