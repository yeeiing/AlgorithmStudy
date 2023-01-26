import sys
input = sys.stdin.readline

N = int(input())
predict = [int(input()) for _ in range(N)] # 엔터를 기준으로 리스트에 넣기

predict.sort() # 예상등수 정렬

result = 0
for i in range(1, N+1): # 1등부터 시작하므로 1부터 시작
    result += abs(predict[i-1] - i) # 리스트는 0부터 시작이므로 인덱스는 i-1

print(result)
