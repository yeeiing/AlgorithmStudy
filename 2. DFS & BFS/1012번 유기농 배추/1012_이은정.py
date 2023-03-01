import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, a, b):
    queue = deque([])
    queue.append((a, b))
    graph[a][b] = 0 # 방문했으면 0으로 바꾸기

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[nx][ny] == 1: # 배추가 심어져있으면
                    queue.append((nx, ny)) # append
                    graph[nx][ny] = 0 # 0으로 바꿔주기
    return


for _ in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    graph = []

    # 그래프 0으로 초기화
    for i in range(M):
        graph.append([0]*N)

    # 배추 심기 (1로)
    for i in range(K):
        a, b = map(int, input().split()) # a: row, b: column
        graph[a][b] = 1 # 입력한 애들은 1로 심어주기

    for x in range(M):
        for y in range(N):
            if graph[x][y] == 1: # 1이면
                bfs(graph, x, y) # bfs 돌기
                cnt += 1 # 다 돌면 cnt + 1
    print(cnt)
