"""
1. 아이디어
- 소수: 1보다 큰 자연수 중. 1과 자기 자신만을 약수로 가지는 수
- for문을 돌면서 나눴을 때 나머지가 0이 아니면 카운트 증가
2. 시간복잡도
- 입력: O(N)
- for문 돌면서 나누기: O(N) * O(1)
3. 변수
- N: int, 개수
- nums: list[int], 주어진 수
"""

import sys
import math
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

count = 0

for each_num in nums:
    if each_num == 1:
        continue
    is_prime = True
    for i in range(2, int(math.sqrt(each_num))+1):
        if each_num % i == 0:
            is_prime = False
            break
    if is_prime == True:
        count += 1
print(count)