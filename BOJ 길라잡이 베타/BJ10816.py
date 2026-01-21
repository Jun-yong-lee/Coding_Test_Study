"""
1. 아이디어
- 딕셔너리 자료 구조를 활용하여 존재하면 카운트 증가
- 딕셔너리 키 접근으로 빠르게 개수 카운트

2. 시간복잡도
- 입력: O(N)
- 딕셔너리 활용 카운트 증가: O(N)
- 출력: O(M)

3. 변수
- N: int, N 숫자 카드
- M: int, M 숫자 카드
- nums_n: list[int], N 숫자카드
- nums_m: list[int], M 숫자카드
- dict_count: dict[int, int], 숫자 -> 등장 횟수
"""

import sys

input = sys.stdin.readline

N = int(input())
nums_n = list(map(int, input().split(" ")))
M = int(input())
nums_m = list(map(int, input().split(" ")))

dict_count = {}

# for each_num_n in nums_n:
#     dict_count[each_num_n] = dict_count.get(each_num_n, 0) + 1

for each_nums_n in nums_n:
    if each_nums_n in dict_count:
        dict_count[each_nums_n] += 1
    else:
        dict_count[each_nums_n] = 1

for each_num_m in nums_m:
    print(dict_count.get(each_num_m, 0), end=" ")