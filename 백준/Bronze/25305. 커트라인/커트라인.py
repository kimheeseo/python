a, b=map(int, input().split())
#a: 총인원수, b: 상을 받을 사람
c=list(map(int, input().split()))
c.sort(reverse=True)
print(c[b-1])