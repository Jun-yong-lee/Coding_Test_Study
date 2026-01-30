import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n_set = set([input().rstrip() for _ in range(N)])
m_list = [input().rstrip() for _ in range(M)]

count = 0

for each_m in m_list:
    if each_m in n_set:
        count += 1
print(count)

# 5 11
# baekjoononlinejudge
# startlink
# codeplus
# sundaycoding
# codingsh
# baekjoon
# codeplus
# codeminus
# startlink
# starlink
# sundaycoding
# codingsh
# codinghs
# sondaycoding
# startrink
# icerink