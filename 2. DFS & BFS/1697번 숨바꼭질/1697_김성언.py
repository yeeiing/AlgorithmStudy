import sys
from collections import deque

def bfs():

    queue = deque([n])

    # 큐에 탐색해야 하는 노드 없을 때까지 실행
    while queue:
        x = queue.popleft()

        if x == k: # 멈춤
            print(g[x])
            break

        for i in (x - 1, x + 1, x * 2): # 방법 3가지
            if 0 <= i <= 100000 and not g[i]:
                g[i] = g[x] + 1
                queue.append(i)


n, k = map(int,sys.stdin.readline().split())
g = [0] * 100000
bfs()