import sys
input = sys.stdin.readline

N = int(input())
res = []

for _ in range(N):
    num = int(input())
    if num == 0:
        res.pop()
    else:
        res.append(num)
print(sum(res))

# 4
# 3
# 0
# 4
# 0