line = input()


def solution(line):
    total = 0
    stack = []
    i = 0
    while i < len(line):
        if i + 1 < len(line) and line[i] == '(' and line[i + 1] == ')':
            total += len(stack)
            i += 2
        elif line[i] == '(':
            stack.append(line[i])
            i += 1
        elif line[i] == ')':
            total += 1
            stack.pop()
            i += 1

    return total


print(solution(line))
