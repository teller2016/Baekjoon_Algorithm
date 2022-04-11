A = input()
B = input()

def solution(A, B):
    i = 0
    result = 0
    length = len(B)
    while i <= len(A)-len(B):
        if A[i:i+length] == B:
            result += 1
            i += length
        else:
            i += 1

    print(result)

solution(A, B)