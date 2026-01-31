import sys
input = sys.stdin.readline

def gcd(a, b):
    value = 0
    for i in range(1, min(a, b)+1):
        if a % i == b % i == 0:
            value = i
    return value
    

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    gcd_value = gcd(a, b)
    lcm_value = (a * b) // gcd_value
    print(lcm_value)

# 3
# 1 45000
# 6 10
# 13 17