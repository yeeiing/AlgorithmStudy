# 흙길 보수하기
import sys
input = sys.stdin.readline
N, L = map(int, input().split())

result = 0
soil = []
for _ in range(N): # 2차원 배열로 만들기
    s, e = map(int, input().split())
    temp = [s, e]
    soil.append(temp)
# soil = [[list(map(int, input().split())) for _ in range(N)]]
        
# start 기준으로 정렬하기
soil.sort(key=lambda x:x[0])


ans = 0 # 최종 필요한 널판지의 수
ptr = soil[0][0] # 널판지 시작 위치
for start, end in soil:
    if ptr > end: # 널판지가 커버하면 넘어가기
        continue
    elif ptr < start: # 널판지 시작 재설정
        ptr = start

    dist = end - ptr # 널판지가 필요한 거리
    rest = 1 # 여분
    if dist % L == 0:# 나누어떨어지면 여분 필요없으므로, 0
        rest = 0

    cnt = dist // L + rest
    ptr += cnt*L # 널판지 시작 위치 재설정
    ans += cnt

print(ans)
