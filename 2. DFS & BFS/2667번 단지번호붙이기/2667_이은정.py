import sys
from collections import deque

# 빠른 입력을 위한 모듈 설정
input = sys.stdin.readline

# 상하좌우 방향을 나타내는 변수
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수 정의
def bfs(a, b):
  # 큐 생성 및 시작 위치 추가, 섬의 크기를 나타내는 변수 count 초기화
  queue = deque()
  queue.append([a,b])
  count = 1

  # 큐가 빌 때까지 반복
  while queue:
    x, y = queue.popleft()
    # 상하좌우 방향으로 이동하면서 단지 크기 계산
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 지도 범위를 벗어나지 않으면서, 아직 방문하지 않은 위치이면
      if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
        # 방문한 위치를 0으로 바꾸고, 큐에 추가
        graph[nx][ny] = 0
        queue.append([nx, ny])
        # 섬의 크기 증가
        count += 1

  # 단지의 크기가 1보다 크면, 시작 위치를 제외한 단지의 크기이므로 1을 빼줌
  if count != 1:
    count -= 1
  return count

# 지도의 크기 N 입력
N = int(input())
# 지도 입력 받기
graph = []
for i in range(N):
  graph.append(list(map(int, input().rstrip())))

# 각 단지의 크기를 저장할 리스트
answer = []
# 지도를 전체 탐색하면서, 단지의 시작 위치를 찾아 BFS 실행
for i in range(N):
  for j in range(N):
    if graph[i][j] == 1:
      # 단지의 크기를 구하고, answer 리스트에 추가
      answer.append(bfs(i,j))

# 단지의 개수와 크기 출력
print(len(answer))
answer.sort()
for i in range(len(answer)):
  print(answer[i])
