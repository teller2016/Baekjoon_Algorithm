import collections

N = int(input())
sells = []
for _ in range(N):
    sells.append(input())
sells.sort()
counter = collections.Counter(sells)
print(counter.most_common()[0][0])