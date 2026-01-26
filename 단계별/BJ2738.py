# 3 3
# 1 1 1
# 2 2 2
# 0 1 0
# 3 3 3
# 4 4 4
# 5 5 100

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

arr = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        arr[i][j] = A[i][j] + B[i][j]

for k in range(N):
    print(" ".join(list(map(str, arr[k]))))

