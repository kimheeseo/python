a=int(input())

for i in range(a):
    b=list(input())
    c=len(b)

    if len(b) == 1:
        print(b[0]+b[0])
    else:
        print(b[0]+b[c-1])