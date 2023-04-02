# 프로그래머스
def solution(s):
    answer = ''
    word = s.split(' ')
    num = []
    for i in range(len(word)):
        num.append(int(word[i]))
    num.sort()
    answer = '{} {}'.format(num[0], num[-1])
    return answer
