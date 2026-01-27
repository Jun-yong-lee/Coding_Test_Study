import sys
input = sys.stdin.readline

N, M = map(int, input().split())

res = []
for i in range(1, N+1):
    if N % i == 0:
        res.append(i)

if M-1 >= len(res):
    print("0")
else:
    print(res[M-1])