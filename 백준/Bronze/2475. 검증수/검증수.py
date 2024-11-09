a=list(map(int,input().split()))
su=0

for i in range(5):
    su=su+a[i]**2
print(su%10)