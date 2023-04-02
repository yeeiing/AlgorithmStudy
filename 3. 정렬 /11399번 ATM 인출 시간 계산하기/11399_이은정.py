import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))
time.sort()

sum, total = 0, 0
for i in range(n):
  sum += time[i]
  total += sum

print(total)
           
