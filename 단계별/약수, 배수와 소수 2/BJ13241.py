import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def gcd(a, b):
    while True:
        if b == 0:
            break
        a, b = b, a % b
    return a

gcd_value = gcd(a, b)
print((a * b) // gcd_value)