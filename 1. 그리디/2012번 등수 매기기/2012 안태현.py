import sys

input = sys.stdin.readline

n = int(input())

arr = []  # 등수를 저장할 배열
for i in range(n):
  temp = int(input())
  arr.append(temp)

arr.sort()  # 오름차순 정렬

ans = 0
for i in range(n):
  if arr[i] != (i + 1):
    ans += abs(arr[i] - (i + 1)) # 불만도 계산

print(ans)
