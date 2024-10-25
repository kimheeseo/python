qq=[]
qq2=[]

while 1:
    qq=[]
    qq2=[]
    a,b,c=map(int,input().split())

    qq.append(a)
    qq.append(b)
    qq.append(c)
    
    qq2=sorted(qq, reverse=True)
    a=qq2[0]
    b=qq2[1]
    c=qq2[2]

    if a==0 and b ==0 and c==0:
        break  

    if b+c<=a:   
        print('Invalid')
  
    elif a == b == c:
        print('Equilateral')

    elif a==b or b==c or c==a:
        print('Isosceles')   

    else:
        print('Scalene')