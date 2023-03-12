s = input()

stack = []
length = 0
str =''

for item in s:
  # 현재 item이 숫자라면 길이 +1, str은 현재 item
  if item.isdigit():
    length += 1
    str = item

  # (를 만났다면 str은 반복된 개수, length - 1은 그전까지의 전체 길이
  elif item == '(':
    stack.append((str, length - 1))
    length = 0 # 초기화, 괄호 안에 괄호가 또 있을 경우 대비
  else:
    # )를 만났을때
    # iter * () 사이에 있는 문자열 길이 + (부터 iter 전까지의 길이
    iter, pre = stack.pop()

    length = (int(iter) * length) + pre

print(length)
