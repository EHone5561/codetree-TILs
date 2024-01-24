def calculate(a, b):
    sigma = 0
    for i in range(a, b+1):
        prime = True
        for j in range(2, i):
            if (i % j == 0):
                prime = False
        if(prime):
            sigma += i
    return sigma
input = list(map(int, input().split()))
a = input[0]; b = input[1]
print(calculate(a, b))