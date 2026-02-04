import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
dq = deque()
for _ in range(N):
    cmd = input().rstrip()
    if cmd[0:4] == "push":
        dq.append(int(cmd.split()[1]))
    elif cmd[0:3] == "pop":
        if len(dq) == 0:
            print("-1")
        else:
            print(dq.popleft())
    elif cmd[0:4] == "size":
        print(len(dq))
    elif cmd[0:5] == "empty":
        if len(dq) == 0:
            print("1")
        else:
            print("0")
    elif cmd[0:5] == "front":
        if len(dq) == 0:
            print("-1")
        else:
            print(dq[0])
    elif cmd[0:4] == "back":
        if len(dq) == 0:
            print("-1")
        else:
            print(dq[-1])
    else:
        print("need arr check")