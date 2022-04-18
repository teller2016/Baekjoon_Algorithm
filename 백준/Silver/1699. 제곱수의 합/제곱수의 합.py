def solution(n):
    dic = [i for i in range(n+1)]
    for i in range(1, n + 1):
        for j in range(1, i):
            if j*j > i:
                break
            if dic[i] > dic[i - j*j] + 1:
                dic[i] = dic[i - j*j] + 1

    return dic[n]


N = int(input())
print(solution(N))
