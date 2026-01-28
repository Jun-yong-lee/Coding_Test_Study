import sys
input = sys.stdin.readline

N = int(input())
x_list = []
y_list = []

for _ in range(N):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

dx = max(x_list) - min(x_list)
dy = max(y_list) - min(y_list)
print(dx * dy)