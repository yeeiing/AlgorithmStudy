import sys
input=sys.stdin.readline

n = int(input())
num = 0

list = [] # 입력받은 정수 담을 리스트 생성

for i in range(n):
    order = input().split()

    if order[0] == "push":
        num = order[1]
        list.append(num)
    
    elif order[0] == "pop":
        if len(list) == 0:
            print(-1)
        else:
            print(list[-1])
            list.pop()

    elif order[0] == "size":
        print(len(list))

    elif order[0] == "empty":
        if len(list) == 0:
            print(1)
        else:
            print(0)

    elif order[0] == "top":
        if len(list) == 0:
            print(-1)
        else:
            print(list[-1])
