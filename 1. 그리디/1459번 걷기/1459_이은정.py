import sys
input = sys.stdin.readline
x, y, w, s = map(int, input().split())

# 가로세로로 가기
res1 = (x+y)*w

# 대각선으로만 이동
if (x+y)%2 == 0:
    res2 = max(x,y)*s
# 대각선 + 평행이동 1번
else:
    res2 = (max(x,y)-1)*s + w

# 대각선 + 평행이동
res3 = (min(x,y)*s) + (abs(x-y)*w)

print(min(res1, res2, res3))
