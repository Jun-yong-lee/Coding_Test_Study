# """
# 1. 아이디어
# - N개의 수를 set에 저장
# - M개의 수에 대해, 각 수가 set에 존재하는지 확인
# - 존재하면 1, 아니면 0을 공배긍로 구분해 출력

# 2. 시간복잡도
# - 입력: O(N) + O(M)
# - set 생성: N개 삽입 -> 평균 O(N)
# - 존재 여부 확인: M x O(1) --> O(M)
# - 출력: O(M)

# 3. 변수
# - N: int[], N의 개수
# - M: int[], M의 개수
# - nums_N: set[int] --> set hash 활용
# - nums_M: list[int]
# """

# import sys

# input = sys.stdin.readline

# N = int(input())
# nums_N = set(map(int, input().split()))
# M = int(input())
# nums_M = list(map(int, input().split()))

# for num_M in nums_M:
#     if num_M in nums_N:
#         print("1", end=" ")
#     else:
#         print("0", end=" ")



"""
1. 아이디어
- N개의 수를 정렬
- M개의 수에 대해, 각 수가 N개의 수에 존재하는지 이진탐색
- 존재하면 1, 아니면 0을 공배긍로 구분해 출력

2. 시간복잡도
- 입력: O(N) + O(M)
- N개의 수 정렬: O(NlogN)
- 존재 여부 확인: M x O(logN) --> O(MlogN)
- 출력: O(M)

3. 변수
- N: int[], N의 개수
- M: int[], M의 개수
- nums_N: list[int]
- nums_M: list[int]
"""

import sys

input = sys.stdin.readline

N = int(input())
nums_N = list(map(int, input().split()))
M = int(input())
nums_M = list(map(int, input().split()))

nums_N.sort()

def binary_search(st, en, target):
    if st == en:
        if nums_N[st] == target:
            print("1", end=" ")
        else:
            print("0", end=" ")
        return
    
    mid = (st + en) // 2
    if target > nums_N[mid]:
        binary_search(mid+1, en, target)
    else:
        binary_search(st, mid, target)


for num_M in nums_M:
    binary_search(0, N-1, num_M)