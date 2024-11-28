a,b,c,d,N=map(int,input().split())

sum=a+b+c+d
total=N*4
if (total-sum) >0:
    print(total-sum)
else:
    print(0)