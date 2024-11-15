temp1=0
cnt=0

while 1:
    a=int(input())
    if a== -1:
        break
    
    temp1=0 #prev_time
    cnt=0 # total_distance
    for i in range(a):    
        b,c=map(int, input().split())
        c1=c-temp1
        cnt=cnt+b*c1
        temp1=c
    print(f'{cnt} miles')