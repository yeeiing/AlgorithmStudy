import sys
 
input = sys.stdin.readline
 
n, s, r = map(int, input().split())
sTeam = list(map(int, input().split()))
rTeam = list(map(int, input().split()))
 
sList = [0 for i in range(n + 1)]
rList = [0 for i in range(n + 1)]
for item in sTeam:
  sList[item] = 1
 
for item in rTeam:
  rList[item] = 1
 
# 부서진 팀이 자신의 여분을 가지고 있는 경우는 미리 제거
for index, s in enumerate(sList):
  if s == rList[index]:
    rList[index] = 0
    sList[index] = 0
 
#print(sList, rList)
 
result = 0
for i in range(n):
  if sList[i + 1] == 1:
    # 앞에 팀
    if i != 0 and rList[i] == 1:
        rList[i] = 0
        sList[i + 1] = 0
 
    #뒤에 팀
    elif i + 2 != n + 1 and rList[i + 2] == 1:
      rList[i + 2] = 0
      sList[i + 1] = 0
 
    #둘다 없대요ㅠ
    else:
      result += 1
 
print(result)
