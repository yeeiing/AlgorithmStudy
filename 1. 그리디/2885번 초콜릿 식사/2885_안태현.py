import sys

input = sys.stdin.readline

k = int(input())

d = 2
while d < k:
  d *= 2

D = d
cnt = 0
while k > 0:
  if k >= d:
    k -= d
  else:
    d = d // 2
    cnt += 1
print(D, cnt)
