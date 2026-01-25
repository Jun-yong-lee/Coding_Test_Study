"""
1. 아이디어
- 조건문 활용 분기 체크
2. 시간복잡도
- O(1)
3. 변수
- a, b, c: int, int, int, 3개의 주사위 눈
"""

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

if a==b and b==c:
    print(10000 + a * 1000)
elif a==b or a==c:
    print(1000 + a * 100)
elif b==c:
    print(1000 + b * 100)
else:
    print(max(a, b, c) * 100)