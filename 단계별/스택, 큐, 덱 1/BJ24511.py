import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split())) # 큐 -> 0, 스택 -> 1
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

res = []
dq = deque()
for i in range(N):
    if A[i] == 0:
        dq.append(B[i])

for j in range(M):
    dq.appendleft(C[j])
    res.append(dq.pop())

print(" ".join(map(str, res)))
     

# 4
# 0 1 1 0
# 1 2 3 4
# 3
# 2 4 7