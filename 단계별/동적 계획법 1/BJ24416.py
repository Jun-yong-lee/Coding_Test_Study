import sys
input = sys.stdin.readline

n = int(input())

def fibonacci(n):
    f = [0] * (n+1)
    f[1] = f[2] = 1
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n], n-2
res1, res2 = fibonacci(n)
print(res1, res2)


# fib(n) {
#     if (n = 1 or n = 2)
#     then return 1;  # 코드1
#     else return (fib(n - 1) + fib(n - 2));
# }

# fibonacci(n) {
#     f[1] <- f[2] <- 1;
#     for i <- 3 to n
#         f[i] <- f[i - 1] + f[i - 2];  # 코드2
#     return f[n];
# }