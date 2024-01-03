list = [] # 입력된 정수를 관리할 리스트 생성

k = int(input()) # 정수 입력받기

for i in range(k):
    num = int(input())

    if num==0:
        list.pop()
    else:
        list.append(num)

print(sum(list))