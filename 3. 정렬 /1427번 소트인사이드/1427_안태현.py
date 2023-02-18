n = input()
n = list(n)

# 삽입 정렬
for i in range(1, len(n)) :
  for j in range(i, 0, -1) :
    if n[j - 1] < n[j] :
      temp = n[j]
      n[j] = n[j - 1]
      n[j - 1] = temp

for i in n:
  print(i, end='')
