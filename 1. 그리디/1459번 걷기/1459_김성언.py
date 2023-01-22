import sys
input = sys.stdin.readline

x, y, w, s = map(int, input().split())
# 할 수 있는거 다 해보고 최소값 출력해주기
# i) 한 블록씩만 가기 
time_1 = (x + y) * w
# 1. x-y가 짝수일 경우
if abs(x - y)%2==0:
    # ii) 대각선으로만 가기
    time_2 = max(x, y) * s
# 2. x-y가 홀수일 경우
else : 
    # # i) 한 블록 씩 가기 (4,2) -> 6번
    # time_1 = (x + y) * w
    # ii) 대각선으로 최대한 가고 한 블록씩 가기
    time_2 = (max(x, y) - 1) * s + w

time_3 = (min(x, y) * s) + (abs(x-y) * w)

print(min(time_1, time_2, time_3))