a = input().upper() # 대소문자 구분 없이 모두 대문자로 변환
b = list(set(a)) # 중복된 알파벳을 제거한 리스트 생성
c = []

# 각 알파벳의 등장 횟수 계산
for i in b:
    c.append(a.count(i)) # 알파벳의 등장 횟수를 리스트에 추가

# 가장 많이 등장한 횟수 찾기
m = max(c)

# 가장 많이 등장한 알파벳의 개수 확인
if c.count(m) > 1: 
    print('?') # 가장 많이 등장한 알파벳이 여러 개라면 '?' 출력
else:
    print(b[c.index(m)]) # 그렇지 않으면 가장 많이 등장한 알파벳 출력