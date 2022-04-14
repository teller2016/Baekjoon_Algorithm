import collections
N = int(input())

def solution(n):
    dic = collections.defaultdict(int)
    dic[0] = 1
    dic[1] = 1
    dic[2] = 1
    dic[3] = 2
    dic[4] = 2
    for i in range(5, n):
        dic[i] = dic[i-1] + dic[i-5]

    return dic[n-1]

for _ in range(N):
    m = int(input())
    print(solution(m))