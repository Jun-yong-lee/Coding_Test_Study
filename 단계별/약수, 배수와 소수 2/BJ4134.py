import sys
import math

input = sys.stdin.readline

N = int(input())

def is_prime(num):
    if num == 2:
        return True
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
        

for _ in range(N):
    num = int(input())
    while True:
        if num == 0 or num == 1:
            print("2")
            break
        if is_prime(num):
            print(num)
            break
        num += 1

# 3
# 6
# 20
# 100