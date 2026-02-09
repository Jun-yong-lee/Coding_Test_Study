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
        dfs(depth+1, i+1)
        
dfs(0, 0)


# 3 1
# 4 5 2