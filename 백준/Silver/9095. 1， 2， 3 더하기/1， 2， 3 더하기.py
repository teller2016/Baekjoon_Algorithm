import collections

n = int(input())


def solution(num):
    dic = collections.defaultdict(int)
    dic[1] = 1
    dic[2] = 2
    dic[3] = 4

    for i in range(4, num + 1):
        dic[i] = dic[i - 3] + dic[i - 2] + dic[i - 1]

    return dic[num]


for _ in range(n):
    print(solution(int(input())))
