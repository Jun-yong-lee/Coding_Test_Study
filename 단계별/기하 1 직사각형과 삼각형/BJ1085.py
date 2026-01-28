import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())
print(min((min(x-0, abs(x-w))), (min(y-0, abs(y-h)))))