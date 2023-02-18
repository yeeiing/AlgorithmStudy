n, m, k = map(int, input().split())

all = n + m
cnt = 0
while all > k :
  if n >= 2 and m >= 1 : # 짝지을 수 있는지 확인
    n -= 2
    m -= 1
    all = n + m
    if all - k >= 0 :  # 인턴십에 나갈 인원이 남았다면 팀 +1
      cnt += 1
  else:
    break

print(cnt)
