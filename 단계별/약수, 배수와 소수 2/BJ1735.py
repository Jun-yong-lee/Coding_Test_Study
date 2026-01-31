import sys
input = sys.stdin.readline

n1, d1 = map(int, input().split())
n2, d2 = map(int, input().split())

numerator = n1 * d2 + n2 * d1
denominator = d1 * d2

def gcd(a, b):
    while True:
        if b == 0:
            break
        a, b = b, a % b
    return a

gcd_value = gcd(numerator, denominator)
print(numerator // gcd_value, denominator // gcd_value)

# 2 7
# 3 5