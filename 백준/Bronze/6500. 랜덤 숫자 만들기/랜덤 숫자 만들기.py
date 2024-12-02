def main():
    while True:
        n = int(input())
        if n == 0:  # 입력이 0이면 종료
            break
        
        v = []  # 방문한 숫자를 저장할 리스트
        v.append(n)
        n *= n
# zfill(): 문자열 형태에서 지정한 길이만큼 0을 채워줍니다.        
        while True:
            s = str(n).zfill(8)  # 숫자를 문자열로 변환하고 8자리로 채움
            n = int(s[2:6])  # 중간 4자리 추출
            
            if n in v:  # 이미 방문한 숫자라면 종료
                break
            
            v.append(n)
            n *= n
        
        print(len(v))  # 방문한 숫자의 개수 출력

if __name__ == "__main__":
    main()
