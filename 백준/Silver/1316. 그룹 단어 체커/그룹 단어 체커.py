ii=int(input())
jung=0

for a in range(ii):
    a=input()
    cnt=0
    c=[0 for i in range(len(a))]

    for i in range(len(a)):
        cnt=0
        for j in range(i+1,len(a)):    
            if a[j]==a[i]:
                c[i]+=1

    cnt=0
    for i in range(len(a)):
        if c[i] !=0:
            for j in range(0,c[i]):
                if a[i] != a[i+j+1]:
                    cnt+=1
                    #print(cnt)
                    break
        if cnt ==1:
            #print('중복 단어가 아닙니다.')
            break
    if cnt==0:
        #print('중복단어입니다.')
        jung=jung+1
print(jung)