import sys
input = sys.stdin.readline

N, K = map(int, input().split())
prices = [int(input()) for _ in range(N)]
prices = sorted(prices, reverse=True)

count = 0

for i in prices:
    if K // i != 0:
        count += K // i
        K = int(K % i)

print(count)

# 10 4200
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000