# 5
# 6 3 2 10 -10
# 8
# 10 9 -5 2 3 4 5 -10

import sys
input = sys.stdin.readline

N = int(input())
n_set = set(map(int, input().split()))

M = int(input())
m_list = list(map(int, input().split()))

for i in range(M):
    if m_list[i] in n_set:
        print("1", end=" ")
    else:
        print("0", end=" ")