def calculate(a, b):
    if a * b <= 1000:
        return a * b
    else:
        return a + b

print(calculate(20, 30))