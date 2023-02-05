# import sys
# input = sys.stdin.readline

n = int(input()) # 수의 개수
arr = []

for i in range(n):
    arr.append(int(input()))   # int로 형 변환 후 list에 넣어주자!!!!!!!!!!!!!!!!!!!!!

# 배열의 크기 만큼 반복
for i in range(len(arr)):
    # 배열의 크기에서 i 값과 1을 뺀 만큼 반복 
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]: # 앞에 있는 값이 더 크면 바꾼다.
            swap = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = swap
            
# 정답 출력하는 부분            
for i in range(len(arr)):
    print(arr[i])    
    
    

# sort 함수 이용한 풀이 
n = int(input()) # 수의 개수
arr = []

for i in range(n):
    arr.append(int(input()))   # int로 형 변환 후 list에 넣어주자!!!!!!!!!!!!!!!!!!!!!
arr.sort()
for i in range(len(arr)):
    print(arr[i])  
