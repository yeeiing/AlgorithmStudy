import sys
from collections import deque
input = sys.stdin.readline

# BFS 알고리즘을 이용하여 연결된 정점들을 탐색하는 함수
def bfs(graph, start):
  queue = deque([])     # 큐 생성
  queue.append(start)   # 시작 정점 큐에 삽입
  visited[start] = True # 시작 정점 방문 처리
  cnt = 0               # 방문한 정점 개수 초기화

  while queue:          # 큐가 빌 때까지 반복
    v = queue.popleft() # 큐의 가장 왼쪽 정점을 꺼내옴
    for i in graph[v]:  # 꺼내온 정점과 연결된 정점들 중에서
      if not visited[i]: # 방문하지 않은 정점이 있다면
        queue.append(i)   # 큐에 삽입
        visited[i] = True # 방문 처리
        cnt += 1          # 방문한 정점 개수 증가

  return cnt             # 방문한 정점 개수 반환


node = int(input())     # 노드 개수 입력
edge = int(input())     # 간선 개수 입력

graph = [[] for i in range(node+1)]  # 노드 개수만큼 빈 그래프 생성
visited = [False]*(node+1)           # 방문 여부를 저장하는 리스트 초기화
for i in range(edge):                # 간선 개수만큼 반복
  a, b = map(int, input().split())   # 두 정점 입력
  graph[a].append(b)                 # 그래프에 연결된 정점 정보 저장
  graph[b].append(a)                 # 양방향 그래프이므로 반대 방향도 저장

print(bfs(graph, 1))                 # 1번 노드를 시작으로 bfs 알고리즘 수행 후 결과 출력
