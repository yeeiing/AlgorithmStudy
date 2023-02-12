import sys
from collections import deque

input = sys.stdin.readline

# BFS 수행해서 탐색, 1번 노드에서 방문 가능한 컴퓨터의 개수 출력하기

n = int(input())
m = int(input())

graph = [[0] * (n + 1) for i in range(n + 1)]  # 인접행렬
visit = [0] * (n + 1)  # 방문한 노드라면 1
cnt = 0  # 감염된 컴퓨터 개수

for i in range(m):
  s, e = map(int, input().split())
  graph[s][e] = graph[e][s] = 1

#print(graph)

queue = deque([1])
visit[1] = 1  # 1번 노드에서 출발

while queue:
  v = queue.popleft() 

  for i in range(1, n + 1):
    if visit[i] == 0 and graph[v][i] == 1:  # 방문한 적 없는 인접노드인가?
      queue.append(i)
      visit[i] = 1
      cnt += 1  # 바이러스 감염

print(cnt)
