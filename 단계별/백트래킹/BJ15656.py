import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

result = [0] * M

def dfs(depth):
    if depth == M:
        print(*result)
        return
    
    for i in range(N):
        result[depth] = nums[i]
        dfs(depth+1)
dfs(0)

# 4 2
# 9 8 7 1