# Project Teams
# 1 2 3 4 5 6 이면 양끝끼리 더해서 구한다!!

import sys
input = sys.stdin.readline

N = int(input()) # 팀 수
ability = list(map(int, input().split())) # 학생 코딩 역량 리스트로 넣음

ability.sort() # 코딩 역량 오름차순 정렬

min = 200000 # 코딩 역량 최솟값
for i in range(N):
    if ability[i] + ability[2*N - i - 1] < min: # 최솟값보다 작으면 최솟값으로 정의
        min = ability[i] +  ability[2*N - i - 1]

print(min)
