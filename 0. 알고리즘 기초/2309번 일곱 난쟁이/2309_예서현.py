# 조합 코드 사용
from itertools import combinations

# 9명의 난쟁이 정보 입력 받기 및 총 합 구하기
total = 0
array = []
for i in range(9):
    array.append(int(input()))
    total += array[i]

comb = list(combinations(array,7)) # 조합으로 7명 정보 뽑기

for i in range(len(comb)):
    if sum(comb[i]) == 100:
        result = sorted(comb[i]) # 오름차순 정렬
        for j in result:
            print(j)
        break