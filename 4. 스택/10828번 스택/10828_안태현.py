import sys

input = sys.stdin.readline

n = int(input())

stack = []

for i in range(n):
  temp = input().split()
  if temp[0] == 'push':
    stack.append(temp[1])

  elif temp[0] == 'pop':
    if len(stack) == 0:
      print(-1)
    else:
      #print(stack.popleft())
      print(stack.pop())

  elif temp[0] == 'size':
    print(len(stack))

  elif temp[0] == 'empty':
    if len(stack) == 0:
      print(1)
    else:
      print(0)

  elif temp[0] == 'top':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[len(stack) - 1])
