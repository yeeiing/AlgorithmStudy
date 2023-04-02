import sys
from collections import deque
input = sys.stdin.readline

# 적록색약 : RG 구분 못함
N = int(input())
graph = [[] for i in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문처리 할 리스트 (방문 안했으면 0, 방문 했으면 1)
normal_visited = [[0]* N for _ in range(N)]
weak_visited = [[0]* N for _ in range(N)]

# 적록색약이 아닌 사람의 BFS 함수
def normalBFS(x, y):
    queue = deque()
    queue.append((x, y))
    normal_visited[x][y] = 1 # 방문 처리
    color = graph[x][y] # BFS를 돌기 위해 저장한 색깔(이 색깔만 돌아야함)
        
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N: # 범위 안에 있으면
                # 돌고 있는 색이고 방문하지 않았으면
                if graph[nx][ny] == color and normal_visited[nx][ny] == 0: 
                    normal_visited[nx][ny] = 1 # 방문 처리
                    queue.append((nx, ny)) # 큐에 넣기
                    
# 적록색약인 사람의 BFS 함수
def weakBFS(x, y):
    queue = deque()
    queue.append((x, y))
    weak_visited[x][y] = 1 # 방문 처리
    color = graph[x][y] # BFS를 돌기 위해 저장한 색깔(이 색깔만 돌아야함)
    
    # +) 적록색약은 R G를 구분 못함
    status = 0 # 적색이나 녹색이면 0, 파란색이면 1
    if color == 'B':
        status = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N: # 범위 안에 있으면
                # 돌고 있는 색이 R 또는 G이고(status=0), 방문하지 않았으면
                if status == 0 and weak_visited[nx][ny] == 0: 
                	# 현재 그래프가 R 또는 G이면
                    if graph[nx][ny] == 'R' or graph[nx][ny] == 'G': 
                        weak_visited[nx][ny] = 1 # 방문처리
                        queue.append((nx, ny)) # 큐에 넣기
                        
				# 돌고 있는 색이 B이고(status=1), 방문하지 않았으면
                elif status == 1 and weak_visited[nx][ny] == 0:
                	# 현재 그래프가 B이면
                    if graph[nx][ny] == 'B':
                        weak_visited[nx][ny] = 1 # 방문 처리
                        queue.append((nx, ny)) # 큐에 넣기
# ----------------------------------------------------------------------------------
                    
# 그래프 입력
for i in range(N):
    temp = list(input())
    for j in range(N):
        graph[i].append(temp[j])

normal_cnt = 0 
weak_cnt = 0
for i in range(N):
    for j in range(N):
    	# 방문하지 않았으면 함수 돌기
        if normal_visited[i][j] == 0:
            normalBFS(i, j)
            normal_cnt += 1

        if weak_visited[i][j] == 0:
            weakBFS(i, j)
            weak_cnt += 1

print(normal_cnt)
print(weak_cnt)
