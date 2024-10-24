a,b=map(int, input().split())
A=[]
B=[]

for i in range(a):
    qq=list(map(int, input().split()))
    A.append(qq)

for i in range(a):
    qq=list(map(int, input().split()))
    B.append(qq)

for i in range(a):
  for j in range(b):
    print(A[i][j]+B[i][j],end=" ")
print()