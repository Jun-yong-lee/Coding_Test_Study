import sys
input = sys.stdin.readline

N = int(input())
dance_set = {"ChongChong"}

for _ in range(N):
    p1, p2 = input().split()
    if p1 in dance_set:
        dance_set.add(p2)

    if p2 in dance_set:
        dance_set.add(p1)

print(len(dance_set))