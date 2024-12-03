import math
import sys
input=sys.stdin.readline

def max(a, b):
    return a if a > b else b

def min(a, b):
    return a if a < b else b

def calculate(a, b, c, d, price):
    highest_h = max(math.ceil(rh / a), math.ceil(sh / c))
    highest_v = max(math.ceil(rv / b), math.ceil(sv / d))
    return highest_h * highest_v * price

rh, rv, sh, sv = map(int, input().split())
monitor_num = int(input())

result = float('inf')

for _ in range(monitor_num):
    rhi, rvi, shi, svi, pi = map(int, input().split())
    result = min(result, min(calculate(rhi, rvi, shi, svi, pi), calculate(rvi, rhi, svi, shi, pi)))

print(result)