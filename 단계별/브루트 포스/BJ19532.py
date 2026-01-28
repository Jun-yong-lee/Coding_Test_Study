import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

y = (a*f-d*c) / (a*e - b*d)
x = (e*c-b*f) / (a*e - b*d)

print(" ".join([str(int(x)), str(int(y))]))

# 1 3 -1 4 1 7


import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

for i in range(-999, 999+1):
    for j in range(-999, 999+1):
        if (a*i + b*j == c) and (d*i + e*j == f):
            print(i, j)
            break