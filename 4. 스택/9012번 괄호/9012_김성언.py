n = int(input())
for _ in range(n):
    data = input()
    stack = []
    status = True
    for str in data:
        if str == '(':
            stack.append(str)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                status = False #no
                break
    if len(stack) != 0:
        status = False
    
    if status:
        print('YES')
    else:
        print('NO')