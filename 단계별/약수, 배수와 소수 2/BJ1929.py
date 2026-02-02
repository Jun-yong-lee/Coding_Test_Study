import sys
input = sys.stdin.readline

M, N = map(int, input().split())

arr = [True] * (N + 1)
arr[0] = arr[1] = False

for i in range(2, int(N**(0.5))+1):
    for j in range(i*i, N+1, i):
        arr[j] = False

for k in range(M, N+1):
    if arr[k] == True:
        print(k)