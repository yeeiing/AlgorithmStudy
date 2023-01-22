import sys
input = sys.stdin.readline
n, m = map(int, input().split()) # n: 과목 수, m: 마일리지

res = []
for _ in range(n):
    P, L = map(int, input().split()) # P: 지원자, L: 수강인원
    mile = list(map(int, input().split())) 


    if P < L: # 수강인원보다 지원자가 적으면
        res.append(1) # 성준이는 1마일리지만 내도 뽑힘
        
    elif P == L: # 수강인원 == 지원자라면
        mile.sort(reverse = True) # 마일리지가 큰 순서로 정렬
        res.append(mile[L-1]) # 성준이는 가장 적게 낸 마일리지 그대로 냄
                 # 마일리지 같다면 성준이가 우선순위
    else:
        mile.sort(reverse = True)
        res.append(mile[L-1]) # 턱걸이 지원자만큼 내면 됨
        

res.sort() # 지금까지 성준이가 낼 마일리지를 오름차순으로 정렬
# 적은 걸 많이 내는 게 더 유리

cnt = 0
sum = 0
for i in range(n):
    sum += res[i]
    cnt += 1
    if sum > m: # 합이 m보다 크거나 같으면 break
        cnt = i
        break
    elif sum == m:
        cnt = i+1
        break


print(cnt)
