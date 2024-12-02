a=int(input())
c=[]


for i in range(a):
  c=[]
  b=str(int(input())) # 숫자 대입

  cnt=0
  for i in range(0,len(b)):
    c.append(b[-i-1])
  cc=''.join(c) # 거꾸로
  sum_=str(int(cc)+int(b))


  for i in range(0,len((sum_))//2):
    #print('b[i]값:',sum_[i])
    #print('b[반대값]',sum_[len(sum_)-1-i])
    if sum_[i]!= sum_[len(sum_)-1-i]:
      print('NO')
      break
    else:
      cnt+=1
  if cnt==len(sum_)//2:
    print('YES')