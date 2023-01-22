# 주식 하나를 산다.
# 원하는 만큼 가지고 있는 주식을 판다. 
# 아무것도 안한다.

import sys
input = sys.stdin.readline

t = int(input()) # 테스트 케이스 개수 T
# 최적의 해를 보장해야하지 않을까?
for i in range(t):
    day = int(input()) # 날의 수를 나타내는 자연수 N
    
    price = list(map(int, input().split())) # 날 별 주가를 나타내는 자연수 N
    profit = 0 # 이익을 나타내는 변수
    last =  price[-1] # 마지막 날 주식의 가격
    
    for j in range(day-1,-1,-1): # 거꾸로 확인하는 코드    1 2 3 4 -> 4 3 2 1        
        if price[j] < last: # N번째 날 주식이 증가하면 (N번째 날 - 오늘 주식)만큼 이득이 생긴다.
            profit = profit + last-price[j]
        else: # N번째 날 날 주식이 감소하면 j날 팔자
            last = price[j]
    print(profit)
    
# 왜 뒤에서부터 접근하는가?
# 내일 주식이 비싸다는 것이 N일 동안 주식의 최대값을 보장하지 않으므로

# 좋은 정리 글
# 아래와 같은 동작을 생각해볼 수 있습니다. (단, stock[d]는 d일의 주식 가격)
# stock[d] < stock[d+1]이면, 주식을 산다.
# stock[d] > stock[d+1]이면, 주식을 판다.
# stock[d] == stock[d+1]이면 아무것도 안 한다.
# 하지만, stock[d] > stock[d+1]이더라도 stock[d] < stock[m] 일 수 있습니다. (단, d < m)
# 즉, 주식이 다음날 떨어지더라도, 나중에 오를 수 있기 때문에 바로 팔지 않아도 나중에 수익을 낼 수 있습니다. 
 
# 따라서 아래와 같이 행동하면 최대 이익을 계산할 수 있습니다.
# stock[d] < stock[m]인 m이 존재하면, d일에 주식을 사고 m일에 주식을 판다. (단, d < m)
 
# 하지만, 매번 d일 이후에 stock[d] < stock[m]인 m이 존재하는 지 확인하면 시간 복잡도가 O(N2)입니다.
# 하지만, n이 최대 1,000,000이기 때문에 이러한 방식의 경우 시간 초과가 발생할 수 있습니다.
 
# 따라서 d부터 n - 1일까지일 중 가장 주가가 높은 날을 저장하는 배열을 만들어주어야 합니다.