a=int(input())
b=map(int,input().split())
count=0

for i in b:
    count+=i

if count >0:
    print("Right")
elif count ==0:
    print("Stay")
else:
    print("Left")