import sys
from collections import deque
input = sys.stdin.readline

# BFS 함수
def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    area = 1 # 넓이 세기

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 안에 있으면
            if 0 <= nx < M and 0 <= ny < N:
            	# 그래프 값이 0이 아니면 continue(값이 1이면 직사각형임)
                if graph[nx][ny] != 0:
                    continue
                    
                # 그래프 값이 0이면
                else:
                    area += 1 # 넓이 1 증가
                    graph[nx][ny] = 1 # graph 값 바꿔주고
                    queue.append([nx, ny]) # BFS 돌기 위해 큐에 넣어주기

    if area != 1:
        area -= 1
    return area


M, N, K = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(M):
    graph.append([0]*N)

# 전체적인 그래프 만들기
# 직사각형이 있는 곳에는 1, 없는 곳에는 0
# 따라서 0이 있는 곳만 BFS 돌면 된다
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
   
   # ********이부분이 생각하기 어려웠음
    for j in range(x1, x2):
        for k in range(y1, y2):
            graph[k][j] = 1

answer = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            answer.append(bfs(i, j))

print(len(answer))
answer.sort()
for i in range(len(answer)):
    print(answer[i], end=' ')
