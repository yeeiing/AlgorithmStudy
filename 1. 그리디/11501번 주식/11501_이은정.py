# 거꾸로 접근
import sys
input = sys.stdin.readline
T = int(input())

price_list = []
benefit = 0

for _ in range(T):
    n = int(input())
    price_list = list(map(int, input().split()))
    max = price_list[n-1] # 마지막 값을 max로 지정
    for i in range(len(price_list)-2, -1, -1): # 마지막 인덱스부터 거꾸로
        if price_list[i] >= max: # 새로운 최댓값이 나오면 다시 선언
            max = price_list[i]
        else: # price_list[i] < max   매번 benefit 갱신
            benefit += max - price_list[i]

    print(benefit)
    price_list.clear()
    benefit = 0
            

