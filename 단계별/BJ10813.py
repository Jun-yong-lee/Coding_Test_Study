import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [i for i in range(0, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    arr[i], arr[j] = arr[j], arr[i]

print(" ".join(list(map(str, arr[1:]))))