# 배열에 넣어두고 푸는 방법
money = int(input())
rest = 1000 - money  # 거스름돈
coin = [500, 100, 50, 10, 5, 1] # 동전 종류 - 큰 동전 순서대로 확인

cnt = 0
i = 0
while rest != 0:
  if rest // coin[i] != 0:  
    tmp = rest // coin[i]
    rest -= tmp * coin[i]
    cnt += tmp
  else:
    i += 1 # 더 작은 동전이 필요할 때, +1

print(cnt)


# 그냥 if문으로 풀면 코드 길이는 길어지고 시간은 40ms로 똑같음
money = int(input())
rest = 1000 - money

cnt = 0
while rest != 0:
  if rest // 500 != 0:
    tmp = rest // 500
    rest -= tmp * 500
    cnt += tmp
  elif rest // 100 != 0:
    tmp = rest // 100
    rest -= tmp * 100
    cnt += tmp
  elif rest // 50 != 0:
    tmp = rest // 50
    rest -= tmp * 50
    cnt += tmp
  elif rest // 10 != 0:
    tmp = rest // 10
    rest -= tmp * 10
    cnt += tmp
  elif rest // 5 != 0:
    tmp = rest // 5
    rest -= tmp * 5
    cnt += tmp
  elif rest // 1 != 0:
    tmp = rest // 1
    rest -= tmp * 1
    cnt += tmp

print(cnt)
