import collections

N = int(input())
data = []
for _ in range(N):
    state, student, score = list(map(int, input().split()))
    data.append([state, student, score])

data.sort(key=lambda x: -x[2])

maxTwo = collections.defaultdict(int)
result = []

count = 0
for state, student, score in data:
    if count >= 3:
        break
    if maxTwo[state] < 2:
        maxTwo[state] += 1
        result.append([state, student])
        count += 1

for state, student in result:
    print(state, student)