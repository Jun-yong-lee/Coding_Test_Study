import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
dq = deque(list(range(1, N+1)))
res = []

while True:
    if len(res) == N:
        print("<"+", ".join((map(str, res)))+">")
        break
    for i in range(K-1):
        dq.append(dq.popleft())
    res.append(dq.popleft())