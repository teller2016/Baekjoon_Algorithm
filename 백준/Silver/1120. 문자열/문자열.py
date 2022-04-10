A, B = input().split()

def compare(a, b):
    result = 0
    for a, b in zip(a, b):
        if a != '*' and a != b:
            result += 1

    return result


def solution(A, B):
    result = float('inf')
    for i in range(len(B) - len(A) + 1):
        a = '*' * i + A + '*' * (len(B) - len(A) - i)
        result = min(result, compare(a, B))
    print(result)


solution(A, B)
