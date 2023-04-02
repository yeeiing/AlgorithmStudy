import sys
from collections import deque
input = sys.stdin.readline

MAX = 10 ** 5 # 시간 초과 안나게 수 제한
time = [0] * (MAX + 1)
n, k = map(int, input().split())


queue = deque([])
queue.append(n)
while queue: # 큐가 빌 때까지
    x = queue.popleft()
    if x == k: # x가 목적지랑 같으면 break
        break

    for nx in (x-1, x+1, 2*x): #  x-1, x+1, 2*x 차례대로 반복
        if 0 <= nx <= MAX and time[nx] == 0: # 만약 nx가 범위 안에 있고 방문하지 않았다면(방문하지 않으면 리스트 값 0)
            time[nx] = time[x] + 1 
            queue.append(nx)


print(time[k])
