# 1260 DFS와 BFS
import sys
from collections import deque
input = sys.stdin.readline

# DFS
def DFS(graph, V, visited):
    visited[V] = True # 방문 처리
    print(V, end=' ')

    # 연결된 노드 재귀로 방문
    for i in graph[V]:
        if not visited[i]:
            DFS(graph, i, visited)

# BFS
def BFS(graph, V, visited):
    queue = deque([V]) # deque 라이브러리 사용
    visited[V] = True # 방문 처리

    while queue: # queue가 빌 때까지
        v = queue.popleft() # 하나 빼고
        print(v, end=' ')
        for i in graph[v]: # 뺀 애들이랑 연결된 애들 방문처리
            if not visited[i]:
                queue.append(i)
                visited[i] = True


    
N, M, V = map(int, input().split()) # node, edge, start

graph = [[] for _ in range(N+1)] # 리스트는 0부터 시작이니까 빈 리스트 하나 더 만들어줌

for _ in range(M): # edge 수만큼 반복
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 연결된 애들끼리 정렬
for i in range(1, N+1):
    graph[i].sort()

visited = [False]*(N+1)
DFS(graph, V, visited)
print()
visited = [False]*(N+1)
BFS(graph, V, visited)
