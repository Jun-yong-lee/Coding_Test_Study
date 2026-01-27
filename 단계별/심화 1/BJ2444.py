import sys
input = sys.stdin.readline
N = int(input())

for i in range(1, N+1):
    star = i * 2 - 1
    space = N - i
    print(space * " " + star * "*")

for j in range(N-1, 0, -1):
    star = j * 2 - 1
    space = N - j
    print(space * " " + star * "*")