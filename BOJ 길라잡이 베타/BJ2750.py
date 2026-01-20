"""
1. 아이디어
- for문을 돌면서 N개의 값 입력
- 정렬

2. 시간복잡도
- 입력 저장: O(N)
- 정렬: O(NlogN)
- 전체: O(NlogN)
--> 가능

3. 변수
- N: int[], 수의 개수
- nums: list[int], 입력된 수 저장
"""

import sys

input = sys.stdin.readline
N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input())) # nums = [int(input()) for _ in range(N)]

nums = list(set(nums))
nums.sort()

for each_num in nums:
    print(each_num)