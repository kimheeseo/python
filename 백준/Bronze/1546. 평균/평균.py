a=int(input()) #과목의 갯수
b=list(map(int, input().split()))
max_value=max(b)

new_list=[]
for c in b:
  new_list.append(c/max_value*100)

sum2=0
for cc in range(a):
  sum2=sum2+new_list[cc]
print(sum2/a)