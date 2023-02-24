import sys
from collections import deque
input = sys.stdin.readline

# #: 벽
# .: 지나갈 수 있는 공간
# J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
# F: 불이 난 공간

R, C = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue_J, queue_F = deque(), deque() # BFS 하기 위한 Queue
visit_J, visit_F = [], [] # 방문처리 할 리스트

for i in range(R):
    visit_J.append([0]*C) # 방문처리 0은 not visited, 1은 visited
    visit_F.append([0]*C)
    graph.append(list(input().rstrip())) # rstrip() 쓰면 맨 뒤에 있는 개행문자 제거됨

temp = [] # 처음 주어질 때 F 였던 애들 1로 만들기 위해서(반복문 돌다보면 중복돼서 숫자 계속 늘어나는 오류 해결 위해서)
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'J':
            queue_J.append((i, j))
        if graph[i][j] == 'F':
            queue_F.append((i, j))
            temp.append([i, j]) # 처음 주어질 때 F인 애들 append

# 불이 번지는 시간을 visitF에 저장
while queue_F:
    x, y = queue_F.popleft()
    for i in range(4): # 상하좌우 돌기
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C: # 범위 안에 있으면
            if visit_F[nx][ny] == 0 and graph[nx][ny] != '#': # 방문하지 않았고 벽이 아니면
                visit_F[nx][ny] = visit_F[x][y] + 1 # time + 1
                queue_F.append((nx, ny))

# 반복문 돌다보면 중복돼서 숫자 계속 늘어나는 오류 해결 위해
for i in range(len(temp)): 
    a = temp[i][0]
    b = temp[i][1]
    visit_F[a][b] = 1

# 불에 번지는 시간에 따른
# 지훈이의 대피 시간 계산
while queue_J:
    x, y = queue_J.popleft()
    for i in range(4): # 상하좌우
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < R and 0 <= ny < C): # 범위 밖이므로 탈출 성공
            print(visit_J[x][y] + 1)
            sys.exit(0) # 바로 프로그램 종료

        if visit_J[nx][ny] == 0 and graph[nx][ny] != "#": # 방문하지 않았고 벽이 아닐 때
            if visit_F[nx][ny] == 0 or visit_J[x][y]+1 < visit_F[nx][ny]: # 불이 난 적 없거나 불이 오기 전에 갈 수 있는 곳이라면
                visit_J[nx][ny] = visit_J[x][y]+1
                queue_J.append((nx, ny))


print("IMPOSSIBLE")
