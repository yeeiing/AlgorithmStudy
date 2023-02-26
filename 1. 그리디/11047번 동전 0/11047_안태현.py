import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # n, k
coin = [] # coin 종류 저장할 list

for i in range(n):
  coin.append(int(input())) # coin 저장


idx = 0
cnt = 0

while k > 0: # k원을 만들 때까지
  num = k // coin[n - idx - 1] # 큰 단위부터 나누어지는지 확인
  if num >= 1:  # 나누어진다면 그 개수만큼 동전을 사용하기
    k -= coin[n - idx - 1] * num
    cnt += num
  else:  # 나누어지지 않으면 더 작은 단위로
    idx += 1

print(cnt)
