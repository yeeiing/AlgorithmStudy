from collections import deque

def bfs(n):
    queue = deque()
    
    queue.append(n)
    
    while queue:
        n = queue.popleft()
        
        if check[n] == 0:
            check[n] = 1
            for v in g[n]:
                queue.append(v)

N = int(input())
g = [[] for _ in range(N+1)]

for _ in range(int(input())):
    n, m = map(int, input().split())
    g[n].append(m)
    g[m].append(n)
    
check = [0]*(N+1)
bfs(1)

print(sum(check)-1)