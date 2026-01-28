import sys
input = sys.stdin.readline

N = int(input())

possitive = False

for i in range(1, N):
    total = 0
    i_str = list(str(i))
    total += i
    for j in range(len(i_str)):
        total += int(i_str[j])
    if total == N:
        print("".join(i_str))
        possitive = True
        break
if possitive == False:
    print("0")