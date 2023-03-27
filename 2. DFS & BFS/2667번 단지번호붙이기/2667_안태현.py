import sys
input = sys.stdin.readline

n = int(input())
graph = []

for i in range(n):
  # '0110110' 문자열을 ['0','1'...]으로 변환한 후 원소들을 int로 변경해줌
  temp = list(map(int, list(input().split()[0])))
  graph.append(temp)

# 상하좌우 이동할 좌표 설정
dx = [0, 0, 1, -1] # 좌우
dy = [1, -1, 0, 0] # 상하

count = 0
result = []
def DFS(x, y):
  global count
  
  # base case: 지도의 범위를 벗어나면 return
  if x < 0 or x >= n or y < 0 or y >= n:
    return

  if graph[x][y] == 1:
    # 원소가 1이라면 +1
    count += 1
    # 방문한 집은 0으로
    graph[x][y] = 0 

    # 상하좌우 탐색
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      DFS(nx, ny)

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      DFS(i, j)
      result.append(count)
      count = 0


result.sort()
print(len(result))
for item in result:
  print(item)
