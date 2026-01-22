# """
# 1. 아이디어
# - combinations를 활용하여 부분수열 구하기
# - 부분수열의 합과 S를 비교하여 개수 카운트

# 2. 시간복잡도
# - 입력: O(N)
# - 길이 1~N 모든 조합 개수: 2^N-1
# - 각 조합에 대해 합 계산: O(N)
# - 전체: O(N * 2^N) -> 2 * 1e7 --> 가능

# 3. 변수
# - N: int, N개의 정수
# - S: int, 목표 합
# - count: int, 합이 S가 되는 부분수열의 개수
# - nums: list[int], 정수 저장
# """

# import sys
# from itertools import combinations

# input = sys.stdin.readline
# N, S = map(int, input().split())

# nums = list(map(int, input().split()))
# count = 0

# for i in range(1, N+1):
#     for combi in combinations(nums, i):
#         if sum(combi) == S:
#             count += 1
# print(count)


"""
1. 아이디어
- 백트래킹 활용
    - 인덱스 idx와 현재까지의 합 cur_sum을 들고 재귀함수 dfs(idx, cur_sum) 생성
    - idx번째 원소에 대해:
        - 포함하는 경우: dfs(idx + 1, cur_sum + nums[idx])
        - 포함하지 않는 경우: dfs(idx + 1, cur_sum)
    - idx == N에 도달하면
        - 지금까지 만든 부분수열의 합 cur_sum이 S와 같으면 count += 1
    - 공집합 처리
2. 시간복잡도
- 입력: O(N)
- 총 N개 원소: 2^N

3. 변수
- N: int, N개의 정수
- S: int, 목표 합
- count: int, 합이 S가 되는 부분수열의 개수
- nums: list[int], 정수 저장
- dfs(idx, cur_sum):
    - idx: 현재 보고 있는 인덱스(0~N)
    - cur_sum: idx 이전까지 선택한 원소들의 합
"""

import sys
input = sys.stdin.readline

N, S = map(int, input().split())

nums = list(map(int, input().split()))
count = 0

def dfs(idx, cur_sum):
    global count

    if idx == N:
        if cur_sum == S:
            count += 1
        return
    
    # 1. idx번째 원소를 선택하는 경우
    dfs(idx + 1, cur_sum + nums[idx])

    # 2. idx번째 원소를 선택하지 않는 경우
    dfs(idx + 1, cur_sum)

dfs(0, 0)

if S == 0:
    count -= 1

print(count)