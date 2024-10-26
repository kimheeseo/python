a=int(input())
cnt=0

b=list(map(int,input().split()))

for i in range(len(b)):
 # print('b[i]값:',b[i])
  if b[i]==1:
    cnt=cnt+1
 #   print('1입니다.')
  for j in range(2, b[i]):  
#    print('j값:',j)

    if b[i]%j ==0:
     # print('소수인가?')
   # else:
     # print('소수 아닙니다.')
      cnt=cnt+1
      break

print(a-cnt)  