a,b,c=map(int, input().split())
dd=[a,b,c]
max1a=max(dd)
inde=dd.index(max1a)

if a==b and a==c and b==c:
    d=10000+a*1000
elif (a==b or a==c):
    d=1000+a*100
elif (b==c or b==a):
    d=1000+b*100
else:
    d=dd[inde]*100
print(d)  