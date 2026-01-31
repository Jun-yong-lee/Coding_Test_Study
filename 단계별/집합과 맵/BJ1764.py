import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name_dict = {}
res = []

for _ in range(N):
    name = input().rstrip()
    name_dict[name] = name_dict.get(name, 0) + 1

for _ in range(M):
    name = input().rstrip()
    if name_dict.get(name, 0) == 1:
        res.append(name)
res.sort()
print(len(res))
for i in range(len(res)):
    print(res[i])


# 3 4
# ohhenrie
# charlie
# baesangwook
# obama
# baesangwook
# ohhenrie
# clinton