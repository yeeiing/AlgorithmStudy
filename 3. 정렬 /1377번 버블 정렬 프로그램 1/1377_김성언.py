# bool changed = false;   # 처음 bool 변수 false
# for (int i=1; i<=N+1; i++) {  # 배열의 수 만큼 N번 동안
#     changed = false; # bool 초기화 
#     for (int j=1; j<=N-i; j++) {  # N에서 i빼고, 1뺀 값 동안
#         if (A[j] > A[j+1]) {   # 앞에 값이 크다면
#             changed = true;    # bool 상태 true로 바꿔주고
#             swap(A[j], A[j+1]);  # 둘의 위치 바꿔주세요
#         }
#     }
#     if (changed == false) {    # j의 loop문에서 값이 바뀌지 않았으면 -> 앞의 값이 뒤의 값보다 큰 경우가 나타나지 않으면 i 값을 출력하고 멈춰라 
#         cout << i << '\n';
#         break;
#     }
# }

#ex) 10, 1, 5, 2, 3 인 경우 
# i = 1: 10 > 1, 10 > 5, 10 > 2, 10 > 3 -> 1, 5, 2, 3, 10       
# i = 2: 1 < 5, 5 > 2, 5 > 3 -> 1, 2, 3, 5, 10
# i = 3, 1 < 2, 2 < 3 -> 1, 2, 3, 5, 10
# --> 아! 버블 정렬을 위해 반복된 바깥 loop문의 횟수를 구하는 문제구나~

# import sys
# input = sys.stdin.readline

# changed = False
# n = int(input())
# arr = []

# for i in range(n):
#     arr.append(int(input()))

# for i in range(n):
#     changed = False
#     for j in range(n-i-1):
#         if arr[j] > arr[j+1]:
#             changed = True
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#     if changed == False:   # 변화 없이 정렬이 완료된 경우
#         print(i+1)
#         break
#     elif i == range(n):
#         print(i+1)
        
# 계속되는 시간 초과 문제,.
# N의 최대 범위가 500,000이므로 버블 정렬을 통해서 문제를 풀면 시간초과가 발생한다..
# 안쪽 for문이 몇 번 수행됐는지 구하는 다른 아이디어가 필요하다.
# C++ 코드에서 안쪽 루프는 1에서 n - j 까지 swap를 수행한다. 이는 특정 데이터가 안쪽 루프에서 swap의 왼쪽으로 이동할 수 있는 최대 거리가 1이라는 뜻이다.
# --> 데이터의 정렬 전 index와 정렬 후 index를 비교해 왼쪽으로 가장 많이 이동한 값을 찾으면 이 문제를 해결할 수 있다..?

# 파이썬에서 제공하는 sort()함수를 이용해 배열을 정렬한다. sort() 함수의 시간 복잡도는 O(nlogn)이다

import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append([int(input()), i])
sorted_arr = sorted(arr)
answer = 0 
for i in range(n):
    answer = max(answer, sorted_arr[i][1] - i + 1)
print(answer)
