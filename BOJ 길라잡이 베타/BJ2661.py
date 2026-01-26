"""
1. 아이디어
- 길이 N인 수열을 앞에서부터 한 자리씩 채워나가는 백트래킹 활용
- 각 자리에 올 수 있는 숫자는 1, 2, 3 뿐이므로, 현재 수열에 "1", "2", "3"을 차례로 붙여보면서 탐색
- 새로운 숫자를 붙인 뒤, 현재 수열이 "좋은 수열"인지 매번 검사
    - 좋은 수열 판별: 어떤 길이 k에 대해, 뒤에서 k개, 그 앞의 k개가 완전히 같으면 나쁜 수열이므로 False
- 나쁜 수열이면 그 수열로는 절대 답을 만들 수 없으므로 즉시 되돌아감
- 1, 2, 3 순서로 시도하기 때문에, DFS로 내려가다가 처음으로 길이 N에 도달한 수열이 사전순으로 가장 작은 좋은 수열 --> 바로 출력 후 탐색 종료

2. 시간복잡도
- 최악의 완전탐색: 각 자리에 3가지 선택 --> 3^N 가지 수열
    - 가지치기를 통해 실제로 탐색하는 경우의 수는 3^N보다 훨씬 적음
- 한 단계에서 좋은 수열 판별(is_good):
    - 수열 길이를 L이라 하면, k = 1 ~ L//2에 대해
        - 마지막 k개와 그 앞의 k개 비교
    - 느슨하게 상한을 잡으면 O(L^2) 정도
- 전체: 이론상 상한은 O(탐색 노드 수 * N^2) n이 80보다 작거나 같으므로, 가능

3. 변수
- N: int, 수열의 길이
- answer: str, 처음으로 찾은 길이 N의 좋은 수열(사전순 최소)
"""

import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())

answer = None

def is_good(seq):
    L = len(seq)
    for k in range(1, L//2+1):
        if seq[-k:] == seq[-2*k:-k]:
            return False
    return True

def dfs(seq):
    global answer

    if answer is not None:
        return
    
    if len(seq) == N:
        answer = seq
        print(answer)
        return
    
    for ch in "123":
        new_seq = seq + ch
        if is_good(new_seq):
            dfs(new_seq)

dfs("")