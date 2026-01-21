"""
1. 아이디어
- A, B 정렬 후 B를 reverse
- for문을 돌면서 A, B를 곱하면서 더함

2. 시간복잡도
- 입력: 모름
- 정렬: O(NlogN)
- for: O(N)

3. 변수
- N: int, 전체 수
- A: list[int], A의 원소
- B: list[int], B의 원소
- total: int, 합 저장

"""

import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

B = B[::-1]

total = 0

for i in range(N):
    total += A[i] * B[i]

print(total)