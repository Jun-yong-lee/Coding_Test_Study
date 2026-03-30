# DFS, BFS
import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

# 인접 리스트 만들기
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

visited_dfs = [False] * (N + 1)

def dfs(V):
    visited_dfs[V] = True
    print(V, end=" ")
    for i in graph[V]:
        if not visited_dfs[i]:
            dfs(i)

visited_bfs = [False] * (N + 1)

def bfs(V):
    visited_bfs[V] = True
    queue = deque([V])
    while queue:
        now = queue.popleft()
        print(now, end=" ")
        for next_node in graph[now]:
            if not visited_bfs[next_node]:
                visited_bfs[next_node] = True
                queue.append(next_node)
dfs(V)
print()
bfs(V)