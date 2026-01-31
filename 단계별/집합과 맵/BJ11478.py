import sys
input = sys.stdin.readline

strings = input().rstrip()
res = []
for i in range(len(strings)+1):
    for j in range(len(strings)+1):
        res.append(strings[i:j])


res = list(set(res))
print(len(res)-1)

# ababc