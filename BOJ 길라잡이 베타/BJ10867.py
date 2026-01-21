"""
1. 아이디어
- N개의 수를 입력받아, 중복제거
- 오름차순 정렬

2. 시간복잡도
- 입력: O(N)
- 중복 제거: O(N)
- 정렬: O(NlogN)

3. 변수
- nums: list[int], N개의 정수 저장
"""

import sys

input = sys.stdin.readline
N = int(input())

nums = list(set(list(map(int, input().split(" ")))))
nums.sort()

for each_num in nums:
    print(each_num, end=" ")