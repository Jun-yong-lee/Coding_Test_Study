"""
1. 아이디어
- 편집기의 커서를 기준으로 문자열을 나누어 스택으로 관리

2. 시간복잡도
# insert, pop(0)를 활용할 시, for문과 insert, pop이 사용되어서 N^2이 됨 --> 시간초과
- 입력: N * O(1)
- Stack 활용 맨뒤 삽입: O(1)
- 맨 뒤 제거: O(1)
- 출력: O(1)
- 전체: O(N)

3. 변수
- strings: str, 입력 문자열
- N: int, 명령어의 개수
- cmds: list[str], 명령어
- strings_r, strings_l: list[str]
"""

import sys

input = sys.stdin.readline
strings = list(input().rstrip())
N = int(input())

cmds = [input().rstrip() for _ in range(N)]

strings_l = strings
strings_r = []

for cmd in cmds:
    if cmd[0] == "L":
        if len(strings_l) == 0: continue
        else:
            pop_str = strings_l.pop()
            strings_r.append(pop_str)
    elif cmd[0] == "D":
        if len(strings_r) == 0: continue
        else:
            pop_str = strings_r.pop()
            strings_l.append(pop_str)
    elif cmd[0] == "B":
        if len(strings_l) == 0: continue
        else:
            strings_l.pop()
    elif cmd[0] == "P":
        strings_l.append(cmd.split(" ")[1])
    else:
        print("[Error] need check")

print("".join(strings_l + strings_r[::-1]))