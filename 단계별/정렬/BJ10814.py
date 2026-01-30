import sys
input = sys.stdin.readline

N = int(input())
members = []

for _ in range(N):
    age, name = input().split()
    members.append([int(age), name])
    
members.sort(key=lambda x:x[0])

for i in range(N):
    print(" ".join(list(map(str, members[i]))))