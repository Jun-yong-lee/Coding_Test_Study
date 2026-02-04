import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
dq = deque()
for _ in range(N):
    cmd = input().rstrip()
    if len(cmd) != 1:
        cmd, value = cmd.split()
        if cmd == "1":
            dq.appendleft(value)
        elif cmd == "2":
            dq.append(value)
    else:
        if cmd == "3":
            if len(dq) == 0:
                print("-1")
            else:
                print(dq.popleft())
        elif cmd == "4":
            if len(dq) == 0:
                print("-1")
            else:
                print(dq.pop())
        elif cmd == "5":
            print(len(dq))
        elif cmd == "6":
            if len(dq) == 0:
                print("1")
            else:
                print("0")
        elif cmd == "7":
            if len(dq) == 0:
                print("-1")
            else:
                print(dq[0])
        elif cmd == "8":
            if len(dq) == 0:
                print("-1")
            else:
                print(dq[-1])
        else:
            print("need check")