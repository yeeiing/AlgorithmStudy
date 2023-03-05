from collections import deque # deque로 풀면 76ms list로 풀면 72ms
import sys

input = sys.stdin.readline # 빼면 시간 초과나옴 ㅜ

n = int(input())

#queue = deque([])
queue = []

for i in range(n):
  temp = input().split()
  if temp[0] == 'push':
    queue.append(temp[1])

  elif temp[0] == 'pop':
    if len(queue) == 0:
      print(-1)
    else:
      #print(queue.popleft())
      print(queue.pop(0))

  elif temp[0] == 'size':
    print(len(queue))

  elif temp[0] == 'empty':
    if len(queue) == 0:
      print(1)
    else:
      print(0)

  elif temp[0] == 'front':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[0])

  elif temp[0] == 'back':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[len(queue) - 1])
