def count_odd(arr):
  cnt = 0
  for i in arr:
    if i%2==1:
      cnt+=1
  return cnt

while True:
  n = int(input())
  if n == 0:
    break
    
  else:
    Mary = list(map(int,input().split()))
    John = list(map(int,input().split()))

    odd_m = count_odd(Mary)
    even_m = n - odd_m

    odd_j = count_odd(John)
    even_j = n - odd_j

    ans = n - min(odd_m, even_j) - min(odd_j, even_m)
    print(ans)