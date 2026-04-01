# DFS 풀이
import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 1:
                dfs(nx, ny)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1
    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)