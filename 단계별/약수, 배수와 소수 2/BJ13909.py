import sys
input = sys.stdin.readline

N = int(input())

# 시간 초과
# arr = [0] * (N + 1)

# for i in range(1, N+1):
#     for j in range(i, N+1, i):
#         if arr[j] == 0:
#             arr[j] = 1
#         else:
#             arr[j] = 0
# print(sum(arr[1:]))
# print(arr[1:])

print(int(N**(0.5)))