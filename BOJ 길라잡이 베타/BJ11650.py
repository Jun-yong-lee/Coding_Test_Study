"""
1. 아이디어
- N개의 점을 입력받아 리스트에 저장
- x좌표 순으로 정렬 & x좌표가 같으면 y좌표 순으로 정렬

2. 시간복잡도
- 입력: O(N)
- 정렬: O(NlogN)
- join: O(N)

3. 변수
- N: int, 2차원 평면 위의 점
- coords: list[int], 2차원 평면 위의 점 위치
"""

import sys

input = sys.stdin.readline

N = int(input())
coords = [list(map(int, input().split(" "))) for _ in range(N)]

coords = sorted(coords, key=lambda x:(x[0], x[1]))
for each_coord in coords:
    print(" ".join(list(map(str, each_coord))))