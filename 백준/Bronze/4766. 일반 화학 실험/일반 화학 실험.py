a=float(input())
prev=a
while 1:
    a=float(input())
    if a == 999:
        break
    
    print('%0.2f' %(a-prev))
    prev=a