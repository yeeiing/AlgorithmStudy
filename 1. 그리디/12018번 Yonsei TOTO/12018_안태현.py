import sys

input = sys.stdin.readline

n, m = map(int, input().split())

sub_m = [] # 필요한 마일리지 배열
ans = 0
for i in range(n):
  p, l = map(int, input().split())
  arr = list(map(int, input().split()))
  if p < l:  # 신청한 인원 < 수강인원
    if m >= 1: # 마일리지가 남아있는 경우
      m -= 1
      ans += 1
  elif p >= l: # 수강인원보다 신청한 인원이 많다면
    arr.sort(reverse=1) # 내림차순으로 정렬
    sub_m.append(arr[l - 1])

sub_m.sort() # 오름차순으로 정렬
for item in sub_m:
  if item <= m:
    m -= item
    ans += 1
  else:
    break

print(ans)
