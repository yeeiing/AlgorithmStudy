import sys
input = sys.stdin.readline

num = list(input())
num = num[:len(num)-1]

num.sort(reverse=True)
print("".join(num))
