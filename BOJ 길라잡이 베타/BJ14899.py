"""
1. 아이디어
- 사람 번호를 0부터 N-1까지 부여하고, 이 중에서 N//2명을 뽑아 스타트 팀으로 사용한다.
- itertools.combinations(range(N), N//2)를 이용해 가능한 스타트 팀 조합을 모두 생성한다.
- 각 스타트 팀 조합에 대해, 포함되지 않은 나머지 사람들로 링크 팀을 구성한다.
- 한 팀의 능력치는 해당 팀에 속한 사람들 중 2명을 뽑는 조합(combinations(team, 2))을 모두 돌며
  S[i][j] + S[j][i]를 합산하여 구한다.
- 스타트 팀과 링크 팀의 능력치 차이의 절댓값을 구하고, 그 중 최솟값을 갱신한다.

2. 시간복잡도
- 팀을 나누는 경우의 수: C(N, N//2)
- 팀 하나의 능력치 계산: 조합 개수 C(N//2, 2) ≈ O((N//2)^2) = O(N^2)
- 두 팀(스타트, 링크)을 모두 계산하므로 상수 배를 곱한 수준이므로 여전히 O(N^2)로 본다.
- 전체 시간복잡도: O(C(N, N//2) * N^2)
  (N ≤ 20인 경우 C(20, 10) ≈ 1.8e5, N^2 = 400 정도여서 충분히 가능)

3. 변수
- N: int, 전체 사람 수 (짝수)
- S: list[list[int]], 크기 N×N의 능력치 행렬, S[i][j]는 i와 j가 같은 팀일 때의 능력치 기여도
- ans: int, 두 팀 능력치 차이의 최솟값을 저장하는 변수 (초기값은 무한대)
- team_score(team): 주어진 팀(team: iterable[int])의 총 능력치를 계산해 반환하는 함수
    - team: iterable[int], 같은 팀에 속한 사람들의 인덱스 집합
    - score: int, 해당 팀의 능력치 합
- start_team: tuple[int], combinations로 뽑힌 스타트 팀 인덱스 조합
- link_team: list[int], start_team에 속하지 않은 나머지 사람들로 구성된 링크 팀 인덱스 리스트
- number: int, 0부터 N-1까지를 순회하며 링크 팀을 만들 때 사용하는 임시 변수
- start_score: int, 현재 스타트 팀의 능력치 합
- link_score: int, 현재 링크 팀의 능력치 합
- diff: int, 현재 스타트 팀과 링크 팀 능력치의 절댓값 차이
"""

import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
ans = float('inf')

def team_score(team):
    score = 0
    for i, j in combinations(team, 2):
        score += S[i][j] + S[j][i]
    return score

for start_team in combinations(range(N), N//2):
    link_team = []
    for number in range(N):
        if number not in start_team:
            link_team.append(number)

    start_score = team_score(start_team)
    link_score = team_score(link_team)
    
    diff = abs(start_score - link_score)
    ans = min(ans, diff)

print(ans)
