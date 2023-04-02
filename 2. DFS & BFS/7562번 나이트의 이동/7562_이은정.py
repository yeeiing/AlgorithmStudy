import sys
from collections import deque
input = sys.stdin.readline

T = int(input()) # 테스트 수
# 나이트가 갈 수 있는 경우의 수 8가지
dx = [-2,-2, 2, 2, -1, -1, 1, 1]
dy = [-1, 1,-1, 1, -2, 2, -2, 2]

for _ in range(T):
    status = 0 # 원하는 위치에 도달했는지 확인할 변수
    I = int(input()) # 체스판 크기 n x n
    curX, curY = map(int, input().split()) # 현재 나이트 위치
    wantX, wantY = map(int, input().split()) # 원하는 위치

    # 방문처리 할 체스판 0으로 초기화
    graph = [[0]*I for _ in range(I)]

    queue = deque()
    queue.append((curX, curY)) # 처음 위치 큐에 넣기
    
    while queue:
        x, y = queue.popleft()
        if x == wantX and y == wantY: # 처음 위치랑 원하는 위치가 같으면 break
            break
            
        for i in range(8): # 8가지 경우의 수 돌기
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < I and 0 <= ny < I: # 범위 내에 있으면
                if nx == wantX and ny == wantY: # 도달했으면
                    graph[nx][ny] = graph[x][y] + 1 # 횟수 + 1
                    status = 1 # 원하는 위치에 도달했으므로 1로 체크
                    break

                if nx == curX and ny == curY: # 처음 위치와 같으면
                    continue

                if graph[nx][ny] != 0: # 이미 방문했으면
                    continue
                
                queue.append((nx, ny)) # 큐에 넣기
                graph[nx][ny] = graph[x][y] + 1
        
        if status == 1:
            break
    
    print(graph[wantX][wantY])
