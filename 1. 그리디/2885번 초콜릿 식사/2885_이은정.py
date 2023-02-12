# 처음에 풀었을 때 반례
# 5
# answer: 8 3
# wrong: 8 2

import sys
input = sys.stdin.readline
K = int(input())
C = 1 # 최소 초콜릿 길이
i = 1 # 몇 번 곱해졌는지
while(K > C):
    C = 2 ** i
    i += 1
chocolate = C # 밑에서 C를 2로 나눌 거기 때문에 복사

# 반으로 쪼개면서 K개의 초콜릿 만들기
cnt = 0 # 더해지는 초콜릿 수
num = 0 # 몇 번 쪼개지는지 세는 변수
if (K == C):
    pass
else:
    while(cnt < K):
        if(cnt + C//2 > K): # ***쪼개서 더한 수가 주어진 초콜릿 수보다 많으면 더 쪼개야함***
            pass
        else:
            cnt += C // 2
        C = C // 2
        num += 1

print(chocolate, num)
