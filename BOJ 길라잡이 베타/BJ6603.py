"""
1. 아이디어
- 조합 활용

2. 시간복잡도
- 입력: O(N)
- combinations: O(nCr)

3. 변수
- nums: list[int], 숫자 저장
"""

import sys
from itertools import combinations

input = sys.stdin.readline

def combi(iter, r):
    arr = list(iter)
    n = len(arr)
    result = []
    path = []

    def dfs(start):
        if len(path) == r:
            result.append(tuple(path))
            return
        
        for i in range(start, n):
            path.append(arr[i])
            dfs(i + 1)
            path.pop()

    dfs(0)
    return result

while True:
    s = input().rstrip()
    if s == "0":
        break
    else:
        nums = list(map(int, s.split()))[1:]
        for i in combi(nums, 6):
            print(" ".join(map(str, i)))

        # for i in combinations(nums, 6):
        #     print(" ".join(map(str, i)))
        print()