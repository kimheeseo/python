a=int(input())
s=[0,1,1]
idx=3

while True:
    p=s[idx-1]+s[idx-2]
    if len(str(p))>1000 or idx >a: # 1000자 이내의 피보나치 수를 구하는 문제
        break
    else:
        s.append(p)
        idx+=1
print(s[a])