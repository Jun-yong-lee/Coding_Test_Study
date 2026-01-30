import sys
input = sys.stdin.readline

N = int(input())
name_dict = {}
res = []
for _ in range(N):
    name, el = input().rstrip().split()
    name_dict[name] = name_dict.get(name, 0) + 1
    if name_dict[name] == 2:
        name_dict[name] = 0

for each in name_dict:
    if name_dict[each] == 1:
        res.append(each)

res.sort(reverse=True)

for i in res:
    print(i)
    
# 5
# Baha enter
# Askar enter
# Baha leave
# Baha enter
# Artem enter