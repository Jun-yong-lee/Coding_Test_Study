"""
1. 아이디어
- deque를 활용하여 큐 구현
- push, pop, size, empty, front, back 구현

2. 시간복잡도
- N개 명령: N * O(1)
- 전체: O(N)

3. 변수
- N: int, 입력 개수
- q: deque[int]
- cmds: list[str], 입력으로 받은 명령 문자열

"""

from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
q = deque()

cmds = [input() for _ in range(N)]

for cmd in cmds:
    if cmd[:4] == "push":
        q.append(int(cmd[5:]))
    elif cmd[:3] == "pop":
        if len(q) != 0:
            pop_num = q.popleft()
            print(pop_num)
        else: print("-1")
    elif cmd[:4] == "size":
        print(len(q))
    elif cmd[:5] == "empty":
        if len(q) != 0: print("0")
        else: print("1")
    elif cmd[:5] == "front":
        if len(q) != 0: print(q[0])
        else: print("-1")
    elif cmd[:4] == "back":
        if len(q) != 0: print(q[-1])
        else: print("-1")
    else:
        print("[Error] need check")