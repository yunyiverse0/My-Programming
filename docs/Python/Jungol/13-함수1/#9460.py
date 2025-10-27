# 함수 내부: a = 10, b = 5
# 함수 외부: a = 5, b = 10
# 함수 내부: a = 10, b = 5
# 함수 외부: a = 10, b = 5

def f1():
  a, b = map(int,input().split())
  a, b = b, a
  print(f"함수 내부: a = {a}, b = {b}")
  return a, b
  
b, a = f1()

print(f"함수 외부: a = {a}, b = {b}")

a, b = b, a

def f2():
  print(f"함수 내부: a = {a}, b = {b}")
  return a, b

a, b = f2()

print(f"함수 외부: a = {a}, b = {b}")
