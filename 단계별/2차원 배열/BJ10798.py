# ABCDE
# abcde
# 01234
# FGHIJ
# fghij

# AABCDD
# afzz
# 09121
# a8EWg6
# P5h3kx

# AABCDD
#  fzz
#  9121
# a8EWg6
# P5h3kx


import sys
input = sys.stdin.readline

arr = []
res= []
max_length = 0

arr = [list(input().rstrip()) for _ in range(5)]
for i in range(len(arr)):
    if max_length < len(arr[i]):
        max_length = len(arr[i])

for i in range(len(arr)):
    if len(arr[i]) != max_length:
        for _ in range(max_length - len(arr[i])):
            arr[i].append(" ")

for j in range(max_length):
    for i in range(len(arr)):
        if arr[i][j] != " ":
            res.append(arr[i][j])
print("".join(res))

