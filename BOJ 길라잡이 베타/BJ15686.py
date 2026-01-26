"""
1. 아이디어
- 도시 정보를 입력받아, 치킨집과 집의 좌표를 각 리스트에 저장
- 치킨집 리스트와 M을 이용하여 모든 조합 생성
- 각 치킨집 조합에 대해
    - 모든 집을 하나씩 순회하며
        - 선택된 치킨집 중 가장 가까운 치킨집까지의 거리를 계산
    - 각 집의 치킨 거리를 모두 더해 도시 치킨 거리 계산
- 모든 조합에 대해 도시 치킨 거리를 비교하여 최솟값을 갱신
- 최솟값을 두 번 구함
2. 시간복잡도
- 치킨집 개수: C=13
- 집 개수: H=100
- O(13C6 * 100 * 13)
3. 변수
- N: int, 도시의 크기
- M: int, 치킨집의 개수
- arr: list[list[int]], 도시 정보(0: 빈 칸, 1: 집, 2: 치킨집)
- homes: list[tuple[int, int]], 모든 집의 좌표 목록
- chickens: list[tuple[int, int]], 모든 치킨집의 좌표 목록
"""

import sys
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

chickens = []
homes = []
answer = float('INF')

for i in range(0, N):
    for j in range(0, N):
        if arr[i][j] == 1:
            homes.append((i+1, j+1))
        if arr[i][j] == 2:
            chickens.append((i+1, j+1))

for each_chicken in combinations(chickens, M):
    total = 0
    for hx, hy in homes: # 각 집
        min_dist = float("INF")
        for cx, cy in each_chicken: # 각 치킨집
            dist = abs(cx - hx) + abs(cy- hy)
            if dist < min_dist:
                min_dist = dist
        total += min_dist
        if total >= answer:
            break

    if total < answer:
        answer = total
print(answer)