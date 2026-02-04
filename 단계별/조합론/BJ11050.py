import sys
from itertools import combinations
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(range(1, N+1))
count = 0

for combi in combinations(nums, K):
    count += 1
print(count)
