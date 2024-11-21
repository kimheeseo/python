import sys
input = sys.stdin.readline
flat,up,down=0,0,0
count=int(input())
a=[0] * (count+1)
a[0] = int(input())
flag=0
for i in range(1,count+1):
    if i < count :
        a[i] = int(input())
    else : 
        a[i] = a[0]
    if a[i] == a[i-1] and flag != 1 :
        flat +=1 
        flag = 1
    elif a[i] > a[i-1] and flag != 2 :
        up +=1 
        flag = 2
    elif a[i] < a[i-1] and flag != 3 :
        down +=1 
        flag = 3
print(flat, up, down)