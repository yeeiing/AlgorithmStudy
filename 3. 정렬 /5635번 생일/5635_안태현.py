import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n): 
  name, day, month, year = input().split()
  arr.append([name, int(day), int(month), int(year)]) # 숫자 정보 int로 변환

arr.sort(key=lambda x:(x[3], x[2], x[1])) # year, month, day 순으로 오름차순 정렬


print(arr[n -1][0])
print(arr[0][0])
