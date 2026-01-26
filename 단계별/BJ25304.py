import sys
input = sys.stdin.readline

x = int(input())
N = int(input())

total = 0

for _ in range(N):
    a, b = map(int, input().split())
    total += a * b
if total == x:
    print("Yes")
else:
    print("No")