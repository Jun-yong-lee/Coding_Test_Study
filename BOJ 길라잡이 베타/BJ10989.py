"""
1. 아이디어
- N개의 수를 입력받아 계수정렬

2. 시간복잡도
- 입력: O(N)
- 계수정렬: O(N+K) # 카운트 배열 순회 + 총 출력 N회

3. 변수
- N: int[], 입력 개수
- nums: list[int], 0부터 10,001까지의 N의 개수 
"""

import sys

input = sys.stdin.readline
N = int(input())
nums = [0] * 10001

for _ in range(N):
    num = int(input())
    nums[num] += 1

for i in range(1, len(nums[1:])+1):
    if nums[i] != 0:
        for _ in range(nums[i]):
            print(i)