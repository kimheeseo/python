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
            #list del method은 코테 풀이할때 가급적 쓰지 말자!

for i in arr:
    if i in fake:
        continue
    print(i)
 #출처: https://velog.io/@rhdmstj17/%EB%B0%B1%EC%A4%80-2309%EB%B2%88-%EC%9D%BC%EA%B3%B1-%EB%82%9C%EC%9F%81%EC%9D%B4-python-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4%EB%B2%95-3%EA%B0%80%EC%A7%80