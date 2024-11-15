import math
import sys
input=sys.stdin.readline

k = int(input())

for i in range(1, k + 1):
    balloon_num, weight = map(float, input().split())
    total_helium = 0

    for _ in range(int(balloon_num)):
        radius = float(input())
        total_helium += 4.0 / 3.0 * math.pi * (radius ** 3) / 1000

    print(f"Data Set {i}:")
    if total_helium >= weight:
        print("Yes")
    else:
        print("No")
    print()