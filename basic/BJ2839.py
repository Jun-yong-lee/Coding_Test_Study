# 완전 탐색
import sys
input = sys.stdin.readline

N = int(input())

res = []

for i in range(N):
    for j in range(N):
        if N == 5 * i + 3 * j:
            res.append(i + j)
if len(res) == 0:
    print("-1")
else:
    print(min(res))

# 그리디
import sys
input = sys.stdin.readline

N = int(input())

bags = 0
flag = False

while N >= 0:
    if N % 5 == 0:
        bags += (N // 5)
        flag = True
        print(bags)
        break
    N -= 3
    bags += 1
if flag == False:
    print("-1")