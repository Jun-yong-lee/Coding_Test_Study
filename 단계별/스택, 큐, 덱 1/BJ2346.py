import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split())) # 3 2 1 -3 -1

dq = deque()
for i, v in enumerate(nums):
    dq.append((i+1, v))

res = []

while True:
    idx, move = dq.popleft()
    res.append(idx)

    if len(dq) == 0:
        break

    if move > 0:
        for _ in range(move - 1):
            dq.append(dq.popleft())
    else:
        for _ in range(-move):
            dq.appendleft(dq.pop())
print(" ".join(list(map(str, res))))

# 5
# 3 2 1 -3 -1