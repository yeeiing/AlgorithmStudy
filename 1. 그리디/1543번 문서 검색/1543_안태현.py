document = input()
word = input()

length = len(document)

ans = 0
i = 0 # 단어를 찾기 시작할 index
while len(document) - i >= len(word): # 문서의 길이 - i가 찾을 단어와 같거나 작아진다면 loop 탈출
  if document[i : i + len(word)] == word: # i부터 단어의 길이만큼 봤을때 단어와 일치하는지 확인
    i += len(word) # 일치한다면 겹치는 부분을 건너뛰기 위해 단어만큼 index 증가
    ans += 1
  else:
    i += 1
print(ans)
