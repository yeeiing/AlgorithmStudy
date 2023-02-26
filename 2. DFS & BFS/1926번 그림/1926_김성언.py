# 1을 찾아나가는 과정은 BFS를 통해 진행
# 1인 경우 찾아나간다. 0인경우 찾아나기지 않는다.
# 2중 for문을 돌면서 1이 나올 때 마다 BFS를 진행 (값은 1, 방문 X일 경우 BFS 진행)

# 아이디어
# - 2중 for => 값은 1 && 방문 X => BFS
# BFS 돌면서 그림 개수 +1, 최대값을 갱신
# 시간복잡도
# O(V + E) => V = M x N, E = V * 4
# 자료구조
# 그래프 전체 지도 : int[][]
# 방문 : bool[][]
# Queue(BFS)

from collections import deque

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y, x):
    rs = 1
    q = deque()
    q.append((y, x))
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return rs

cnt = 0
maxv = 0
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            cnt += 1
            maxv = max(maxv, bfs(j,i))

print(cnt)
print(maxv)


