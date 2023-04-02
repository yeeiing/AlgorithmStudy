# 프로그래머스
def solution(s):
    answer = True
    stack = []
    for i in range(len(s)):
        if s[i] == '(': # 열린 괄호면 스택에 넣기
            stack.append('(')
        elif s[i] == ')': # 닫힌 괄호면 스택 빼기
            if stack != []: # 스택이 비어있지않으면
                stack.pop()
            else:
                answer = False
                break
        else:
            answer = False
            break
    
    if stack != []:
        answer = False


    return answer
