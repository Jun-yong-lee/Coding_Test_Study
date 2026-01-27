import sys
input = sys.stdin.readline

N = int(input().strip())

if N == 1:
    print("1")
else:
    layer = 1
    end = 1

    while N > end:
        layer += 1
        end += 6 * (layer - 1)

    print(layer)