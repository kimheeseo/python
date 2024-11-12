a=int(input()) # N단계

b=a*(a+1)/2-1 # 단계씩 증가할때마다 N단계*3+1개씩 증가
c=b*3+(a-1)

result=int(c+5)
print(result%45678)