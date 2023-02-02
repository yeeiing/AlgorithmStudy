import sys
input = sys.stdin.readline

question = input().split('\n') #'\n'을 기준으로 잘랐으므로 주어진 문장은 question[0]
search = input().split('\n') #'\n'을 기준으로 잘랐으므로 주어진 문장은 search[0]

print(question[0].count(search[0])) # 개수세기
