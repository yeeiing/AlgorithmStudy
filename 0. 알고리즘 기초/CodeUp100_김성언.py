# 6001
print("Hello")

# 6002 
print("Hello World")

# 6003
print("Hello")
print("World")

# 6004
print("'Hello'")

# 6005
print('"Hello World"')

# 6006
print('"!@#$%^&*()\'') # \를 사용하여 ", '를 출력할 수 있다.
print('"!@#$%^&*()'+ "'")

# 6007
print("\"C:\\Download\\'hello'.py\"")

# 6008 
print('print("Hello\\nWorld")')

# [기초-입출력]
# 6009
n = input()
print(n)

# 6010 
n = input()
print(int(n))

# 6011
n = input()
print(float(n))

# 6012
n = input()
m = input()
print(n)
print(m)

# 6013
n = input()
m = input()
print(m)
print(n)

# 6014 
n = input()
for i in range(3):
    print(n)
    
# 6015
n = list(map(int, input().split()))
for i in range(2):
    print(n[i])
n, m = input().split()
print(n)
print(m)

# 6016
n, m = input().split()
print(m, n)

# 6017 
n = input()
print(n, n, n)

# 6018
time, second = input().split(":")
print(time, second, sep = ":")
# print(?, ?, sep=':') 를 사용하면 콜론 ':' 기호를 사이에 두고 값을 출력한다.
# sep 는 분류기호(seperator)를 의미한다.

# 6019
year, month, day =  input().split('.')
print(day, month, year, sep="-")

# 6020
n, m = input().split("-")
print(n, m, sep='')

# 6021
n = input()
for i in range(len(n)):
    print(n[i])
    
# 6022
n = input()
print(n[0:2],n[2:4],n[4:6])

# 6023
# n = input()
# print(n[3:5])
hour, minute, second = input().split(":")
print(minute)


# 6024
a, b =input().split()
print(a+b)

# 6025 
n = list(map(int, input().split()))
print(n[0] + n[1])

# 6026 
a = float(input())
b = float(input())
print(a+b)

# 6027
# https://velog.io/@robinyeon/python-16진수로-출력하기
n = int(input())
print("%x"%n)

# 6028
# print('%X' % n)  #n에 저장되어있는 값을 16진수 대문자 형태 문자열로 출력
n = int(input())
print("%X"%n)

# 6029
# n = hex(int(input()))
a = input() 
n = int(a, 16)      #입력된 a를 16진수로 인식해 변수 n에 저장 
print('%o' % n)  #n에 저장되어있는 값을 8진수(octal) 형태 문자열로 출력 

# 6030
n = ord(input())
print(n)

# 6031
c = int(input())
print(chr(c)) 

# 6032
n = int(input())
print(-n)
# 단항(unary) 연산자인 -(negative)를 변수 앞에 붙이면 부호가 반대인 값이 된다. 

# 6033
n = ord(input())
print(chr(n+1))

# 6034
n, m = input().split()
print( int(n) - int(m))

# 6035
n, m = input().split()
print( float(n) * float(m))

# 6036
n, m = input().split()
print(n*int(m))

# 6037
n = int(input())
m = input()
print(n * m)

# 6038
n, m = input().split()
print(int(n)**int(m))

# 6039
n, m = input().split()
print(float(n)**float(m))

# 6040
n, m = input().split()
print(int(n)//int(m))

# 빠른 입출력 # 15552 빠른 A+B # 기업 코테에선 거의 X, 대회에선 쓸 수 O
import sys
input = sys.stdin.readline()
# 오버플로우: 자료형이 담을 수 있는 범위를 초과 (Python 고려 X, 기업 코테 거의 X)
# 딕셔너리 : Key, Value, 삽입/삭제
# set : 중복 X,
s = set()
s.add(12)
s.add(12)
s.add(34)
s.add(54)
print(s)
s.pop() # 랜덤으로 한 값이 빠짐 -> 유용X
s.remove(54) # 특정 값 빼기
s.clear()
print(s)
