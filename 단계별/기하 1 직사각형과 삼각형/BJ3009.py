import sys
input = sys.stdin.readline

x = []
y = []

for _ in range(3):
    N, M = map(int, input().split())
    if N in x:
        x.remove(N)
    else:
        x.append(N)
    if M in y:
        y.remove(M)
    else:
        y.append(M)

print(" ".join(list(map(str, x + y))))