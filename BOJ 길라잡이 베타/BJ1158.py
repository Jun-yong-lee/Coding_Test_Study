"""
1. 아이디어
- 1번부터 N번까지 원형 구조이므로 큐 자료구조 활용
- K번째 사람은 최종 nums에 저장

2. 시간복잡도
- 큐 생성: O(N)
- 각 단계에서 K-1번 회전 + 1번 제거 -> O(K)
- 총 N명이 제거되므로: O(NK)
3. 변수
- N, K: N명, 사람 제거
- nums: deque[int], 순서 저장
"""

import sys
from collections import deque

input = sys.stdin.readline
N, K = list(map(int, input().split()))
people_q = deque(list(range(1, N+1)))
nums = deque()

while len(people_q) != 1:
    for _ in range(K-1):
        people_q.append(people_q.popleft())
    nums.append(str(people_q.popleft()))
nums.append(str(people_q[-1]))

print("<"+", ".join(nums)+">")