import sys
input = sys.stdin.readline

n = int(input())
# arr = []

# arr = list(map(int, input().split()))
# 아 index를 저장해야지.,
# for i in range(n):
#     arr.append([int(input()),i])   
# 근데 이러면 띄어쓰기로 넣지 못하고 그냥 넣어버리네?

arr = list(map(int, input().split()))
arr.sort()
for i in range(1,n):
    arr[i] = arr[i] + arr[i-1]
print(sum(arr))
# arr_index = []
# for i in range(n):
#     arr_index.append([arr[i],i])
# #sorted_arr = arr.sort()

# # sorted_arr = arr_index.sort()
# # print(sorted_arr)
# # ㄴ> 이거 하면 왜 None 나오지?

# # print(sorted(arr_index))
# sorted_arr = sorted(arr_index)
# sum = []
# # print(sorted_arr)  # 잘 정렬된 것 확인 완료

# for i in range(n):
#     sum.append(sorted_arr[i][1])
# print(sum)
