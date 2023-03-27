import sys
input = sys.stdin.readline

# O(n) 정렬 - 계수 정렬 이용
n = int(input())

# for문 안에서 append를 사용하면 메모리 재할당이 이루어져서 메모리를 효율적으로 사용하지 못한다.
# 정렬할 배열을 입력받아서 append하지 않고, 주어진 입력값의 범위만큼 배열을 미리 생성한다.
# 메모리 낭비를 줄이기 위해서이며, 계수 정렬의 장점을 살린 풀이 (애초에 파이썬으로 풀다보니 생긴 문제같기도,,)
arr = [0] * 10001

for i in range(n):
  item = int(input())
  arr[item] += 1

for i in range(1, 10001):
  if arr[i] >= 1:
    for j in range(arr[i]):
      print(i)
