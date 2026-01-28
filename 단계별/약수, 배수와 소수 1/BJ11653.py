import sys
input = sys.stdin.readline

N = int(input())
res = []
i = 2

while True:
    if N < i:
        break

    if N % i == 0:
        N = N // i
        res.append(i)
        i = 2
    else:
        i += 1

for each_res in res:
    print(each_res)