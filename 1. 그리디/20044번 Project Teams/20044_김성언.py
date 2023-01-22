# 전형적인 그리디 문제라고 생각
# 큰 순서대로 정렬해서~ 착착착 가장 작은 값 출력
import sys
input = sys.stdin.readline

n = int(input())
member = list(map(int, input().split()))

sorted_member = sorted(member)  # 1 2 3 5 7 9
reverse_sorted_member = sorted(member, reverse = True)   # 기본은 오름차순, 내림차순을 위해 reverse= True 9 7 5 3 2 1
 
list = [] 
for i in range(n): # 짝수이므로 //2도 상관 없다.
    ability = int(sorted_member[i] + reverse_sorted_member[i])
    list.append(ability)
    
print(min(list))