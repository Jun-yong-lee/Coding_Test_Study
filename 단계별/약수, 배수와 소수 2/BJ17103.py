import sys
input = sys.stdin.readline

def soe(N):
    arr = [True] * (N+1)
    arr[0] = arr[1] = False
    for i in range(2, int(N**(0.5))+1):
        for j in range(i*i, N+1, i):
            arr[j] = False

    return arr

N = int(input())

MAX_N = 1000000
is_prime = soe(MAX_N)

for _ in range(N):
    M = int(input())
    count = 0

    for i in range(2, M//2 + 1):
        if is_prime[i] and is_prime[M-i]:
            count += 1
    print(count)