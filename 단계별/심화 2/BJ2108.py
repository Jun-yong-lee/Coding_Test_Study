import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

nums.sort()

mean = 0
dict_num = {}
res = []

for each_num in nums:
    mean += each_num
    dict_num[each_num] = dict_num.get(each_num, 0) + 1

for k, v in dict_num.items():
    if v == max(dict_num.values()):
        res.append(k)
res.sort()

print(round(mean / N))
print(nums[N//2])
if len(res) == 1:
    print(res[0])
else:
    print(res[1])
print(nums[-1] - nums[0])
