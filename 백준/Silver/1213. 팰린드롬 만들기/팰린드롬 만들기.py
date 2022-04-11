import collections
name = input()

def available(counter):
    count = 0
    for char, cnt in counter:
        if cnt % 2 == 1:
            count += 1

    if count > 1:
        return False

    return True

def solution(name):
    counter = list(collections.Counter(name).items())

    if not available(counter):
        print("I'm Sorry Hansoo")
        return

    counter.sort(key=lambda x:x[0])

    result = ""
    end = ""
    for char, cnt in counter:
        result = result + char * (cnt//2)
        if cnt % 2 == 1:
            end = char

    print(result + end + result[::-1])



solution(name)
