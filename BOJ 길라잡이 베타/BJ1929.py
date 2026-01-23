"""
1. 아이디어
- 에라토스테네스의 체를 활용하여 M 이상 N 이하의 소수를 구한다
- 2부터 N까지의 모든 수를 소수 후보로 설정한다
- i를 2부터 √N까지 증가시키며 반복한다
    - i가 아직 소수로 남아 있다면,
      i의 배수들은 모두 합성수이므로 제거한다
    - 이때 i 자신은 소수이므로 제거하지 않는다
    - 이미 제거된 수는 다시 처리하지 않는다
- 모든 배수 제거가 끝난 후,
  M 이상 N 이하에서 소수로 남아 있는 수만 출력한다

2. 시간복잡도
- 에라토스테네스의 체의 시간복잡도는 O(N log log N)
- N이 최대 1,000,000이므로 충분히 수행 가능

3. 변수
- M: int, 소수를 출력할 하한값
- N: int, 소수를 출력할 상한값
- prime_list: list[int], 
    - 인덱스가 소수인지 여부를 저장하는 배열
    - prime_list[i] == 1이면 i는 소수, 0이면 합성수
"""

import sys
input = sys.stdin.readline
M, N = map(int, input().split())

prime_list = [1] * (N + 1)
prime_list[0] = prime_list[1] = 0

for i in range(2, int(N**(0.5))+1):
    if prime_list[i]:    
        for j in range(i*i, N+1, i): # i의 배수 지우기
            prime_list[j] = 0

for i in range(M, N+1):
    if prime_list[i] == 1:
        print(i)