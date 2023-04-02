# 프로그래머
def solution(cards1, cards2, goal):
    answer = ''
    stack1 = []
    stack2 = []
    
    # cards1 스택에 넣기
    for i in range(len(cards1)):
        stack1.append(cards1[i])
        
    # cards2 스택에 넣기
    for i in range(len(cards2)):
        stack2.append(cards2[i])
    
    
    stack1.reverse()
    stack2.reverse()
    
    status = 0 # 0이면 만들 수 있고 1이면 만들 수 없음
    for i in range(len(goal)):
        if stack1 != []:
            if goal[i] == stack1[-1]:
                stack1.pop()
                continue
                
        if stack2 != []:
            if goal[i] == stack2[-1]:
                stack2.pop()
                continue
            
        status = 1
        break
        
    
    if status == 1:
        answer = 'No'
    else:
        answer = 'Yes'

        
    return answer
