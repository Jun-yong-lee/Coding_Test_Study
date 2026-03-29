import sys
import math

input = sys.stdin.readline

N = list(map(int, input().rstrip()))

nums = [0] * 10

for i in N:
    nums[i] += 1
# nums[6] = math.ceil((nums[6] + nums[9]) / 2)
nums[6] = (nums[6] + nums[9] + 1) // 2
nums[9] = 0
print(max(nums))
