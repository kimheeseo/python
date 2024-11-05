aa=int(input())

for i in range(0,aa):
  a,b,c=map(int, input().split())
  if (b-c)>a:
    print('advertise')
  if (b-c)==a:
    print('does not matter')
  if (b-c)<a:
    print('do not advertise')