# 카약과 강풍
import sys
input = sys.stdin.readline

N, S, R = map(int, input().split())
demage = list(map(int, input().split()))
extras = list(map(int, input().split()))

kayak = []
# 손상된 팀이랑 여분있는 팀이 같으면 없애기
original_demage = demage[:] # 원래 demage 리스트 복사
for i in range(len(original_demage)):
    if original_demage[i] in extras:
        extras.remove(original_demage[i])
        demage.remove(original_demage[i])
        
for k in range(1, N+1):
    if k not in demage:
        kayak.append(k)
    else: # 손상된 카약이라면
        for extra in extras:
            if (k == extra + 1) or (k == extra - 1):
                kayak.append(k)
                extras.remove(extra)
                break

print(N - len(kayak))
