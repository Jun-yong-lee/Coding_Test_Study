import sys
input = sys.stdin.readline

def recursive_function(arr):
    if arr == 1:
        return "-"
    else:
        left = recursive_function(arr // 3)
        center = " " * (arr // 3)
        return left + center + left

while True:
    try:
        N = int(input())
        arr = 3**N
        res = recursive_function(arr)
        print(res)
    except:
        break