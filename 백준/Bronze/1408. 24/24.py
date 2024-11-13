# 시작 시간 입력
a = input()
hour1 = int(a[0:2])
min1 = int(a[3:5])
sec1 = int(a[6:8])

# 종료 시간 입력
b = input()
hour2 = int(b[0:2])
min2 = int(b[3:5])
sec2 = int(b[6:8])

# 시작 시간과 종료 시간을 초 단위로 변환
start_time = hour1 * 3600 + min1 * 60 + sec1
end_time = hour2 * 3600 + min2 * 60 + sec2

# 만약 종료 시간이 시작 시간보다 작다면, 하루가 지난 시간으로 간주
if end_time < start_time:
    end_time += 24 * 3600

# 두 시간의 차이 계산
diff = end_time - start_time

# 시, 분, 초로 변환
hour3 = (diff // 3600) % 24
min3 = (diff % 3600) // 60
sec3 = diff % 60

# 출력 (2자리 형식 유지)
print('%02d:%02d:%02d' % (hour3, min3, sec3))