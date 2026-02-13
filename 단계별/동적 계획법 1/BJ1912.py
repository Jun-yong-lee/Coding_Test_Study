import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

res = [0] * n
res[0] = nums[0]

for i in range(1, n):
    sum_of_them = nums[i] + res[i-1]
    if sum_of_them < nums[i]:
        res[i] = nums[i]
    else:
        res[i] = sum_of_them

print(max(res))