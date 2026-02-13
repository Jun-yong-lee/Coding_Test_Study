import sys
input = sys.stdin.readline

T = int(input())

arr = [0] * 101
arr[0] = 1
arr[1] = 1
arr[2] = 1

for i in range(3, 101):
    arr[i] = arr[i-2] + arr[i-3]

test_case = [int(input()) for _ in range(T)]
for j in range(T):
    print(arr[test_case[j]-1])

# 2
# 6
# 12