import sys
input = sys.stdin.readline

def soe(N):
    arr = [1] * (2*N + 1)
    arr[0] = arr[1] = 0
    for i in range(2, int((2*N)**(0.5)) + 1):
        for j in range(i*i, 2*N + 1, i):
            arr[j] = 0
    print(sum(arr[N+1:]))

while True:
    N = int(input())
    if N == 0:
        break
    soe(N)