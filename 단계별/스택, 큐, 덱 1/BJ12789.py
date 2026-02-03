import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
stack = []
count = 1

for each_num in nums:
    stack.append(each_num)
    while stack and stack[-1] == count:
        stack.pop()
        count += 1
                
if len(stack) == 0:
    print("Nice")
else:
    print("Sad")
        

        
