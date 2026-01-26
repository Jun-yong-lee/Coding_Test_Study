import sys
input = sys.stdin.readline

peaces = list(map(int, input().split()))
right_set = [1, 1, 2, 2, 2, 8]

res = []

for i, each_peace in enumerate(peaces):
    res.append(right_set[i] - each_peace)

print(" ".join(list(map(str, res))))