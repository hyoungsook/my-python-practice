def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

x = int(input("첫 번째 숫자: "))
y = int(input("두 번째 숫자: "))

print("더하기:", add(x, y))
print("빼기:", subtract(x, y))
print("곱하기:", multiply(x, y))
print("나누기:", divide(x, y))