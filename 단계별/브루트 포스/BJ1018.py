import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]

b_arr = "BWBWBWBW WBWBWBWB BWBWBWBW WBWBWBWB BWBWBWBW WBWBWBWB BWBWBWBW WBWBWBWB"
w_arr = "WBWBWBWB BWBWBWBW WBWBWBWB BWBWBWBW WBWBWBWB BWBWBWBW WBWBWBWB BWBWBWBW"
b_arr = list(b_arr.rstrip().split())
w_arr = list(w_arr.rstrip().split())

def check(arr): # arr = (8x8)
    count_w = 0
    count_b = 0

    for i in range(8):
        for j in range(8):
            if arr[i][j] != b_arr[i][j]:
                count_b += 1

    for i in range(8):
        for j in range(8):
            if arr[i][j] != w_arr[i][j]:
                count_w += 1

    return min(count_b, count_w)

res = []

for i in range(0, N - 8 + 1):
    for j in range(0, M - 8 + 1):
        slicing = []
        for row in arr[i:i+8]:
            slicing.append(row[j:j+8])
        count = check(slicing)
        res.append(count)
print(min(res))