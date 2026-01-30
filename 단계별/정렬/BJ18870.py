import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

nums_sort = sorted(list(set(nums)))
res = []

def binary_search(st, ed, target):
    if st == ed:
        res.append(st)
        return
    
    mid = (st + ed) // 2

    if target > nums_sort[mid]:
        binary_search(mid+1, ed, target)
    else:
        binary_search(st, mid, target)

for i in range(len(nums)):
    binary_search(0, len(nums_sort), nums[i])

print(" ".join(list(map(str, res))))