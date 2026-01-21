"""
1. 아이디어
- 큐와 중요도를 이용 [idx, 중요도]
- 중요도에서부터 max값을 뽑아와 비교
- max값과 같다면 인쇄, 아니면 뒤로 재배치
2. 시간복잡도
- 큐 연산은 최대 N번 수행: O(N)
- 각 반복마다 max 연산: O(N)
- popleft, append: O(1)
- 전체: O(N^2) --> N이 최대 100이므로 현재 알고리즘으로는 가능, 추후 중요도를 sort하여 NlogN으로 변경하는 작업 필요
3. 변수
- N: int, 문서의 개수
- M: int, 몇 번째로 인쇄되었는지 궁금한 문서의 위치
"""

import sys
from collections import deque

input = sys.stdin.readline
test_data = int(input())

for i in range(test_data):
    idx_im = []
    count = 0
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))

    for idx in range(N):
        idx_im.append([idx, importance[idx]])
    
    idx_im = deque(idx_im)
    while len(idx_im) != 0:
        if idx_im[0][1] == max(idx_im, key=lambda x:x[1])[1]:
            count += 1
            if idx_im[0][0] == M:
                print(count)
                break
            idx_im.popleft()
        else:
            idx_im.append(idx_im.popleft())