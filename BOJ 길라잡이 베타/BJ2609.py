"""
1. 아이디어
- 유클리드 호제법으로 최대공약수(GCD) 도출
  - gcd(a, b): b가 0이 될 때까지 a, b = b, a % b 반복 --> 마지막 a가 GCD
- 최소공배수(LCM)는 두 수의 곱을 GCD로 나눈 값: LCM = N * M // GCD

2. 시간복잡도
- 유클리드 호제법: O(log(min(N, M)))
- 곱셈, 나눗셈: O(1)

3. 변수
- N, M: int, int, 입력으로 받은 두 자연수
- gcd_number: int, 최대공약수
- lcd_number: int, 최소공배수
"""

import sys
input = sys.stdin.readline
N, M = map(int, input().split())

def gcd(N, M):
    while M != 0:
        N, M = M, N % M
    return N

gcd_number = gcd(N, M)
lcd_number = N * M // gcd_number

print(gcd_number)
print(lcd_number)