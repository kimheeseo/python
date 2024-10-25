a=int(input())
ha=[]
ha2=[]
for i in range(a):
  b,c=map(int,input().split())
  ha.append(b)
  ha2.append(c)

hamax=max(ha)
hamin=min(ha)

ha2max=max(ha2)
ha2min=min(ha2)

print((hamax-hamin)*(ha2max-ha2min))