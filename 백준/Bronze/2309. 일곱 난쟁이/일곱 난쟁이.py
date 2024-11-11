import sys
input=sys.stdin.readline

arr = []
for _ in range(9):
    f=int(input())
    arr.append(f)
arr.sort()

sum_ = sum(arr)
fake=[]
# 7번 반복 대신 반대로 생각 9명 합에서 2명을 뺐을때 100 이하인 경우 찾기
for i in range(9):
    for j in range(i+1,9):
        if(len(fake)==2):
            continue
        if sum_-arr[i]-arr[j] ==100:
            fake.append(arr[i])
            fake.append(arr[j])

for i in arr:
    if i in fake:
        continue
    print(i)