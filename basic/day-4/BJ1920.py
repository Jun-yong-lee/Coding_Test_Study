import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))

M = int(input())
nums = list(map(int, input().split()))

for each_num in nums:
    if each_num in A:
        print("1")
    else:
        print("0")

# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

M = int(input())
nums = list(map(int, input().split()))

A.sort()

def binary_search(A, target):
    left = 0
    right = len(A) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == A[mid]:
            return 1

        if A[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

for each_num in nums:
    print(binary_search(A, each_num))

# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5