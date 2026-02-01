import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
count = 0

diff_nums = list(set([abs(nums[i-1]-nums[i]) for i in range(1, len(nums))]))

def gcd(a, b):
    while True:
        if b == 0:
            break
        a, b = b, a % b
    return a

for i in range(len(diff_nums)):
    if i == 0:
        gcd_value = diff_nums[i]
    else:
        gcd_value = gcd(gcd_value, diff_nums[i])

print(((nums[-1] - nums[0]) // gcd_value + 1) - len(nums))

# 4
# 1
# 3
# 7
# 13