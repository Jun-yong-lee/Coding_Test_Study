"""
1. 아이디어
- python deque를 활용하여 정수를 저장하는 덱 수현
- push_front, push_back, pop_front, pop_back, size, empty, front, back 명령 구현

2. 시간복잡도
- 입력: N * O(1)
- 출력: N * O(1)
- 전체: O(N)

3. 변수
- N: int, 명령의 수
- dq: deque[int]
- cmds: list[str], 입력으로 받은 명령 문자열

"""

import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
dq = deque()
cmds = [input() for _ in range(N)]

for cmd in cmds:
    if cmd[:10] == "push_front":
        dq.appendleft(int(cmd[11:]))
    elif cmd[:9] == "push_back":
        dq.append(int(cmd[10:]))
    elif cmd[:9] == "pop_front":
        if len(dq) != 0:
            pop_value = dq.popleft()
            print(pop_value)
        else: print("-1")
    elif cmd[:8] == "pop_back":
        if len(dq) != 0:
            pop_value = dq.pop()
            print(pop_value)
        else: print("-1")
    elif cmd[:4] == "size":
        print(len(dq))
    elif cmd[:5] == "empty":
        if len(dq) != 0: print("0")
        else: print("1")
    elif cmd[:5] == "front":
        if len(dq) != 0: print(dq[0])
        else: print("-1")
    elif cmd[:4] == "back":
        if len(dq) != 0: print(dq[-1])
        else: print("-1")
    else:
        print("[Error] need check")