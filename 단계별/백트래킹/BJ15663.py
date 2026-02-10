import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [False] * (N+1)

result = [0] * M
res = []

def dfs(depth):
    if depth == M:
        res.append(tuple(result))
        return
    for i in range(len(nums)):
        if visited[i] == False:
            visited[i] = True
            result[depth] = nums[i]
            dfs(depth+1)
            visited[i] = False

dfs(0)
res = sorted(list(map(list, set(res))))
for i in res:
    print(*i)