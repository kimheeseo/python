a, b= map(int,input().split())

if b<=44:
    if a == 0:
        a=24
    d=60-(45-b)
    c=a-1
    print(c,d)
else:
    c=a
    d=b-45
    print(c,d)