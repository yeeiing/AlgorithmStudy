import sys

input = sys.stdin.readline

test = int(input())

for i in range(test):
  day = int(input())
  stock = list(map(int, input().split()))

  sum = 0
  temp = 0

  for idx, value in enumerate(reversed(stock)):
    if value > temp:
      temp = value
    else:
      sum += temp - value
  print(sum)
