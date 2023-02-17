# 2178번 미로탐색
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip()))) # readline의 경우 맨 뒤에 '\n'까지 입력받으므로 제거해줘야 함
    # graph.append(input())
    # graph[i] = graph[i][:-1]
    # graph[i] = list(graph[i])

dx = [0, 1, -1, 0] # 우 하 상 좌
dy = [1, 0, 0, -1] 

queue = deque()
queue.append((0, 0))

while queue:
    x, y = queue.popleft()
    for i in range(4): # 상하좌우 다 돌기
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m: # 범위 안에 있으면
            if graph[nx][ny] == 1: # 갈 수 있는 길이면
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1 # 거리 계속 업데이트


print(graph[n-1][m-1]) 
