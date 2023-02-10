import sys

input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
  temp = int(input())
  arr.append(temp)

# 삽입 정렬
for i in range(1, n):
  for j in range(i, 0, -1): # 현재 위치 - 1 부터 거꾸로 탐색
    if arr[j - 1] > arr[j]: # 앞에 있는 값이 현재 값보다 크다면 swap
      temp = arr[j]
      arr[j] = arr[j - 1]
      arr[j - 1] = temp

for item in arr:
  print(item)
