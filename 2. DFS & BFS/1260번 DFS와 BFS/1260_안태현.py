import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

# 인접행렬 생성
graph = [[0] * (n + 1) for i in range(n + 1)]

# visit
dfs_visit = [0] * (n + 1)
bfs_visit = [0] * (n + 1)

# 연결된 두 정점의 index는 1로
for i in range(m):
  s, e = map(int, input().split())
  graph[s][e] = graph[e][s] = 1


# dfs - 재귀
def dfs(v):
  print(v, end=' ')

  dfs_visit[v] = 1  # 방문한 노드 체크
  for i in range(1, n + 1):
    if dfs_visit[i] == 0 and graph[v][i] == 1:  # 방문한 적 없는 인접노드인가?
      dfs(i)


# bfs - 큐
def bfs(v):
  queue = deque([v])
  bfs_visit[v] = 1  # 시작 노드 방문

  while queue:
    v = queue.popleft()  # 노드 제거
    print(v, end=' ')  # 시작 노드 출력

    for i in range(1, n + 1):
      if bfs_visit[i] == 0 and graph[v][i] == 1:  # 방문한 적 없는 인접노드인가?
        queue.append(i)
        bfs_visit[i] = 1


dfs(v)
print()
bfs(v)
