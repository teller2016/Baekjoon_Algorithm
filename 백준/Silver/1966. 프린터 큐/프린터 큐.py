import collections


def solution(n, index, li):
    result = 1
    deque = collections.deque()
    counter = collections.Counter(li)
    for i, num in enumerate(li):
        deque.append([i, num])

    while True:
        if max([num for i, num in deque]) > deque[0][1]:
            deque.append(deque.popleft())
        else:
            if deque[0][0] == index:
                return result
            else:
                deque.popleft()
                result += 1


N = int(input())

for _ in range(N):
    n, index = map(int, input().split())
    li = list(map(int, input().split()))
    print(solution(n, index, li))
