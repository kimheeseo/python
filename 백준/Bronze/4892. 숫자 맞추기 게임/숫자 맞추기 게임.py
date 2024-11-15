import sys
input=sys.stdin.readline

cnt=0
while 1:
    a=int(input()) #n0

    if a == 0:
        break
    cnt=cnt+1

    n1=a*3
    if n1%2==0: #짝수
        n2=n1//2
        parity="even"
    else:
        n2=(n1+1)//2
        parity="odd"
        
    n3=3*n2
    n4=n3//9      
    print(f"{cnt}. {parity} {n4}")