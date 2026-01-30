import sys
input = sys.stdin.readline

N = int(input())
res = []

for i in range(N):
    for j in range(N):
        if 5 * i + 3 * j == N:
            res.append(i+j)
if len(res) == 0:
    print("-1")
else:
    print(min(res))