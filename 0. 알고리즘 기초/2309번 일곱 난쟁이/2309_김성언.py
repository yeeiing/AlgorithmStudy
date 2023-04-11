# from itertools import combinations

# heights = [int(input()) for _ in range(9)]
# for seven_man in combinations(heights, 7): # 9C7
#     if sum(seven_man) == 100:
#         sorted_seven_man = sorted(seven_man)
#         for height in sorted_seven_man:
#             print(height)
#         break
    
# # combinations 없이 7중 for 문 -> 9개 중 2개 뽑는 것과 같다
for i in range(9):
    for j in range(i,9):
        print(i,j)
