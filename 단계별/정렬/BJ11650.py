import sys
input = sys.stdin.readline

N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]

nums.sort(key=lambda x:(x[0], x[1]))
for each_num in nums:
    print(" ".join(list(map(str, each_num))))