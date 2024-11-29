#등차수열/ 등비수열 문제
a=int(input()) # 수열의 길이
b=[]

for _ in range(a):
  j=int(input())
  b.append(j)

b.sort()
if b[1]-b[0] == b[2]- b[1]:
  #print("등차수열")
  print(int(b[-1]+(b[1]-b[0])))
else:
 # print("등비수열")
  print(int(b[-1]*(b[1]/b[0])))