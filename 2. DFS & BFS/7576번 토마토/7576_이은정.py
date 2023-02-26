import sys
from collections import deque
input = sys.stdin.readline

def bfs():
 while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 그래프의 범위 내에 있고, 빈 칸이 아닌 경우
    if 0 <= nx < m and 0 <= ny < n:
      if graph[nx][ny] == -1:
        continue
      # 아직 방문하지 않은 경우
      elif graph[nx][ny] == 0:
        queue.append((nx, ny))
        graph[nx][ny] = graph[x][y]+1
  
 
n, m = map(int, input().split()) # 그래프 크기 입력 받기
graph = [[] for i in range(m)] # 그래프 초기화
res = 0 # 일수 초기화

# 이동방향 : 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(m):
  graph[i] = list(map(int, input().split()))
  # 익은 토마토 : 1
  # 익지 않은 토마토 : 0
  # 빈 칸 : -1

queue = deque([])
for i in range(m):
  for j in range(n):
    if graph[i][j] == 1: 
      queue.append([i,j]) # 익은 토마토의 위치 큐에 추가
      
bfs() # BFS 탐색

for i in graph:
  for j in i:
    if j == 0: # 모든 토마토가 익지 않은 경우 -1 출력 후 종료
      print(-1)
      exit(0)
  res = max(res, max(i)) # 익은 토마토가 가장 오래 걸린 일수

print(res-1) # 최소 일수 출력
