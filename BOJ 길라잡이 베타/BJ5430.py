"""
1. 아이디어
- 명령 문자열 p를 한 글자씩 리스트로 받아 순차적으로 처리
- 정수 배열은 deque로 만들어 양쪽에서 O(1)로 삭제 가능하게 함
- R 명령은 실제로 배열을 뒤집지 않고, 방향 플래그(reverse_flag)를 토글해서 논리적으로만 방향을 변경**
- D 명령은 방향 플래그에 따라 앞 또는 뒤에서 원소를 제거
- 중간에 비어 있는 배열에서 D가 나오면 바로 error 출력
- 모든 명령 처리 후, 방향 플래그가 뒤집힌 상태면 deque를 한 번 뒤집고 출력

2. 시간복잡도
- 각 테스트케이스마다:
    - p의 길이를 P, 배열의 길이를 N이라 하면
    - 명령 순회: O(P) (각 명령 문자마다 R, D 처리 O(1))
    - D 연산으로 인한 삭제: 최대 N번, 각 O(1)
    - 최종 reverse 또는 출력: O(N)
- 한 테스트케이스의 전체 시간복잡도: O(P + N)
- 문제에서 P = 100, N = 1e5, T = 100, --> 100 * (1e5 + 1e5) = 2 * 1e7 가능

3. 변수
- T: int, 테스트 케이스 개수
- p: list[str], 명령 문자열 (R, D로 구성)
- N: int, 배열의 길이(입력으로 주어지는 숫자 개수)
- s: str, 입력으로 받은 배열 문자열
- nums: deque[int], 현재 남아 있는 정수 배열
- reverse_flag: int, 현재 방향 (짝수 = 정방향, 홀수 = 역방향)
- possible: bool, 중간에 error 발생 여부
"""

import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for i in range(T):
    p = list(input().rstrip())
    N = int(input())
    s = input().rstrip()
    possible = True
    reverse_flag = 0

    if s == "[]": nums = list([])
    else: nums = list(map(int, s[1:-1].split(",")))
    nums = deque(nums)

    for each_p in p:
        if each_p == "R":
            reverse_flag += 1
        elif each_p == "D":
            if len(nums) != 0:
                if reverse_flag % 2 == 1:
                    nums.pop()
                else:
                    nums.popleft()
            else:
                possible = False
                break
    if possible:
        if reverse_flag % 2 == 1:
            nums.reverse()
        print("["+",".join(map(str, nums))+"]")
    else:
        print("error")