"""
1. 아이디어
- stack 자료 구조를 활용하여 문자열 왼쪽부터 push, pop 진행
- stack이 비어있을 때 ")" 문자가 push될 시 NO
- 문자열 끝까지 처리한 뒤 stack이 비어 있으면 YES, 남아 있으면 NO

2. 시간복잡도
- 입력: O(N)
- for: O(N) * O(50)

3. 변수
- string_list, list[str], 빈 스택
"""

import sys

input = sys.stdin.readline
N = int(input())

test_data = [list(input().rstrip()) for _ in range(N)]

for each_data in test_data:
    vps = True
    string_list = []
    for each_str in each_data:
        if each_str == "(":
            string_list.append(each_str)
        if each_str == ")":
            if len(string_list) == 0:
                vps = False
                break
            string_list.pop()
    if len(string_list) == 0 and vps: print("YES")
    else: print("NO")