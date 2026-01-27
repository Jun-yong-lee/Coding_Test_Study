import sys
input = sys.stdin.readline
import math

M = int(input())
N = int(input())

res = []

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for i in range(M, N+1):
    if is_prime(i):
        res.append(i)

if sum(res) == 0:
    print("-1")
else:
    print(sum(res))
    print(res[0])
