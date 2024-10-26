a,b=map(int, input().split())
cc=[]
tmp=[]

for i in range(a):
    cc.append(i+1)

for i in range(b):
    q,w=map(int, input().split())
    cnt=0
    for j in range(q-1,(w+q)//2):
        tmp=cc[j]
        cc[j]=cc[w-cnt-1]
        cc[w-cnt-1]=tmp
        cnt=cnt+1
        
for i in range(a):
    print(cc[i], end=' ')