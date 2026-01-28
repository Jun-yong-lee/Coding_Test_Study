import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

res = []

for each_combi in combinations(nums, 3):
    if sum(each_combi) <= M:
        res.append(sum(each_combi))
res.sort()
print(res[-1])


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

def combi(iter, r):
    arr = list(iter)
    n = len(arr)
    result = []
    path = []

    def dfs(start):
        if len(path) == r:
            result.append(tuple(path))
            return
        
        for i in range(start, n):
            path.append(arr[i])
            dfs(i + 1)
            path.pop()
    dfs(0)
    return result

res = []

for each_combi in combi(nums, 3):
    if sum(each_combi) <= M:
        res.append(sum(each_combi))
res.sort()
print(res[-1])