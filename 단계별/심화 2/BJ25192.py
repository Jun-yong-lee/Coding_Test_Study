import sys
input = sys.stdin.readline

N = int(input())
chattings = []
count = 0

for _ in range(N):
    chat = input().rstrip()
    if chat == "ENTER":
        count += len(set(chattings))
        chattings = []
    else:
        chattings.append(chat)
count += len(set(chattings))

print(count)