"""
1. 아이디어
- N의 진짜 약수를 입력받아 정렬
- 첫번째 수와 마지막 수를 곱하여 원래의 수 복원
2. 시간복잡도
- 입력: O(N)
- 정렬: O(NlogN)
3. 변수
- nums: list[int], 약수 리스트
"""

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

print(nums[0] * nums[-1])