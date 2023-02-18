n = int(input())

arr = list(map(int, input().split()))

# 삽입 정렬
for i in range(1, n): # 탐색 범위의 시작은 1
  for j in range(i, 0, -1): # i부터 0까지 탐색
    if arr[j - 1] > arr[j]:
      temp = arr[j]
      arr[j] = arr[j - 1]
      arr[j - 1] = temp

for i in range(n - 1): # 누적합
  arr[i + 1] += arr[i]

print(sum(arr))
