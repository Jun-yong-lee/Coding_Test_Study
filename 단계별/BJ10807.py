import sys

input = sys.stdin.readline
N = int(input())

nums = list(map(int, input().split()))
target_num = int(input())

count = 0

for each_num in nums:
    if target_num == each_num:
        count += 1

print(count)