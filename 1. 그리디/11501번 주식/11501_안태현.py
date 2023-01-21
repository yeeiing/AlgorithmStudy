import sys

input = sys.stdin.readline

test = int(input())

for i in range(test):
  day = int(input())
  stock = list(map(int, input().split()))

  sum = 0
  temp = 0

  # 순서를 뒤집어서 마지막날부터 순차적으로 봄
  for value in reversed(stock): 
    if value > temp:  # 앞날 값이 더 크다면 현재 주식을 업데이트
      temp = value
    else:
      sum += temp - value # 앞날 값이 더 작다면 현재와 앞날의 차가 이익
  print(sum)
