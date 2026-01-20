"""
1. 아이디어
- N개의 수를 입력받아 정렬

2. 시간복잡도
- N개 입력: O(N)
- N개 정렬: O(NlogN)
- 1e6 * log(1e6) = 1e6 * 20 = 2e7 --> 가능

3. 변수
- N: int[], 수의 개수
- nums: list[int], 입력 수 저장
"""

import sys
input = sys.stdin.readline
N = int(input())

nums = [int(input()) for _ in range(N)]
nums.sort()

for each_num in nums:
    print(each_num)