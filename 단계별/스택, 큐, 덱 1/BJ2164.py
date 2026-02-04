import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
nums = list(range(1, N+1))
dq = deque(nums)

while True:
    if len(dq) == 1:
        print(dq[-1])
        break
    dq.popleft()
    dq.append(dq.popleft())