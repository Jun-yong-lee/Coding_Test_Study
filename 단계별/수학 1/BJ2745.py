import sys
input = sys.stdin.readline

N, B = input().split()

list_n = list(N[::-1])
res = 0
for i in range(len(N)):
    if list_n[i] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
       res += (ord(list_n[i])-55) * int(B)**i
    else:
        res += int(list_n[i]) * int(B)**i
print(res)