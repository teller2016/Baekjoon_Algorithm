import collections

N = int(input())


def solution(n):
    dic = collections.defaultdict(int)
    dic[1] = 0

    for i in range(2, n + 1):
        dic[i] = dic[i-1] + 1
        if i % 3 == 0:
            dic[i] = min(dic[i], dic[i//3]+1)
        if i % 2 == 0:
            dic[i] = min(dic[i], dic[i//2]+1)

    return dic[n]


print(solution(N))
