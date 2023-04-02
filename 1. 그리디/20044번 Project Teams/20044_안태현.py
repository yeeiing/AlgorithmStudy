import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))


k = 2 * n # 학생 수

# 합의 최솟값이 최대가 되도록 오름차순 정렬 후 가장 작은 값 + 가장 큰 값
arr.sort() # 오름차순 정렬
min = arr[0] + arr[-1] # 첫번째 + 마지막
for i in range(1, n):
    if min > arr[i] + arr[k-(i+1)]:
        min = arr[i] + arr[k-(i+1)]

print(min)
