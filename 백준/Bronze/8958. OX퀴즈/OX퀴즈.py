qw=int(input())

for ii in range(qw):
  a=input().strip()
  cnt=[]
  cnt1=0

  for i in range(0,len(a)):
      if a[i] == 'O':
        cnt1=cnt1+1
        cnt.append(cnt1)
      else:
        cnt1=0
        cnt.append(0)
      if i == len(a)-1:
        print(sum(cnt))