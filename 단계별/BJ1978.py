import sys
import math
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
count = 0

for each_num in nums:
    possible = True

    if each_num == 1:
        continue
    if each_num == 2:
        count += 1
        continue

    for i in range(2, int(math.sqrt(each_num))+1):
        if each_num % i == 0:
            possible = False
            break
    if possible == True:
        count += 1
print(count)