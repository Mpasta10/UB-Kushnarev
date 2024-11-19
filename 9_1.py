a = int(input())
b = int(input())
def f(a, b):
    a, b = abs(a), abs(b)
    if a >= b:
        return f(a-b, b)
    else:
        return a
print(f(a, b))
