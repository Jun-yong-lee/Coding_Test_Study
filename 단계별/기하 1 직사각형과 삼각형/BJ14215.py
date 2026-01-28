import sys
input = sys.stdin.readline
abc = list(map(int, input().split()))

if max(abc) < sum(abc) - max(abc):
    print(sum(abc))
else:
    print((sum(abc) - max(abc)) + (sum(abc) - max(abc) - 1))