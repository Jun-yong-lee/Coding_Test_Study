import sys
input = sys.stdin.readline

N = int(input())
res = []

i = 665
count = 0

while True:
    i += 1

    if "666" in str(i):
        count += 1
    if count >= N:
        print(i)
        break