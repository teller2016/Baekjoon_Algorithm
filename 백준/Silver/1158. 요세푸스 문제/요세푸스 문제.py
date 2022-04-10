import collections
N, K = map(int, input().split())

def solution(N, K):
    deque = collections.deque([i for i in range(1, N + 1)])
    result = []
    while deque:
        for _ in range(K-1):
            deque.append(deque.popleft())
        result.append(deque.popleft())

    print(f"<{', '.join(map(str,result))}>")

solution(N, K)