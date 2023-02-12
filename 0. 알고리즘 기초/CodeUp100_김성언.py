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
