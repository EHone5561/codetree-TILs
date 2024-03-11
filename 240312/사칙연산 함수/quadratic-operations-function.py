def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x // y

a, o, c = tuple(input().split())
a, c = map(int, (a, c))
if (o == '+'):
    answer = add(a, c)
    print(f"{a} {o} {c} = {answer}")
elif (o == '-'):
    answer = sub(a, c)
    print(f"{a} {o} {c} = {answer}")
elif (o == '*'):
    answer = mul(a, c)
    print(f"{a} {o} {c} = {answer}")
elif (o == '/'):
    answer = div(a, c)
    print(f"{a} {o} {c} = {answer}")
else:
    print(False)