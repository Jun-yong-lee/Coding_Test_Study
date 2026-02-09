import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
result = [0] * M

def dfs(depth, start):
    if depth == M:
        print(*result)
        return
    for i in range(start, N):
        result[depth] = nums[i]
        dfs(depth+1, i)

dfs(0, 0)
# 4 2
# 9 8 7 1