import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
ans = 0

# 팀을 만들 수 있는 상태이면 계속 돌리기
while N >= 2 and M >= 1 and N+M >= K+3:
    N -= 2
    M -= 1
    ans += 1

print(ans)
