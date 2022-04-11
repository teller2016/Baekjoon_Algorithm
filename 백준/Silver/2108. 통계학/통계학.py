import collections
import sys
n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))


def most(num):
    counter = collections.Counter(num)
    most_count = counter.most_common(2)
    if len(most_count) > 1:
        if most_count[0][1] == most_count[1][1]:
            return most_count[1][0]
        else:
            return most_count[0][0]
    else:
        return most_count[0][0]


def solution(nums):
    nums.sort()
    print(round(sum(nums) / len(nums)))
    print(nums[len(nums) // 2])
    print(most(nums))
    print(nums[-1] - nums[0])


solution(nums)
