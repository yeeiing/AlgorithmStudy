import sys

input = sys.stdin.readline

k = int(input())

d = 2
while d < k: # 최소 필요한 초콜릿 정사각형 개수 구함
  d *= 2

D = d
cnt = 0
while k > 0:
  if k >= d: # k가 더 크다면 k에서 빼줌
    k -= d
  else:
    d = d // 2 # 반으로 쪼개기
    cnt += 1
print(D, cnt)
