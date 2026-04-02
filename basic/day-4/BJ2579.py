import sys

input = sys.stdin.readline

n = int(input())
s = [0] * 301
for i in range(1, n+1):
    s[i] = int(input())

dp = [0] * 301
dp[1] = s[1]

if n >= 2:
    dp[2] = s[1] + s[2]
if n >= 3:
    dp[3] = max(s[1] + s[3], s[2] + s[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-2] + s[i], dp[i-3] + s[i-1] + s[i])

print(dp[n])
# 6
# 10
# 20
# 15
# 25
# 10
# 20