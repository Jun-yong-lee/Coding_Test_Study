"""
1. 아이디어
- 리스트를 활용하여 스택 구현
- push, pop, size, empty, top 구현
- push 명령에만 정수 X를 처리하는 로직 필요

2. 시간복잡도
- N: O(N) * O(1)
- push, pop, size, empty, top: O(N)
- 출력: O(N)

3. 자료
- nums: list[int]
"""

import sys

input = sys.stdin.readline

N = int(input())
orders = [input() for _ in range(N)]
nums = []

for order in orders:
    if order[:4] == "push":
        nums.append(int(order[5:]))
    elif order[:3] == "pop":
        if len(nums) != 0:
            num_pop = nums.pop()
            print(num_pop)
        else: print("-1")
    elif order[:4] == "size":
        print(len(nums))
    elif order[:5] == "empty":
        if len(nums) != 0: print("0")
        else: print("1")
    elif order[:3] == "top":
        if len(nums) != 0: print(nums[-1])
        else: print("-1")
    else:
        print("[Error] need check")