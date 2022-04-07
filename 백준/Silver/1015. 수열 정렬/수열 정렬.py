N = int(input())
A = list(map(int, input().split()))
A_list = []
for i, a in enumerate(A):
    A_list.append([i,a])

A_list.sort(key = lambda x:(x[1],x[0]))

dic = {}
for i, val in enumerate(A_list):
    dic[val[0]] = i

result = list(sorted(dic.items(), key=lambda x:x[0]))

list = list(zip(*result))[1]
print(*list)
