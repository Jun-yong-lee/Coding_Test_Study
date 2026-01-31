import sys
input = sys.stdin.readline

N, M = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

count = 0

for i in set_a:
    if i not in set_b:
        count += 1

for j in set_b:
    if j not in set_a:
        count += 1
print(count)

# 3 5
# 1 2 4
# 2 3 4 5 6