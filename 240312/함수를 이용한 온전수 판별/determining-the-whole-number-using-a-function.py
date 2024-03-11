def search(x, y):
    cnt = 0
    for i in range(x, y + 1):
        if i % 2 == 0:
            pass
        elif int(list(str(i))[-1]) == 5:
            pass
        elif (i % 3 == 0) and (i % 9 != 0):
            pass
        else:
            cnt += 1
    return cnt
a, b = tuple(map(int, input().split()))
print(search(a, b))