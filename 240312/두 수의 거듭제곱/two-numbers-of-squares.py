def power(a, b):
    return a**b
a, b = tuple(map(int, input().split()))
print(power(a, b))