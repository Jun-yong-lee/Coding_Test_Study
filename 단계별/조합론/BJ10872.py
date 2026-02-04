import sys
input = sys.stdin.readline

N = int(input())

# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n-1)

# print(factorial(N))
res = 1
for i in range(1, N+1):
    res *= i
print(res)