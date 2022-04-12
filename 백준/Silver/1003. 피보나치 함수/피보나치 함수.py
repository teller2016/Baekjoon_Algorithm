import collections
N = int(input())
case = []
for _ in range(N):
    case.append(int(input()))

def solution(num):
    if num == 0:
        return [1, 0]

    dic = collections.defaultdict(int)
    dic[1] = 1
    def fibo(n):
        if n<=1 or dic[n] :
            return dic[n]
        dic[n] = fibo(n-1) + fibo(n-2)

        return dic[n]

    return [fibo(num-1), fibo(num)]



for c in case:
    print(*solution(c))