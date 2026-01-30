import sys
input = sys.stdin.readline

N = int(input())
nums = list(set([int(input()) for _ in range(N)]))
nums.sort()
for i in nums:
    print(i)