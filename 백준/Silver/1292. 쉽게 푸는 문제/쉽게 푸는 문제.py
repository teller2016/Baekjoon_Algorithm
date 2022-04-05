a, b = map(int, input().split())
total = 0


def plus(n):
    total = 0
    cnt = 1
    i = 1
    j = 1
    while cnt <= n:
        cnt += 1
        total += i
        if i == j:
            i += 1
            j = 1
            continue
        j += 1

    return total


print(plus(b) - plus(a - 1))
