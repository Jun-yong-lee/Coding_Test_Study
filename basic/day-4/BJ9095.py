import sys

input = sys.stdin.readline

results = [0] * 11
results[1] = 1
results[2] = 2
results[3] = 4
results[4] = 7

for i in range(5, len(results)):
    results[i] = results[i-1] + results[i-2] + results[i-3]

T = int(input())
for _ in range(T):
    n = int(input())
    print(results[n])
# 3
# 4
# 7
# 10