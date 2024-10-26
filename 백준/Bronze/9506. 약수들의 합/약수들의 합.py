while 1:
  a=int(input())
  b=[]

  if a==-1:
    break
  else:  
    for i in range(1,a):
      if a%i==0:
        b.append(i)
  #  print(b)
    if sum(b) == a:
      print('%d =' %a,end= ' ')
      for i in range(len(b)):
        if i == len(b)-1:
          print('%d' %b[i])  
        else:
          print('%d +' %b[i],end=' ')
          continue
    else:
      print('%d' %a, 'is NOT perfect.')
      continue