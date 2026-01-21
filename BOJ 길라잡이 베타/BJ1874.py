"""
1. 아이디어
- stack에는 1부터 차례대로 push(현재 목표 값까지 push)
- push가 끝난 시점에서 스택의 top이 현재 목표 값과 같으면 pop
- top이 다르면, 스택 규칙상 해당 수열은 만들 수 없으므로 불가능

2. 시간복잡도
- 입력: O(N)
- push, pop: O(N)
- 전체: O(N)

3. 변수
- N: int, 수열의 수
- nums: list[int], 수열
- stack: list[int], push/pop을 위한 스택
- cur_value: int, 현재 숫자
- operation: list[str], push or pop 연산 저장
- possible: bool, 수열 생성 가능 여부
"""

import sys

input = sys.stdin.readline
N = int(input())
nums = [int(input()) for _ in range(N)]
stack = []
cur_value = 1
operation = []
possible = True

for each_num in nums:
    while cur_value <= each_num:
        stack.append(cur_value)
        operation.append("+")
        cur_value += 1
    
    if stack[-1] == each_num:
        stack.pop()
        operation.append("-")
    else:
        possible = False
        break

if possible:
    for each_operation in operation:
        print(each_operation)
else:
    print("NO")