import sys
input = sys.stdin.readline

N, B = map(int, input().split())
remain = 0
results = []

while N != 0:
    remain = N % B
    N = N // B
    if remain > 9:
        results.append(chr(remain+55))
    else:
        results.append(remain)

print("".join(list(map(str, results[::-1]))))
