n = int(input())

info = []
for _ in range(n):
  n, d, m, y = input().rstrip().split()
  info.append((int(y), int(m), int(d), n))
info.sort()
print(info[-1][3]) # 나이 가장 적은 사람
print(info[0][3]) # 나이 가장 많은 사람
