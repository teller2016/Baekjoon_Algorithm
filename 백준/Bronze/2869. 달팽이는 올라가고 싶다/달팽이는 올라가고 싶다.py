import math
A, B, V = map(int, input().split())

def solution(A, B, V):
    result = math.ceil((V - B) / (A - B))
    print(result)

solution(A, B, V)