import sys
import collections


def solution(n, planes):
    graph = collections.defaultdict(list)
    for a, b in planes:
        graph[a].append(b)
        graph[b].append(a)
    visited = collections.defaultdict(int)
    Q = collections.deque([1])  # total, node
    result = 0
    while Q:
        node = Q.popleft()
        for next_node in graph[node]:
            if next_node not in visited:
                visited[next_node] = 1
                Q.append(next_node)
                result += 1

    return result - 1


T = int(sys.stdin.readline())

for _ in range(T):
    # 국가수 ,비행기 종류
    N, M = map(int, sys.stdin.readline().split())
    plane = []
    for _ in range(M):
        plane.append(list(map(int, sys.stdin.readline().split())))

    print(solution(N, plane))
