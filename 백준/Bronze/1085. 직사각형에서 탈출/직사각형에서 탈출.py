a,b,c,d=map(int,input().split())

garo=c
sero=d

garo1=garo-a
sero1=sero-b

if garo1<garo/2:
  garo2=garo1
else:
  garo2=garo-garo1

if sero1<sero/2:
  sero2=sero1
else:
  sero2=sero-sero1

if sero2<garo2:
  print(sero2)
else:
  print(garo2)