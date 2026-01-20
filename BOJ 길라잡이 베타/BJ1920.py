"""
1. 아이디어
- N개의 숫자를 정렬
- M개를 for 돌면서, 이진탐색
- 이진탐색 안에서 마지막에 데이터 찾으면, 1출력, 아니면 0출력

2. 시간복잡도
- N개의 수 정렬: O(NlogN)
- M개의 수 이진탐색: O(MlogN), 이진탐색: O(logN)
- O((N+M)logN) = (1e5+1e5)log(1e5) = 2e5*20 = 4e6 -> 가능
- 가능

3. 변수
- N개의 숫자: int[]
- M개의 숫자: int[]
"""

import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

nums.sort()

def binary_search(st, en, target):
    if st == en:
        if nums[st] == target:
            print("1")
        else:
            print("0")
        return
    mid = (st + en) // 2
    if nums[mid] < target:
        binary_search(mid + 1, en, target)
    else:
        binary_search(st, mid, target)


for target in targets:
    binary_search(0, N-1, target)