"""
1. 아이디어
- 1, 2, 3으로 만들 수 있는 길이 1~n의 모든 수열 생성
- 각 수열의 원소 합이 정수 n과 같으면 카운트
- for문으로 길이 i를 1부터 n까지 증가시키며 product를 사용해 모든 수열 생성

2. 시간복잡도
- 입력: O(T)
- 길이 i(1 ~ n)인 수열 개수: 3^i
- 전체 생성하는 수열 개수: 3^1 + 3^2 + ... + 3^n ≈ O(3^n)
- 각 수열에서 합 계산: O(i) ≤ O(n)
- 전체 시간복잡도: O(n * 3^n)
  (이 문제에서 n ≤ 10이므로 실제 연산량은 약 10 * 3^10 ≈ 6e5로 충분히 가능)

3. 변수
- T: int, 테스트 케이스 개수
- n: list[int], 입력 정수
"""

import sys
from itertools import product

input = sys.stdin.readline
count = 0

T = int(input())
n = [int(input()) for _ in range(T)]
for each_n in n:
    count = 0

    for i in range(1, each_n+1):
        for j in product(range(1, 4), repeat=i):
            if sum(j) == each_n:
                count += 1
    print(count)

# --------------------------------------------------------------------------
"""
1. 아이디어
- arr[i] = arr[i-1] + arr[i-2] + arr[i-3] 점화식 사용
- 입력된 n이 3 이하인 경우는 미리 계산된 값을 사용
- n이 4 이상인 경우, 배열을 만들어 4부터 n까지 순차적으로 계산
2. 시간복잡도
- 입력: O(T)
- 전체: O(sig(n))
- 공간복잡도: O(n)
3. 변수
- T: int, 테스트 케이스 개수
- n: list[int], 입력 정수
- arr: list[int], 점화식을 활용한 합 배열
"""

import sys

input = sys.stdin.readline
count = 0

T = int(input())
n = [int(input()) for _ in range(T)]


for each_n in n:
    if each_n <= 3:
        arr = [0, 1, 2, 4]
    else:
        arr = [0] * (each_n + 1)
        arr[1] = 1
        arr[2] = 2
        arr[3] = 4
        for i in range(4, each_n + 1):
            arr[i] = arr[i-1] + arr[i-2] + arr[i-3]

    print(arr[each_n])