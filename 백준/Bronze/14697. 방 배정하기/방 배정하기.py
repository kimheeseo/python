a,b,c,N=map(int,input().split())
while 1:
  N=N-(N//c)*c

  if b<=N<c:
    N=N-(N//b)*b


  if a<=N<b:
    N=N-(N//a)*a

    if N==0:
      print(1)
      break
    elif N<a:
      print(0) 
      break
    
