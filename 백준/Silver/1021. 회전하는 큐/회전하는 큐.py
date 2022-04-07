import collections
N, M = map(int, input().split())
A = list(map(int, input().split()))

deque = collections.deque([i for i in range(1, N+1)])

result = 0

for i in A:
    while True:
        if deque[0] == i:
            deque.popleft()
            break
        else:
            if deque.index(i) < len(deque)/2:
                while deque[0] != i:
                    deque.append(deque.popleft())
                    result += 1
            else:
                while deque[0] != i:
                    deque.appendleft(deque.pop())
                    result += 1

print(result)