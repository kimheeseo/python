a=int(input())
cnt=0

for i in range(1,a+1): #브루트포스 알고리즘
    num=list(map(int, str(i)))
    cnt=sum(num)+i
    if a==cnt:
        print(i)
        break
else:
    print(0)