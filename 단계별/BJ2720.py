import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    change = int(input())
    a = change // 25
    b = (change % 25) // 10
    c = ((change % 25) % 10) // 5
    d = (((change % 25) % 10) % 5) // 1
    print(a, b, c, d)