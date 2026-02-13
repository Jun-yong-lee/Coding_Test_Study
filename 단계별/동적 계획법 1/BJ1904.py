import sys
input = sys.stdin.readline

N = int(input())

if N == 1:
    print("1")
else:
    arr = [0] * (N+1)
    arr[1] = 1
    arr[2] = 2

    for i in range(3, N+1):
        # 메모리 관리 필요
        arr[i] = (arr[i-2] + arr[i-1]) % 15746
    print(arr[N])


if N == 1:
    print("1")
else:
    a = 1
    b = 2

    for i in range(3, N+1):
        a, b = b, (a+b) % 15746
    print(b)