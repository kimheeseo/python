a=int(input())
b=[]
cnt=0
cntt=0

for i in range(a):
    c=int(input())
    b.append(c)

for i in b:
  if i>cntt:
    cntt=i
    cnt=cnt+1
print(cnt)  
cnt=0
cntt=0
for i in b[::-1]:
  if i>cntt:
    cntt=i
    cnt=cnt+1
print(cnt) 