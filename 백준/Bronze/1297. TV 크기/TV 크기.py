d, h, w = map(int, input().split())
di = (h**2 + w**2)**(1/2) # 높이와 너비를 통해 구한 대각선의 길이
ratio = d / di

height = int(h * ratio)
width = int(w * ratio)

print("%d %d" %(height, width))