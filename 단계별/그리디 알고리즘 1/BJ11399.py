import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

nums.sort()
total = 0

for i in range(len(nums)):
    total += sum(nums[:i+1])
    
print(total)