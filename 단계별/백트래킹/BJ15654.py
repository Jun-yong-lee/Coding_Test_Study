import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

visited = [False] * (N+1)

def dfs(depth, selected, visited):
    if depth == M:
        print(*selected)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            selected.append(nums[i])
            dfs(depth+1, selected, visited)
            selected.pop()
            visited[i] = False
dfs(0, [], visited)

# seq = []

# def dfs():
#     if len(seq) == M:
#         print(*seq)
#         return
    
#     for i in nums:
#         if i not in seq:
#             seq.append(i)
#             dfs()
#             seq.pop()

# dfs()

# 3 1
# 4 5 2