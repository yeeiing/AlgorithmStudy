import sys
from collections import deque
ipnut = sys.stdin.readline

def bfs(x, y):
    each_cnt = 1 # 초기화
    queue = deque()
    queue.append((x, y)) # 큐에 삽입
    visited[x][y] = True # 방문처리

    while queue:
        x, y = queue.popleft() # 큐에서 빼기
        for i in range(4): # 상하좌우 돌기
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m: # 범위 안에 있으면
                if graph[nx][ny] == 1 and not visited[nx][ny]: # 그림이고 방문하지 않았으면
                    visited[nx][ny] = True # 방문처리
                    queue.append((nx, ny)) # 큐에 넣기
                    each_cnt += 1 # 넓이 + 1
    return each_cnt # 그림 넓이 리턴



n, m = map(int, input().split())
visited = [[False]*m for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0] # 하 상 
dy = [0, 0, 1, -1] # 우 좌

# cnt: 그림 개수, max_each_count: 그림 최대 넓이
cnt, max_each_count = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]: # 1이고 방문하지 않았다면
            cnt += 1 # 그림 개수
            max_each_count = max(max_each_count, bfs(i, j)) # 그림 넓이

print(cnt)
print(max_each_count)
