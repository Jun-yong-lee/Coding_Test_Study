import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

# 원하는 숫자를 이진 탐색으로 찾기, 매개변수 탐색

start = 0
end = max(trees)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    for each_tree in trees:
        if each_tree > mid:
            total += each_tree - mid
        
    if total >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)