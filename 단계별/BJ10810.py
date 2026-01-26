import sys
input = sys.stdin.readline
N, M = map(int, input().split())
d_input = [list(map(int, input().split())) for _ in range(M)]

basket = [0] * (N + 1)

for i, j, k in d_input:
    for l in range(i, j+1):
        basket[l] = k

print(" ".join(list(map(str, basket[1:]))))