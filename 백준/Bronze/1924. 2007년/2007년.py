Day = 0
arrList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekList = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]
 
x, y = map(int,input().split())
 
for i in range(x-1):
    Day = Day + arrList[i] # 총 몇달 걸렸는지 계산하기 위해서, day값을 누적.
#그 값과 몇일인지를 계산한 후, 7일로 나눠서 나머지를 몇 요일인지 유추.
Day = (Day + y) % 7
 
print(weekList[Day])